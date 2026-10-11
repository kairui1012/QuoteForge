from fastapi import FastAPI
from app.schemas.quotation import ParseRequest, ParseResponse, ParsedItem

app = FastAPI(
    title="QuoteForge AI Service",
    version="1.0.0"
)


@app.post("/api/parse", response_model=ParseResponse)
def parse_message(request: ParseRequest):

    item = ParsedItem(
        product_id="100",
        product_name="laptop",
        quantity=5,
        requested_discount_percent=15
    )

    return ParseResponse(
        items=[item],
        needs_review=False
    )

