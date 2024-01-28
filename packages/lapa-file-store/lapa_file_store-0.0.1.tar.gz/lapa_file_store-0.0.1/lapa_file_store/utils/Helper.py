import os.path

from lapa_database_helper.main import LAPADatabaseHelper

from lapa_file_store.configuration import config_str_oss_folder_path


def create_entry_in_file_store(file_name_with_extention: str, file_extention: str, curr_timestamp, generated_uuid: str):
    try:
        lobj_lapa_database_helper = LAPADatabaseHelper()

        database_name = "file_storage"
        schema_name = "public"
        table_name = "file"

        data = [{
            "file_name_with_extension": file_name_with_extention,
            "file_extension": file_extention,
            "file_date_created": curr_timestamp,
            "file_last_modified": curr_timestamp,
            "file_system_file_name_with_extension": "",
            "file_system_relative_path": "/" + file_name_with_extention,
            "file_storage_token": str(generated_uuid),
            "file_purpose": "",
            "file_is_deleted": False,
            "file_date_deleted": curr_timestamp
        }]

        response = lobj_lapa_database_helper.insert_rows(data, database_name, schema_name, table_name)

        return response
    except Exception as e:
        raise e


def download_file(file_storage_token):
    try:
        lobj_lapa_database_helper = LAPADatabaseHelper()

        database_name = "file_storage"
        schema_name = "public"
        table_name = "file"

        filters = {"file_storage_token": file_storage_token}

        response = lobj_lapa_database_helper.get_rows(filters, database_name, schema_name, table_name)

        file_id = str(response[0]["file_id"])
        file_relative_path = response[0]['file_name_with_extension']
        filepath = os.path.join(config_str_oss_folder_path, file_id, file_relative_path)

        return filepath

    except Exception as e:
        raise e
