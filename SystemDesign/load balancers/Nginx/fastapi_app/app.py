from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI(root_path="/airflow")
path_prefix = "/airflow"
@app.get("/")
def read_root(request: Request):
    return {"message": "Hello from FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int, request: Request):
    return {"item_id": item_id}


# Mount the static directory to serve CSS, JS, images, etc.
app.mount("/airflow/static", StaticFiles(directory="static"), name="static")

# Set up the templates directory for Jinja2 to load HTML files.
templates = Jinja2Templates(directory="templates")

@app.get("/ui", response_class=HTMLResponse)
async def read_index(request: Request):
    # Render and return index.html, passing the request for url_for to work in the template.
    return templates.TemplateResponse("index.html", {"request": request})