from pydantic import BaseModel, Field


class BaseCommentImageSchema(BaseModel):
    comment_id: int = Field(..., description="")
    image_id: int = Field(..., description="")
    url: str = Field(..., description="")


class BaseCommentBodySchema(BaseModel):
    text: str = Field(..., description="")
    images: list[BaseCommentImageSchema] = Field(description="")
    rate: float = Field(description="")


class BaseCommentSchema(BaseCommentBodySchema):
    id: int = Field(..., description="")
