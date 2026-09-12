from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from src.core.config import get_settings

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

def verify_api_key(api_key: str = Security(api_key_header)):
    settings = get_settings()
    if api_key != settings.api_key_secret:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key"
        )
    return api_key
