from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI(title="Multi-Modal AI Content Marketing Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3"


class CampaignRequest(BaseModel):
    brief: str
    tone: str = "professional"


def ask_ollama(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=180
        )
        data = response.json()
        return data.get("response", "No response from model.").strip()
    except requests.exceptions.ConnectionError:
        return "ERROR: Ollama is not running. Please start Ollama first."
    except Exception as e:
        return f"ERROR: {str(e)}"


@app.get("/")
def root():
    return {"message": "Content Marketing Engine is running!"}


@app.get("/health")
def health():
    try:
        requests.get("http://localhost:11434", timeout=5)
        return {"ollama": "running", "model": MODEL, "status": "ok"}
    except:
        return {"ollama": "NOT running", "model": MODEL, "status": "error"}


@app.post("/generate")
def generate_campaign(req: CampaignRequest):
    brief = req.brief.strip()
    tone = req.tone

    if not brief:
        return {"status": "error", "message": "Brief cannot be empty."}

    blog = ask_ollama(f"""You are a professional content writer.
Write a {tone} blog post for this campaign: "{brief}"
Structure: catchy headline, short intro, 2-3 body paragraphs, call-to-action.
Length: around 250 words.
Write only the blog post, no extra text.""")

    tweets = ask_ollama(f"""You are a social media expert.
Write exactly 3 tweet variants for this campaign: "{brief}"
Tone: {tone}
Rules: each tweet under 280 characters, include hashtags.
Separate each tweet with ---
Write only the 3 tweets, nothing else.""")

    instagram = ask_ollama(f"""You are an Instagram content creator.
Write an Instagram caption for this campaign: "{brief}"
Tone: {tone}
Include relevant emojis and end with 5 hashtags.
Write only the caption, nothing else.""")

    seo = ask_ollama(f"""You are an SEO expert.
Generate SEO metadata for this campaign: "{brief}"
Use exactly this format:
Title: (under 60 characters)
Meta Description: (under 155 characters)
Keywords: word1, word2, word3, word4, word5
Write only the metadata, nothing else.""")

    return {
        "status": "success",
        "brief": brief,
        "tone": tone,
        "blog": blog,
        "tweets": tweets,
        "instagram": instagram,
        "seo": seo
    }
@app.get("/image")
def generate_image(prompt: str, seed: int = 42):
    import urllib.parse
    encoded = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=800&height=600&seed={seed}&nologo=true"
    try:
        r = requests.get(url, timeout=60)
        if r.status_code == 200:
            from fastapi.responses import Response
            return Response(content=r.content, media_type="image/jpeg")
        else:
            return {"error": "Image generation failed"}
    except Exception as e:
        return {"error": str(e)}
@app.get("/image")
def generate_image(prompt: str, seed: int = 42):
    import urllib.parse
    encoded = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=800&height=600&seed={seed}&nologo=true"
    try:
        r = requests.get(url, timeout=60)
        if r.status_code == 200:
            from fastapi.responses import Response
            return Response(content=r.content, media_type="image/jpeg")
        else:
            return {"error": "Image generation failed"}
    except Exception as e:
        return {"error": str(e)}    