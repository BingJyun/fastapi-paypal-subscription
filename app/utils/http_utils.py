import requests
import logging
from fastapi import HTTPException

logger = logging.getLogger(__name__)

def make_request(
        method: str,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        auth: tuple | None = None,
        token: str | None = None
) -> dict:
    headers = headers or {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            data=data,
            json=json,
            auth=auth
        )
        response.raise_for_status()
        if response.status_code == 204:
            return {}
        response_json = response.json()
        if not isinstance(response_json, (dict, list)):
            logger.error("Invalid response format")
            raise HTTPException(status_code=500, detail="Invalid response format")
        return response_json
    except requests.exceptions.HTTPError as http_err:
        status_code = getattr(response, "status_code", 500)
        logger.error(f"Request failed with status code {status_code}: {str(http_err)}")
        raise HTTPException(status_code=status_code, detail=f"Request failed: {str(http_err)}")
    except ValueError:
        logger.error("Invalid JSON response")
        raise HTTPException(status_code=500, detail="Invalid JSON response")
    except Exception as general_err:
        logger.error(f"Unexpected error: {str(general_err)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(general_err)}")