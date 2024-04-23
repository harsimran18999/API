from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

app = FastAPI()

# Your API documentation goes here
# Documentation for User data models
class User(BaseModel):
    """
    User data model.

    Represents a user in the system.
    """
    username: str
    email: str
    hashed_password: str

class Token(BaseModel):
    """
    Token data model.

    Represents an access token used for authentication.
    """
    access_token: str
    token_type: str