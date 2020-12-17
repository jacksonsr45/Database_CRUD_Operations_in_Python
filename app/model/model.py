from abc import ABC, abstractmethod

from app.model.query_builder.all_query import AllQuery
from app import conn, cursor

class Model(ABC):

    @abstractmethod
    def insert( self, fields):
        try:
            sql = AllQuery.insert(self.table_name(self), fields)
            cursor.execute(sql)
            results = cursor.fetchall()
            conn.commit()
            return results
        except ConnectionError as error:
            pass

    @abstractmethod
    def update( self, fields, condition):
        try:
            sql = AllQuery.update(self.table_name(self), fields, condition)
            cursor.execute(sql)
            results = cursor.fetchall()
            conn.commit()   
            return results
        except ConnectionError as error:
            pass
        
    @abstractmethod
    def find_all(self):
        try:      
            sql = AllQuery.find_all(self.table_name(self))
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except ConnectionError as error:
            pass

    @abstractmethod
    def find_where(self, fields):
        try:
            sql = AllQuery.find_where(self.table_name(self), fields)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except ConnectionError as error:
            pass

    @abstractmethod
    def delete( self, fields):
        try:
            sql = AllQuery.delete(self.table_name(self), fields)
            cursor.execute(sql)
            conn.commit()
        except ConnectionError as error:
            pass