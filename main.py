from fastapi import FastAPI, UploadFile, Request, Body
import filesUtil

from pydantic import BaseModel

class DumpModel(BaseModel):
    body: str

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.post("/upload")
async def upload(file: UploadFile):
    await filesUtil.processDSYM(file)
    return {"message": "dSYM file extracted and saved successfully"}

@app.post("/crash")
async def crash(file: UploadFile):
    print(await file.read())
    return {"message": "Bye"}

@app.post("/dump")
def dumpInfo(info: DumpModel):
    print(info.body)
    return info.body