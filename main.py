from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class VibeRequest(BaseModel):
    vibe: str

movie_data = {
    "Adrenaline Rush": [
        {"title": "Mad Max: Fury Road", "year": 2015, "trailer": "https://youtu.be/hEJnMQG9ev8"},
        {"title": "John Wick", "year": 2014, "trailer": "https://youtu.be/2AUmvWm5ZDQ"}
    ],
    "Powerful Performances": [
        {"title": "Whiplash", "year": 2014, "trailer": "https://youtu.be/7d_jQycdQGo"},
        {"title": "The Whale", "year": 2022, "trailer": "https://youtu.be/nWiQodhMvz4"}
    ],
    "Creepy but Smart": [
        {"title": "Hereditary", "year": 2018, "trailer": "https://youtu.be/V6wWKNij_1M"},
        {"title": "Get Out", "year": 2017, "trailer": "https://youtu.be/DzfpyUB60YY"}
    ]
}

@app.post("/recommend")
def recommend_movies(request: VibeRequest):
    vibe = request.vibe
    return {"vibe": vibe, "recommendations": movie_data.get(vibe, [])}
