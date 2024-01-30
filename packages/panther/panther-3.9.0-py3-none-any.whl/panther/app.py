import functools
from collections.abc import Callable
from datetime import datetime, timedelta
import logging
from typing import Literal

from orjson import JSONDecodeError
from pydantic import ValidationError

from panther import status
from panther._utils import is_function_async
from panther.caching import cache_key, get_cached_response_data, set_cache_response
from panther.configs import config
from panther.exceptions import (
    APIException,
    AuthorizationException,
    InvalidPathVariableException,
    JsonDecodeException,
    MethodNotAllowed,
    ThrottlingException,
)
from panther.request import Request
from panther.response import Response
from panther.throttling import Throttling, throttling_storage
from panther.utils import round_datetime

__all__ = ('API', 'GenericAPI')


logger = logging.getLogger('panther')


class API:
    def __init__(
            self,
            *,
            input_model=None,
            output_model=None,
            auth: bool = False,
            permissions: list | None = None,
            throttling: Throttling = None,
            cache: bool = False,
            cache_exp_time: timedelta | int | None = None,
            methods: list[Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE']] | None = None,
    ):
        self.input_model = input_model
        self.output_model = output_model
        self.auth = auth
        self.permissions = permissions or []
        self.throttling = throttling
        self.cache = cache
        self.cache_exp_time = cache_exp_time
        self.methods = methods
        self.request: Request | None = None

    def __call__(self, func):
        @functools.wraps(func)
        async def wrapper(request: Request, **path_variables) -> Response:
            self.request: Request = request  # noqa: Non-self attribute could not be type hinted

            # 1. Check Method
            if self.methods and self.request.method not in self.methods:
                raise MethodNotAllowed

            # 2. Authentication
            self.handle_authentications()

            # 3. Throttling
            self.handle_throttling()

            # 4. Permissions
            self.handle_permissions()

            # 5. Validate Input
            if self.request.method in ['POST', 'PUT', 'PATCH']:
                self.handle_input_validation()

            # 6. Get Cached Response
            if self.cache and self.request.method == 'GET':
                if cached := get_cached_response_data(request=self.request,  cache_exp_time=self.cache_exp_time):
                    return Response(data=cached.data, status_code=cached.status_code)

            # 7. Clean Path Variables
            self.clean_path_variables(func, path_variables)

            # 8. Put Request In kwargs (If User Wants It)
            kwargs = {}
            if req_arg := [k for k, v in func.__annotations__.items() if v == Request]:
                kwargs[req_arg[0]] = self.request

            # 9. Call Endpoint
            if is_function_async(func):
                response = await func(**kwargs, **path_variables)
            else:
                response = func(**kwargs, **path_variables)

            # 10. Clean Response
            if not isinstance(response, Response):
                response = Response(data=response)
            response._clean_data_with_output_model(output_model=self.output_model)  # noqa: SLF001

            # 11. Set New Response To Cache
            if self.cache and self.request.method == 'GET':
                set_cache_response(
                    request=self.request,
                    response=response,
                    cache_exp_time=self.cache_exp_time
                )

            # 12. Warning CacheExpTime
            if self.cache_exp_time and self.cache is False:
                logger.warning('"cache_exp_time" won\'t work while "cache" is False')

            return response

        return wrapper

    def handle_authentications(self) -> None:
        auth_class = config['authentication']
        if self.auth:
            if not auth_class:
                logger.critical('"AUTHENTICATION" has not been set in configs')
                raise APIException
            user = auth_class.authentication(self.request)
            self.request.set_user(user=user)

    def handle_throttling(self) -> None:
        if throttling := self.throttling or config['throttling']:
            key = cache_key(self.request)
            time = round_datetime(datetime.now(), throttling.duration)
            throttling_key = f'{time}-{key}'
            if throttling_storage[throttling_key] > throttling.rate:
                raise ThrottlingException

            throttling_storage[throttling_key] += 1

    def handle_permissions(self) -> None:
        for perm in self.permissions:
            if type(perm.authorization).__name__ != 'method':
                logger.error(f'{perm.__name__}.authorization should be "classmethod"')
                continue
            if perm.authorization(request=self.request) is False:
                raise AuthorizationException

    def handle_input_validation(self):
        if self.input_model:
            validated_data = self.validate_input(model=self.input_model, request=self.request)
            self.request.set_validated_data(validated_data)

    @classmethod
    def validate_input(cls, model, request: Request):
        try:
            if isinstance(request.data, bytes):
                raise APIException(detail='Content-Type is not valid', status_code=status.HTTP_400_BAD_REQUEST)
            return model(**request.data)
        except ValidationError as validation_error:
            error = {'.'.join(loc for loc in e['loc']): e['msg'] for e in validation_error.errors()}
            raise APIException(detail=error, status_code=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            raise JsonDecodeException

    @staticmethod
    def clean_path_variables(func: Callable, request_path_variables: dict):
        for name, value in request_path_variables.items():
            for variable_name, variable_type in func.__annotations__.items():
                if name == variable_name:
                    # Check the type and convert the value
                    if variable_type is bool:
                        request_path_variables[name] = value.lower() not in ['false', '0']

                    elif variable_type is int:
                        try:
                            request_path_variables[name] = int(value)
                        except ValueError:
                            raise InvalidPathVariableException(value=value, variable_type=variable_type)
                    break


class GenericAPI:
    input_model = None
    output_model = None
    auth: bool = False
    permissions: list | None = None
    throttling: Throttling | None = None
    cache: bool = False
    cache_exp_time: timedelta | int | None = None

    async def get(self, *args, **kwargs):
        raise MethodNotAllowed

    async def post(self, *args, **kwargs):
        raise MethodNotAllowed

    async def put(self, *args, **kwargs):
        raise MethodNotAllowed

    async def patch(self, *args, **kwargs):
        raise MethodNotAllowed

    async def delete(self, *args, **kwargs):
        raise MethodNotAllowed

    @classmethod
    async def call_method(cls, *args, **kwargs):
        match kwargs['request'].method:
            case 'GET':
                func = cls().get
            case 'POST':
                func = cls().post
            case 'PUT':
                func = cls().put
            case 'PATCH':
                func = cls().patch
            case 'DELETE':
                func = cls().delete

        return await API(
            input_model=cls.input_model,
            output_model=cls.output_model,
            auth=cls.auth,
            permissions=cls.permissions,
            throttling=cls.throttling,
            cache=cls.cache,
            cache_exp_time=cls.cache_exp_time,
        )(func)(*args, **kwargs)
