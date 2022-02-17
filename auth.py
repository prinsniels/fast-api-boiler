import secrets
from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from config import Config, config

api_key = APIKeyHeader(name="X-API-KEY", auto_error=False)

def authenticate_request(header: Optional[str] = Depends(api_key), config: Config = Depends(config)) -> bool:
    if header is None:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="No API key provided.", headers={})
    if not secrets.compare_digest(header, str(config.API_KEY)):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Authentication required.", headers={})
    return True
