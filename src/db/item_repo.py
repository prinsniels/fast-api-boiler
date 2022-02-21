
from typing import Optional

from src.db.pgcon import PGConnection


class ItemRepo:
    def __init__(self, connection: PGConnection) -> None:
        self.connection = connection

    def get_by_id(self, id: str):
        sql = """select id, name from item where name = %(id)s;"""
        with self.connection.connection.cursor() as c:
            c.execute(sql, {"id": id})
            data = c.fetchone()
            if data:
                return data
            return None

    def get_all(self):
        return [{"id": 1, "name": "foo"}, ]
