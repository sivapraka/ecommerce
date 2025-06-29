from .database import Database
from .database_type import DatabaseType


class MySQLDBDatabase(Database):
    def supports_type(self) -> str:
        return DatabaseType.MYSQL.value

class PostgreSQLDatabase(Database):
    def supports_type(self) -> str:
        return DatabaseType.POSTGRESQL.value

class MongoDBDatabase(Database):
    def supports_type(self) -> str:
        return DatabaseType.MONGODB.value