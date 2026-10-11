from pydantic import BaseModel, Field


class ParseRequest(BaseModel):
    message: str = Field(min_length=1)


class ParsedItem(BaseModel):
    product_id: str | None = None

    product_name: str = Field(min_length=1)

    quantity: int | None = Field(
        default=None,
        gt=0
    )

    requested_discount_percent: float | None = Field(
        default=None,
        ge=0,
        le=100
    )


class ParseResponse(BaseModel):
    items: list[ParsedItem] = Field(default_factory=list)
    needs_review: bool = False


class AiRequest(BaseModel):
    message: str = Field(min_length=1)


class AiResponse(BaseModel):
    items: list[ParsedItem]
    requires_review: bool