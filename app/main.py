from fastapi import FastAPI

from app.routers import books


# Khoi tao ung dung FastAPI
app = FastAPI(

    title="Library API – Khoa CNTT",

    version="1.0.0",

    description="API quản lý sách của Thư viện số Khoa CNTT"

)


# Dang ky router quan ly sach
app.include_router(books.router)


# API kiem tra server
@app.get(
    "/health",
    tags=["System"]
)
def health():

    return {
        "status": "ok"
    }