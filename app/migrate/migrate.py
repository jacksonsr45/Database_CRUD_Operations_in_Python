from abc import ABC, abstractmethod
from app import conn, cursor

class Migrate(ABC):
        
    ##
    # This function get value by new table in value list
    # @param list value
    # @return list self.value
    # #
    @abstractmethod
    def create_table(self, value):
        self.value = value


    # Prepare query from migrate
    """
    # @param list value
    * @return string self.sql
    """
    @abstractmethod
    def __prepare_query(self):
        __list = list()
        __list.append("""CREATE TABLE IF NOT EXISTS {} (""".format(self.table_name(self)))
        __list.append(", ".join(self.table(self)))
        __list.append(");")
        self.sql = "".join(__list)

    ##
    # This function exec query in msqly
    # @param void
    # #
    @abstractmethod
    def exec_query(self):
        self.__prepare_query(self)
        cursor.execute(self.sql)