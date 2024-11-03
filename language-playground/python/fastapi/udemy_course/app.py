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

@app.get("/books/{book_title}")
async def read_book(book_title):
    for each in BOOKS:
        if each.get("title").casefold() == book_title.casefold():
            return each
    return {"message": "Book not found"}

@app.get("/books/")
async def read_books_by_category(category: str):
    books_to_return = []
    for each in BOOKS:
        if each.get('category').casefold() == category.casefold():
            books_to_return.append(each)
    return books_to_return

@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for each in BOOKS:
        if each.get('author').casefold() == author.casefold():
            books_to_return.append(each)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_books_by_author_query(book_author: str):
    books_to_return = []
    for each in BOOKS:
        if each.get('author').casefold() == book_author.casefold():
            books_to_return.append(each)
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            del BOOKS[i]
            break