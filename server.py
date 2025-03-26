from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Defina o diretório de uploads
UPLOAD_DIR = "uploads"

# Certifique-se de que a pasta "uploads" existe
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/download/{filename}")
async def download_file(filename: str):
    """Endpoint para baixar arquivos da pasta uploads"""
    filename.replace("%", " ")
    print("Download filename: ", filename)

    file_path = os.path.join(UPLOAD_DIR, filename)

    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/octet-stream", filename=filename)
    return {"error": "Arquivo não encontrado"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0")    #, port=5000)