from fastapi import FastAPI
from mockData import products
app = FastAPI()

@app.get("/")
def home():
    return "welcome to fastapi series."

@app.get("/products")
def get_products():
    return products