from fastapi import FastAPI, Form
from starlette.responses import FileResponse

from utils import load_reviews, sort_reviews, filter_reviews

app = FastAPI()

@app.get("/")
async def index():
    return FileResponse('index.html')

@app.post("/post_form")
async def post_form(
        orderByRatingHighest: bool = Form(),
        orderByDateNewest: bool = Form(),
        prioritizeByText: bool = Form(),
        minimumRating: int = Form()
    ):

    """
    Returns a json file with the reviews that match the parameters
    """
    raw_reviews, reviews = load_reviews()
    reviews_ids = [review['id'] for review in raw_reviews]
    result = []

    # filter reviews
    reviews = sort_reviews(reviews, prioritizeByText, orderByDateNewest, orderByRatingHighest)
    filtered_ids = filter_reviews(reviews, minimumRating)

    # find the reviews that match the filtered ids
    for id in filtered_ids:
        if id in reviews_ids:
            result.append(raw_reviews[reviews_ids.index(id)])

    return result