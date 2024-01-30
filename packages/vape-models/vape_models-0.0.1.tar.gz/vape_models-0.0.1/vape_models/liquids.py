from pydantic import BaseModel, Field


class BaseLiquidSchema(BaseModel):
    id: int = Field(..., description="")
    title: int = Field(..., description="")
    flavour: int = Field(..., description="")
    mg: int = Field(..., description="")
