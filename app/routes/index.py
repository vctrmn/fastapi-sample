import socket
from fastapi import APIRouter, Response
from pydantic import BaseModel

router = APIRouter()

class HostnameResponse(BaseModel):
    hostname: str

@router.get("/", status_code=204)
async def default():
    return Response(status_code=204)

@router.get("/hostname", response_model=HostnameResponse)
async def hostname():
    return {"hostname": socket.gethostname()}
