from fastapi import FastAPI

app = FastAPI()

#this function is for home root (ex:https:amazon.com/home)
@app.get("/")
def home():
    return "Welcome to fast api series"

#this function is for contact root (ex:https:amazon.com/contact)
@app.get("/contact")
def contact():
    return "You can contact us at any time."