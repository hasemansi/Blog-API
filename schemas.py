from pydantic import BaseModel, ConfigDict
from datetime import datetime

class BlogCreate(BaseModel):
    title:str
    content:str
    author:str

class BlogUpdate(BaseModel):
    title:str
    content:str
    author:str

class BlogResponse(BaseModel):
    id:int
    title:str
    content:str
    author:str
    created_at:datetime

    model_config = ConfigDict(from_attributes=True)