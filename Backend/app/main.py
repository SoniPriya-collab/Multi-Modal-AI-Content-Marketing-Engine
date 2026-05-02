from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.text_generator import (
    generate_blog,
    generate_tweets,
    generate_image
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():

    return {

        "message": "AI Content Generator API Running"

    }

@app.get("/generate/{topic}")
def generate(topic: str):

    blog = generate_blog(topic)

    tweets = generate_tweets(topic)

    image = generate_image(topic)

    return {

    "blog": blog,

    "tweets": tweets,

    "image": image,

    "seo_tags": [

        topic,

        f"{topic} trends",

        f"{topic} marketing",

        f"{topic} future",

        f"{topic} technology"

    ]

}