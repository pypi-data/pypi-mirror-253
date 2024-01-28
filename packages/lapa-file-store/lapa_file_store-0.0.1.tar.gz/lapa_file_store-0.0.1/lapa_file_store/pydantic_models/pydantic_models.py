from fastapi import UploadFile
from pydantic import BaseModel


class UploadObject(BaseModel):
    File: UploadFile

# class GetFile(BaseModel):
#     ContextKey: database_structure_main_file.DatabasesEnum
