from dotenv import dotenv_values
from pymongo import ASCENDING, MongoClient

config = dotenv_values(".env")


def get_database():
    mongodb_client = MongoClient(config.get("MONGODB_CONNECTION_URI"))
    return mongodb_client[config.get("DB_NAME")]

def check_if_index_exists():
    db = get_database()
    index_names = [index['name'] for index in db["urls"].list_indexes()]
    if "created_at_ttl" not in index_names:
        url_validity = config.get("URL_VALIDITY_IN_MINUTES")
        db["urls"].create_index([("created_at", ASCENDING)], expireAfterSeconds=int(url_validity) * 60)