import queue
import sqlite3
import threading
from typing import Optional

from ecommerce.connection.ConnectionPool import ConnectionPool
from ecommerce.connection.DatabaseConnection import DatabaseConnection


class ConnectionPoolImpl(ConnectionPool):
    _instance: Optional["ConnectionPool"] =  None
    _lock = threading.Lock()

    def __init__(self, db_path: str, pool_size: int = 5):
        self.db_path = db_path
        self.pool_size = pool_size
        self.connections = queue.Queue(maxsize=pool_size)

        for _ in range(pool_size):
            self.connections.put(self._create_connection())

    @staticmethod
    def get_instance(db_path: str = "database.db", pool_size: int = 5) -> ConnectionPool:
        with ConnectionPoolImpl._lock:
            if ConnectionPoolImpl._instance is None:
                ConnectionPoolImpl._instance = ConnectionPoolImpl(db_path, pool_size)
            return ConnectionPoolImpl._instance

    @staticmethod
    def reset_instance() -> None:
        with ConnectionPoolImpl._lock:
            if ConnectionPoolImpl._instance:
                ConnectionPoolImpl._instance.close_all_connections()
            ConnectionPoolImpl._instance = None

    def initialize_pool(self) -> None:
        return sqlite3.connect(self.db_path)

    def get_connection(self) -> Optional[DatabaseConnection]:
        if not self.connections.empty():
            return self.connections.get()
        return None

    def release_connection(self, connection: DatabaseConnection) -> None:
        self.connections.put(connection)

    def get_available_connections_count(self) -> int:
        return self.connections.qsize()

    def get_total_connections_count(self) -> int:
        return self.pool_size
