import uvicorn
from fastapi import FastAPI
from routes import hello, tests, fixes

app = FastAPI()


@app.on_event("startup")
async def startup():
    app.include_router(hello.router)
    app.include_router(tests.router)
    app.include_router(fixes.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=4004, reload=True)
