import uvicorn
from polychroma.settings import PORT


if __name__ == "__main__":
    uvicorn.run("polychroma.asgi:application", port=PORT, log_level="info")