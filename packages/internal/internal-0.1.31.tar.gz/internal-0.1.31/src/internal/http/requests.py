import httpx

from fastapi import FastAPI


async def async_request(app: FastAPI, method, url, **kwargs):
    timeout = httpx.Timeout(connect=app.state.config.REQUEST_CONN_TIMEOUT, read=app.state.config.REQUEST_READ_TIMEOUT,
                            write=app.state.config.REQUEST_WRITE_TIMEOUT, pool=app.state.config.REQUEST_POOL_TIMEOUT)

    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.request(method, url, **kwargs)
        return response
