from .comon_database import *
from .database_type import DatabaseType


class DatabaseFactory:

    def get_database(self, database_type: DatabaseType):
        if database_type == DatabaseType.MYSQL:
            return MySQLDBDatabase()
        elif database_type == DatabaseType.MONGODB:
            return MongoDBDatabase()
        elif database_type == DatabaseType.POSTGRESQL:
            return PostgreSQLDatabase()
        else:
            raise ValueError("Database type not supported : " + str(database_type))
