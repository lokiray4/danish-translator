from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import whisper
from deep_translator import GoogleTranslator
import tempfile

app = FastAPI()

# 允许网页访问API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Loading Whisper...")

model = whisper.load_model("small")

print("Whisper Loaded")


@app.post("/translate")
async def translate(file: UploadFile):

    with tempfile.NamedTemporaryFile(delete=False) as temp:

        temp.write(
            await file.read()
        )

        path = temp.name

    result = model.transcribe(
        path,
        language="da"
    )

    danish=result["text"]

    chinese=GoogleTranslator(
        source='da',
        target='zh-CN'
    ).translate(
        danish
    )

    return {
        "danish":danish,
        "translation":chinese
    }
