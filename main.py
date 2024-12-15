from fastapi import FastAPI

app = FastAPI()


@app.get("/items")
def read_items():
    some_var = 1
    result = 1 + some_var
    return {"result": result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
