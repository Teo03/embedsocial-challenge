from fastapi import FastAPI, Form
from starlette.responses import FileResponse 

app = FastAPI()

@app.get("/")
async def index():
    return FileResponse('index.html')

@app.post("/post_form")
async def post_form(orderByRatingHighest: bool = Form(),
                    orderByDateNewest: bool = Form(),
                    prioritizeByText: bool = Form(),
                    minimumRating: int = Form()):
    return (orderByRatingHighest, orderByDateNewest, prioritizeByText, minimumRating)