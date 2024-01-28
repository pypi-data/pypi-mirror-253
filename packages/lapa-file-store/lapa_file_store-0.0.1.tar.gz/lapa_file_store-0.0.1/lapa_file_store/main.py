import mimetypes
import os
import uuid
from datetime import datetime, timezone

from fastapi import FastAPI, status, UploadFile
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from square_logger.main import SquareLogger
from uvicorn import run

from lapa_file_store.configuration import (
    config_int_host_port,
    config_str_host_ip,
    config_str_log_file_name,
    config_str_oss_folder_path
)
from lapa_file_store.utils.Helper import create_entry_in_file_store, download_file

local_object_square_logger = SquareLogger(config_str_log_file_name)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload_file", status_code=status.HTTP_201_CREATED)
@local_object_square_logger.async_auto_logger
async def upload_file(file: UploadFile):
    try:
        file_bytes = await file.read()
        filename = file.filename
        content_type = file.content_type

        current_time_utc = str(datetime.now(timezone.utc))

        generated_uuid = uuid.uuid4()

        response = create_entry_in_file_store(filename, content_type, current_time_utc, generated_uuid)

        file_id = response[0]["file_id"]

        # create folder
        folder_path = os.path.join(config_str_oss_folder_path, str(file_id))
        os.makedirs(folder_path)
        filepath = os.path.join(config_str_oss_folder_path, str(file_id), filename)
        with open(filepath, 'wb') as file:
            file.write(file_bytes)

        # Check if the file exists
        if os.path.exists(filepath):
            # Create FileResponse
            # file_response = FileResponse(filepath, media_type=content_type, filename=filename)

            # Additional information you want to include
            additional_info = {"FileStorageToken": response[0]["file_storage_token"]}

            # Return JSONResponse with file response and additional information
            return JSONResponse(content={"additional_info": additional_info})

        else:
            # Handle the case when the file does not exist
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.post("/downlaod_file", status_code=status.HTTP_201_CREATED)
@local_object_square_logger.async_auto_logger
async def downlaod_file(file_storage_token: str):
    try:

        file_path = download_file(file_storage_token)

        # Get content type
        content_type, encoding = mimetypes.guess_type(file_path)

        # Get filename
        filename = os.path.basename(file_path)

        if file_path:
            return FileResponse(file_path, media_type=content_type, filename=filename)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


if __name__ == "__main__":
    try:
        run(app, host=config_str_host_ip, port=config_int_host_port)
    except Exception as exc:
        local_object_square_logger.logger.critical(exc, exc_info=True)
