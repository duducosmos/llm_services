from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import debugpy
from typing import List


app = FastAPI()
# Allow all origins for CORS (you can customize this based on your requirements)
origins = ["*"]

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
debugpy.listen(("0.0.0.0", 5678))


@app.get("/")
async def read_root():
    return {"body": "teste"}
