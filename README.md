# OpenAPIProject

Firstly, to run server you must write "uvicorn main:app --reload" because we define our name of API **app**. That's why we will use **main:app**.
Secondly, most probably if there is no another server runs, this program will be run in **localhost:8000**. So when you entered **localhost:8000* url side on your browser, you can observe your API.

And the other files **CEZAEREN9-testAPI-0.1.0-resolved.json** and **CEZAEREN9-testAPI-0.1.0-resolved.yaml**, these are OpenAPI docs about project.

- With **get_books()** function, you can see all of books in data list.
- With **get_book()** function, you can see specific book by book ID.
- With **add_book()** function, you can add new book item.
- With **update_book()** function, you can update old book data.
- With **delete_book()** function, you can delete any book item if exist.
