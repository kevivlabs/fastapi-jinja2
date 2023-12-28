
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

DOGS= [{"name": "Milo", "type": "Chihuahua"}, {"name": "Bella", "type": "Poodle"}]


@app.get("/")
async def name(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "name":"TomHanks","dogs":DOGS} )

