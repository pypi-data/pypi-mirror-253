from pydantic import BaseModel, Field


class BaseVaporizerSchema(BaseModel):
    id: int = Field(..., description="")
    volume: int = Field(..., description="")
    weight: int = Field(..., description="")
    resistance: int = Field(..., description="")
