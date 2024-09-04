from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os
from pydantic import BaseModel

app = FastAPI()

# Montar la carpeta 'static' para servir el archivo index.js
app.mount("/static", StaticFiles(directory="app/static"), name="static")

class Content(BaseModel):
    content: str

@app.get("/", response_class=HTMLResponse)
async def get_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Utilitarios</title>
    </head>
    <body>
        <h1 style="text-align:center;">Utilitarios</h1>
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <textarea id="input-text" style="width: 45%; height: 300px;"></textarea>
            <textarea id="output-text" style="width: 45%; height: 300px;" readonly></textarea>
        </div>
        <div style="text-align:center; margin-top: 20px;">
            <button onclick="limpiar()">Formatear</button>
            <button onclick="convertir()">Convertir</button>
            <button id="copy-btn" onclick="copiar()">Copy</button>
            <button id="clear-btn" onclick="clear_campos()">Limpiar</button>
        </div>
        <footer>
            Desarrollado por: <a href="https://github.com/LucasVega777">Lucas Vega</a>
        </footer>
        <script src="/static/index.js"></script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

def limpiar(content: str) -> str:
    result = []
    try:
        for line in content.splitlines():
            line = line.split('#')[0].strip()  
            if line: 
                line = line.replace('"', '') 
                result.append(line)
    except Exception as e:
        return 'No pude formatear tu texto :c'         
    return '\n'.join(result)

@app.post("/api/v1.0.0/limpiar_env")
async def limpiar_env(data: Content):
    cleaned_content = limpiar(data.content)
    return JSONResponse(content={"result": cleaned_content})


def convertir(content: str) -> str:
    result = []
    try:
        for line in content.split('\n- '):
            if line.strip():
                parts = line.split(":")
                name = parts[1].split('value')[0].strip()
                value = parts[2].strip().strip('"')
                result.append(f"{name}={value}")
    except Exception as e:
        return 'No pude convertir tu texto a variables de entorno :c'
    return '\n'.join(result)

@app.post("/api/v1.0.0/convertir_env")
async def convertir_env(data: Content):
    converted_content = convertir(data.content)
    return JSONResponse(content={"result": converted_content})