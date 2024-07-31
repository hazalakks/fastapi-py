from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param: str):  #str is optional
    return{"dynamic_param" : dynamic_param}

#http://127.0.0.1:8000/books/science  dynamic_param : science
#http://127.0.0.1:8000/books/author%20one  dynamic_param : author one


@app.get("/books/{book_title}")   #{dynamic_parameter}
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

#http://127.0.0.1:8000/books/?category=science


@app.get("/books/{book_author}/") 
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
#we'll get book_author from the url as a path param
#category will be otomaticly query param

#path parameters to find location, part of the url, attached after a /
#query parameters filter the data you wanna return, attached after a ?

#get cannot have a body

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
"""
{
    "title": "Title Seven",
    "author": "Author Two",
    "category": "math"
  }
"""

@app.put("/books/update_book") #has body
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
##Assignment##
#1. Create a new endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.
#path param version
@app.get("/books/byauthor/{author}")
async def read_books_by_author_path(author: str):
    book_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            book_to_return.append(book)
    return book_to_return
#http://127.0.0.1:8000/books/byauthor/author%20one

#query param version 
"""@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return"""
#gives an error 422 Unprocessable Entity bsz of line 44 so we need to move before the line 44
#because expects a category param too

#http://127.0.0.1:8000/books/byauthor/?author=author%20one
#author(query)
