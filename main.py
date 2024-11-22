from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')






from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "E-Library Backend is running!"}