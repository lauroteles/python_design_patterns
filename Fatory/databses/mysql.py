from typing import Dict
from interface import DatabaseInterface


class MySqlRepository(DatabaseInterface):

    def select_one(self) -> Dict:
        return {"data": "data from mysql",
                'status': 'success'}