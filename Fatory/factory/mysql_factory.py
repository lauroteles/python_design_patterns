from usecase import Usecase
from databses import MySqlRepository


class MysqlFactory:
    
    @staticmethod
    def create() ->Usecase:
        return Usecase(MySqlRepository())