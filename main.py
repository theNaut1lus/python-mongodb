from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as book_router

config = dotenv_values(".env")


def startup_b_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")


def shutdown_db_client():
    app.mongodb_client.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup events
    startup_b_client()
    yield
    # shutdown events
    shutdown_db_client()


app = FastAPI(lifespan=lifespan)

app.include_router(book_router, tags={"books"}, prefix="/book")
