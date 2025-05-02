# ruff: noqa: E402
import sys
from pathlib import Path

from fastapi import FastAPI
import uvicorn

sys.path.append(str(Path(__file__).parent.parent))


from src.api.messages import router as router_messages


app = FastAPI()

app.include_router(router_messages)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)