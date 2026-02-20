from random import randrange
from typing import Optional
from fastapi import FastAPI,HTTPException, status
from pydantic import BaseModel
from fastapi.params import Body

app = FastAPI()



class Post(BaseModel):
    title:str    
    content:str
    published: bool = True
    rating: Optional[int] = None

""" 
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get('/')
def read_root():
    return{"Hello" : "World"}


@app.get("/items/{item_id}")
def read_item(item_id:int, q:str | None = None):
    return{"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
    return{"item_id": item.name, "item_id":item.price,  "item_id":item_id}


"""

my_posts = [
    {
        "title": "title of post 1",
        "content": "content of post 1",
        "id": 1
    },
    {
        "title": "Favorite foods",
        "content": "I like pizza and pasta",
        "id": 2
    },
    {
      "title": "Favorite game",
      "content": "I like puzzles and COD",
      "published": True,
      "rating": 3,
      "id": 203906
    }
]



@app.get("/posts")
def get_post():
    return{"data": my_posts}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return{"data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int):
    for post in my_posts:
        if post['id'] == id:
            return{"post_details": post}
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail= f"Post with id: {id} not found"
        )



















































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
