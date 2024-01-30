from pydantic import BaseModel, ConfigDict
from bson import ObjectId


class ImmutableMongoDbModel(BaseModel):
    model_config = ConfigDict(frozen=False, json_encoders={ObjectId: str})


class MutableMongoDbModel(BaseModel):
    model_config = ConfigDict(frozen=False, json_encoders={ObjectId: str})


class MutableJsonDbModel(BaseModel):
    model_config = ConfigDict(frozen=False, json_encoders={ObjectId: str})


class ImmutableJsonDbModel(BaseModel):
    model_config = ConfigDict(frozen=False, json_encoders={ObjectId: str})
