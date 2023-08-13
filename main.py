from GoogleTransTextDownload import translate_english_to_spanish
from typing import Union

from fastapi import FastAPI, Request, Form ,UploadFile ,File 

from starlette.templating import Jinja2Templates

templates=Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse('index.html',{"request": request })


@app.post("/")
def process_form(request: Request, user_input: str = Form(default=''), file_input: UploadFile = File(...)):
    user_input_value = user_input
    file_content = file_input.file.read().decode("utf-8")
    translated_result = translate_english_to_spanish(file_content)

    return templates.TemplateResponse('index.html', {"request": request, "user_input_value": user_input_value, "translated_result": translated_result})
