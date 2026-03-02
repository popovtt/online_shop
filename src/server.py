import uvicorn

from src.service import AppService

app = AppService()

if __name__ == "__main__":
    uvicorn.run("src.server:app")