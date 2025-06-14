from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from dbConnection.builder import Builder  # Adjust import if your path differs


@dataclass
class DatabaseConfiguration:
    database_url: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    max_connections: Optional[int] = None
    enable_cache: Optional[bool] = None
    is_read_only: Optional[bool] = None

    @staticmethod
    def builder() -> DatabaseBuilder:
        return DatabaseConfiguration.DatabaseBuilder()

    class DatabaseBuilder(Builder["DatabaseConfiguration"]):
        def __init__(self):
            # Initialize with all fields as None
            self._instance = DatabaseConfiguration()

        def build(self) -> DatabaseConfiguration:
            return self._instance
