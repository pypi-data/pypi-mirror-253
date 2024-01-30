from pydantic import BaseModel, Field


class BaseCompanySchema(BaseModel):
    id: int = Field(..., description="")
    title: str = Field(..., description="")
