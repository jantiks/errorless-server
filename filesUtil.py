import zipfile
import glob
import shutil
import os
from fastapi import UploadFile

def find_file_in_zip(zip_file, file_extension):
    for f in glob.glob(f'./{zip_file}/**/*.{file_extension}', recursive=True):
        print(f)
        return f
    print("No For Loop")
    return None

def move_folder(src_folder, dst_folder):
    if os.path.exists(dst_folder):
        shutil.rmtree(dst_folder)
    shutil.move(src_folder, dst_folder)

async def processDSYM(file: UploadFile):
    with open(file.filename, "wb") as f:
        f.write(await file.read())

    folderName = "directory"
    with zipfile.ZipFile(file.filename, "r") as zip_ref:
        zip_ref.extractall(folderName)
    dSYM = find_file_in_zip(folderName, "dSYM")
    move_folder(dSYM, "./debug.dSYM")

    os.remove(f"./{file.filename}")
    os.remove(f"./{folderName}")

