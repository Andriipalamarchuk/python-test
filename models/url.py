from datetime import datetime
from typing import Annotated, Optional
import uuid
from pydantic import BaseModel, BeforeValidator, Field, constr

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

class UrlModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    original_url: str
    minified_url: str
    created_at: datetime = Field(default_factory=datetime.now)


    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class CreateUrlModel(BaseModel):
    url: str = Field(min_length=1)
    