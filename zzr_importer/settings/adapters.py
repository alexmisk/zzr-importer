from typing import Optional, Union

from pydantic import BaseModel, HttpUrl, validator


class RESTAdapterSettings(BaseModel):
    client_id: Optional[str]
    client_secret: Optional[str]
    refresh_token: Optional[str]
    base_url: Optional[HttpUrl]
    token_url: Optional[HttpUrl]
    authorization_url: Optional[HttpUrl]

    @validator("client_id", pre=True, always=True)
    def default_client_id(cls, v: Optional[str]) -> Union[str, None]:
        return v or None

    @validator("client_secret", pre=True, always=True)
    def default_client_secret(cls, v: Optional[str]) -> Union[str, None]:
        return v or None

    @validator("refresh_token", pre=True, always=True)
    def default_refresh_token(cls, v: Optional[str]) -> Union[str, None]:
        return v or None

    @validator("base_url", pre=True, always=True)
    def default_base_url(cls, v: Optional[HttpUrl]) -> Union[str, None]:
        return v or None

    @validator("token_url", pre=True, always=True)
    def default_token_url(cls, v: Optional[HttpUrl]) -> Union[str, None]:
        return v or None

    @validator("authorization_url", pre=True, always=True)
    def default_authorization_url(cls, v: Optional[HttpUrl]) -> Union[str, None]:
        return v or None
