from dataclasses import dataclass

from psycopg2 import connect


@dataclass(frozen=True)
class PGConfig:
    host: str = "localhost"
    port: int = 5433
    database: str = "postgres"
    schema: str = "public"
    user: str = "postgres"
    password: str = "letmein"


class PGConnection:
    def __init__(self, config: PGConfig) -> None:
        self._config = config
        self._connection = None

    @property
    def connection(self):
        if self._connection is None:
            self._connection = connect(
                host=self._config.host,
                port=self._config.port,
                dbname=self._config.database,
                user=self._config.user,
                password=self._config.password,
            )
        return self._connection

    def close_connection(self):
        if self._connection:
            self._connection.close()
            self._connection = None
