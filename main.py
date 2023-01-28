from fastapi import FastAPI, UploadFile, Request, Body
import filesUtil
import models

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
    with open(file.filename, "wb") as f:
        f.write(await file.read())
        
    symbolicate_crash()
    return {"message": "Bye"}

@app.post("/dump")
def dumpInfo(info: models.DumpModel):
    print(info.body)
    return info.body

import subprocess

def symbolicate_crash():
    developer_dir = subprocess.run(['xcode-select', '--print-path'], stdout=subprocess.PIPE).stdout.decode().strip()

    # Set the DEVELOPER_DIR environment variable
    output = subprocess.run(['export', 'DEVELOPER_DIR=' + f'"{developer_dir}"'], shell=True)
    print(output)
    output = subprocess.run(['/Users/tigran/Desktop/errorless-server/symbolicatecrash', "-v", '/Users/tigran/Desktop/errorless-server/app.crash', '/Users/tigran/Desktop/errorless-server/debug.dSYM', '>', '/Users/tigran/Desktop/errorless-server/output.crash'])
    print(output)