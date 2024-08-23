from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")


def get_db():
    try:
        mongodb_client = MongoClient(config["MONGO_ATLAS_URI"], tls=True, tlsAllowInvalidCertificates=True)
        print(f'\n\nServer Info: {mongodb_client.server_info()}\n\n')

        db = mongodb_client[config['MONGO_DB_NAME']]
        print(f'Successfully connected to the database:{db}')
        return db
    except Exception:
        print(f'Failed to connect to the database:{db}')
        raise
