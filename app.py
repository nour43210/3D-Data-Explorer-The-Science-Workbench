from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.post("/generate-3d")
async def generate_3d(prompt: str):
    subprocess.run(f"python scripts/text2mesh.py --prompt '{prompt}' --output_dir ./output", shell=True)
    return {"status": "3D model generated!"}