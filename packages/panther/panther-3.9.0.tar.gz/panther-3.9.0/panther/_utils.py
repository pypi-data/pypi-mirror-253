import asyncio
import importlib
import logging
import re
import subprocess
import types
from collections.abc import Callable
from traceback import TracebackException
from uuid import uuid4

import orjson as json

from panther import status
from panther.exceptions import PantherException
from panther.file_handler import File

logger = logging.getLogger('panther')


async def _http_response_start(send: Callable, /, headers: dict, status_code: int) -> None:
    bytes_headers = [[k.encode(), str(v).encode()] for k, v in (headers or {}).items()]
    await send({
        'type': 'http.response.start',
        'status': status_code,
        'headers': bytes_headers,
    })


async def _http_response_body(send: Callable, /, body: bytes | None = None) -> None:
    if body is None:
        await send({'type': 'http.response.body'})
    else:
        await send({'type': 'http.response.body', 'body': body})


async def http_response(
        send: Callable,
        /,
        *,
        status_code: int,
        monitoring=None,  # type: MonitoringMiddleware | None
        headers: dict | None = None,
        body: bytes | None = None,
        exception: bool = False,
) -> None:
    if exception:
        body = json.dumps({'detail': status.status_text[status_code]})
    elif status_code == status.HTTP_204_NO_CONTENT or body == b'null':
        body = None

    await monitoring.after(status_code)

    await _http_response_start(send, headers=headers, status_code=status_code)
    await _http_response_body(send, body=body)


def import_class(dotted_path: str, /) -> type:
    """
    Example:
    -------
        Input: panther.db.models.User
        Output: User (The Class)
    """
    path, name = dotted_path.rsplit('.', 1)
    module = importlib.import_module(path)
    return getattr(module, name)


def read_multipart_form_data(boundary: str, body: bytes) -> dict:
    boundary = b'--' + boundary.encode()
    new_line = b'\r\n' if body[-2:] == b'\r\n' else b'\n'

    field_pattern = (
            rb'(Content-Disposition: form-data; name=")(.*)("'
            + 2 * new_line
            + b')(.*)'
    )
    file_pattern = (
            rb'(Content-Disposition: form-data; name=")(.*)("; filename=")(.*)("'
            + new_line
            + b'Content-Type: )(.*)'
    )

    data = {}
    for _row in body.split(boundary):
        row = _row.removeprefix(new_line).removesuffix(new_line)

        if row in (b'', b'--'):
            continue

        if match := re.match(pattern=field_pattern, string=row):
            _, field_name, _, value = match.groups()
            data[field_name.decode('utf-8')] = value.decode('utf-8')

        else:
            file_meta_data, value = row.split(2 * new_line, 1)

            if match := re.match(pattern=file_pattern, string=file_meta_data):
                _, field_name, _, file_name, _, content_type = match.groups()
                file = File(
                    file_name=file_name.decode('utf-8'),
                    content_type=content_type.decode('utf-8'),
                    file=value,
                )
                data[field_name.decode('utf-8')] = file
            else:
                logger.error('Unrecognized Pattern')

    return data


def generate_ws_connection_id() -> str:
    return uuid4().hex


def is_function_async(func: Callable) -> bool:
    """
    Sync result is 0 --> False
    async result is 128 --> True
    """
    return bool(func.__code__.co_flags & (1 << 7))


def clean_traceback_message(exception: Exception) -> str:
    """We are ignoring packages traceback message"""
    tb = TracebackException(type(exception), exception, exception.__traceback__)
    stack = tb.stack.copy()
    for t in stack:
        if t.filename.find('site-packages/panther') != -1:
            tb.stack.remove(t)
    _traceback = list(tb.format(chain=False))
    return exception if len(_traceback) == 1 else f'{exception}\n' + ''.join(_traceback)


def reformat_code(base_dir):
    try:
        subprocess.run(['ruff', 'format', base_dir])
        subprocess.run(['ruff', 'check', '--select', 'I', '--fix', base_dir])
    except FileNotFoundError:
        raise PantherException("No module named 'ruff', Hint: `pip install ruff`")


def check_function_type_endpoint(endpoint: types.FunctionType) -> Callable:
    # Function Doesn't Have @API Decorator
    if not hasattr(endpoint, '__wrapped__'):
        logger.critical(f'You may have forgotten to use @API() on the {endpoint.__name__}()')
        raise TypeError
    return endpoint


def check_class_type_endpoint(endpoint: Callable) -> Callable:
    from panther.app import GenericAPI

    if not issubclass(endpoint, GenericAPI):
        logger.critical(f'You may have forgotten to inherit from GenericAPI on the {endpoint.__name__}()')
        raise TypeError

    return endpoint.call_method
