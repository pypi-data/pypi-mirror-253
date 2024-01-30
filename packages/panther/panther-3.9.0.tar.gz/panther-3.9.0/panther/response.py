from types import NoneType

import orjson as json
from pydantic import BaseModel as PydanticBaseModel
from pydantic._internal._model_construction import ModelMetaclass

ResponseDataTypes = list | tuple | set | dict | int | float | str | bool | bytes | NoneType | ModelMetaclass
IterableDataTypes = list | tuple | set


class Response:
    content_type = 'application/json'

    def __init__(
        self,
        data: ResponseDataTypes = None,
        headers: dict | None = None,
        status_code: int = 200,
    ):
        """
        :param data: should be int | float | dict | list | tuple | set | str | bool | bytes | NoneType
            or instance of Pydantic.BaseModel
        :param status_code: should be int
        """
        self.data = self._clean_data_type(data)
        self._check_status_code(status_code)
        self._headers = headers

    @property
    def body(self) -> bytes:
        if isinstance(self.data, bytes):
            return self.data
        else:
            return json.dumps(self.data)

    @property
    def headers(self) -> dict:
        content_length = 0 if self.body == b'null' else len(self.body)
        return {
            'content-type': self.content_type,
            'content-length': content_length,
            'access-control-allow-origin': '*',
        } | (self._headers or {})

    def _clean_data_type(self, data: any):
        """Make sure the response data is only ResponseDataTypes or Iterable of ResponseDataTypes"""
        if issubclass(type(data), PydanticBaseModel):
            return data.model_dump()

        elif isinstance(data, IterableDataTypes):
            return [self._clean_data_type(d) for d in data]

        elif isinstance(data, dict):
            return {key: self._clean_data_type(value) for key, value in data.items()}

        elif isinstance(data, (int | float | str | bool | bytes | NoneType)):
            return data

        else:
            msg = f'Invalid Response Type: {type(data)}'
            raise TypeError(msg)

    def _check_status_code(self, status_code: any):
        if not isinstance(status_code, int):
            error = f'Response "status_code" Should Be "int". ("{status_code}" is {type(status_code)})'
            raise TypeError(error)

        self.status_code = status_code

    def _clean_data_with_output_model(self, output_model: ModelMetaclass | None):
        if self.data and output_model:
            self.data = self._serialize_with_output_model(self.data, output_model=output_model)

    @classmethod
    def _serialize_with_output_model(cls, data: any, /, output_model: ModelMetaclass):
        # Dict
        if isinstance(data, dict):
            return output_model(**data).model_dump()

        # Iterable
        if isinstance(data, IterableDataTypes):
            return [cls._serialize_with_output_model(d, output_model=output_model) for d in data]

        # Str | Bool | Bytes
        msg = 'Type of Response data is not match with `output_model`.\n*hint: You may want to remove `output_model`'
        raise TypeError(msg)

    def __str__(self):
        if len(data := str(self.data)) > 30:
            data = f'{data:.27}...'
        return f'Response(status_code={self.status_code}, data={data})'

    __repr__ = __str__


class HTMLResponse(Response):
    content_type = 'text/html; charset=utf-8'

    @property
    def body(self) -> bytes:
        if isinstance(self.data, bytes):
            return self.data
        return self.data.encode()


class PlainTextResponse(Response):
    content_type = 'text/plain; charset=utf-8'

    @property
    def body(self) -> bytes:
        if isinstance(self.data, bytes):
            return self.data
        return self.data.encode()
