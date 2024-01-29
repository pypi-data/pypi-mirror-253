# lapa_file_store

## about

file storage layer for my personal server.

## installation

> pip install lapa_file_store

## configs

1. lapa_file_store\data\config.ini
2. square_logger\data\config.ini

## env

- python>=3.12.0

## changelog

### v0.0.2

- change default port to 10100.
- change default LOCAL_STORAGE_PATH to be relative and LOCAL_STORAGE_PATH.
- move logger to configuration.py.
- fix dependencies in setup.py.
- minor optimisations.
- add validation for LOCAL_STORAGE_PATH in config.ini.
- fix logic for upload_file.
- fix logic for download_file.

### v0.0.1

- Base version
