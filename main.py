import io
import qrcode

from fastapi import FastAPI
from starlette.responses import StreamingResponse

app = FastAPI()

@app.get("/generate/{message}")
def generate(message: str):
    img = qrcode.make(message)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/jpeg")

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
