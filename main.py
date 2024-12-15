from fastapi import FastAPI

app = FastAPI()


@app.get("/items")
def read_items():
    result = 1 + 1
    return {"result": result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
