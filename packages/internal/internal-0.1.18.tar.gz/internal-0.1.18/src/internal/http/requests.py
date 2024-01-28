import httpx

from src.internal.base_config import get_app_config


async def async_request(method, url, **kwargs):
    timeout = httpx.Timeout(connect=get_app_config().REQUEST_CONN_TIMEOUT, read=get_app_config().REQUEST_READ_TIMEOUT,
                            write=get_app_config().REQUEST_WRITE_TIMEOUT, pool=get_app_config().REQUEST_POOL_TIMEOUT)

    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.request(method, url, **kwargs)
        return response
