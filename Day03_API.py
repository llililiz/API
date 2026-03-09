from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/employees")
def get_employees(name):
    return {f"{name}님, 환영합니다!"}

# 이거 뭐야