import json

from fastapi import status
from fastapi.responses import JSONResponse
from beanie import Document, PydanticObjectId


async def async_response(data=None, message=None, code=None, page_no=None, total_num=None, page_size=None,
                          status_code=status.HTTP_200_OK):
    def _serialize(data):
        if issubclass(type(data), Document):
            data = json.loads(data.model_dump_json())
        return data

    ret = {}
    if isinstance(data, list):
        data = [_serialize(d) for d in data]
    else:
        data = _serialize(data)

    ret['code'] = code or "ok"

    ret['message'] = message or "success"

    if page_no and total_num and page_size:
        ret['data'] = {
            'page_no': page_no,
            'total_num': total_num,
            'page_size': page_size,
            'page_data': data
        }
    else:
        ret['data'] = data

    return JSONResponse(status_code=status_code, content=ret)
