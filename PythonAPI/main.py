from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
data = [{"id": 1,
         "title": "The First Book",
         "Author": "Unknown",
         "Publisher": "Unknown"}]

class Book(BaseModel):
   id: int
   title: str
   author: str
   publisher: str

@app.get("/list")
async def get_books():
   return data

@app.get("/book/{id}")
async def get_book(id: int):
   id = id - 1
   return data[id]

@app.post("/book")
async def add_book(book: Book):
   data.append(book.dict())
   return data

@app.put("/book/{id}")
async def add_book(id: int, book: Book):
   data[id-1] = book
   return data

@app.delete("/book/{id}")
async def delete_book(id: int):
   data.pop(id-1)
   return data