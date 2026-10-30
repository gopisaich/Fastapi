from fastapi import FastAPI
from mockData import products
app = FastAPI()

@app.get("/")
def home():
    return "welcome to fastapi series."

@app.get("/products")
def get_products():
    return products

#path parameters

@app.get("/product/{product_id}")

## if product available with the id, return product, else return  error message.
def get_oneproduct(product_id:int):
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct
    return{
        "Error":"Product not found for parameter."
    }

## query parameters

@app.get("/greet")
def greet_user(name:str, age:int):
    return {
        "greet":f"Hello {name}, Your age is {age}"
    }
 #for output(http://127.0.0.1:8000/greet?name=gopi&age=21)