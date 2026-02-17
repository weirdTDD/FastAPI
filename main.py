from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

class Book(BaseModel):
    title:str    
    author:str
    publication_year:int


@app.get('/')
def read_root():
    return{"Hello" : "World"}


@app.get("/items/{item_id}")
def read_item(item_id:int, q:str | None = None):
    return{"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
    return{"item_id": item.name, "item_id":item.price,  "item_id":item_id}



@app.get("/posts")
def get_post():
    return{"data":"This is your post"}


@app.post('/createposts')
def create_post(payload: dict = Body(...)):
    print(payload)
    return{"new_post" : f" title: {payload['title']}, content: {payload['content']}"}



@app.post("/booker")
def post_book(book1: dict = Body(...)):
    print(book1)
    return{"new_book": f"{book1}"}


#Valid usage
"""
book1=Book(
    title="The Hitchhiker's Guide to the the Galaxy",
    author="Abieku Adams",
    publication_year=1979
)
print(book1)

title: {book1['title']}, author: {book1['author']}, publication_year: {book1['publication_year']}
"""
