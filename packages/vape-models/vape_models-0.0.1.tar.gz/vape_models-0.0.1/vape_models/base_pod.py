from enum import Enum

from pydantic import BaseModel, Field


class FormatEnum(str, Enum):
    pass


class ConnectorEnum(str, Enum):
    type_c = "type-c"
    micro_usb = "micro-usb"


class BasePodSchema(BaseModel):
    id: int = Field(..., description="")
    title: str = Field(..., description="")
    is_prefilled: bool = Field(description="")
    thickness: int = Field(description="")
    length: int = Field(description="")
    width: int = Field(description="")
    power: int = Field(description="")
    battery: int = Field(description="")
    is_auto: bool = Field(description="")
    material_id: int = Field(description="")
    format: FormatEnum = Field(description="")
    has_screen: bool = Field(description="")
    power_regulation: bool = Field(description="")
    mass: int = Field(description="")
    connector: ConnectorEnum = Field(description="")
    use_cartridge: bool = Field(description="")
    use_vaporizer: bool = Field(description="")
    price: int = Field(description="")
    extractable_battery: bool = Field(description="")
    is_ancet: bool = Field(..., description="")
    short_description: str = Field(..., description="")
    description: str = Field(..., description="")


class BasePodAncetSchema(BaseModel):
    id: int = Field(..., description="")
    title: str = Field(..., description="")
    price: int = Field(..., description="")

    image_url: str = Field(..., description="")
    rating: float = Field(..., description="")
