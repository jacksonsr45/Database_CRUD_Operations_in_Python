__author__ = 'jacksonsr45@gmail.com'


from os.path import dirname, basename, isfile, join
import sys
import glob

project_module = glob.glob(join(dirname(__file__), "*.py"))
__all__=[basename(f)[:-3] for f in project_module if isfile(f) 
            and not f.endswith('__init__.py')]


import pymysql
pymysql.install_as_MySQLdb()

from app.config import db 

##
# Creating new connection with db and init a cursor
# #
conn = pymysql.connect(db['host'],db['username'],db['password'],db['db_name'] )
cursor = conn.cursor()

##
# Init abstract model 
# #
from app.model import model

##
# Required file migrate and run migrate
# #
from app.migrate.create_table_000001_users import create_table_000001_users
create_table_000001_users.exec_query(self=create_table_000001_users)

##
# Default values by fonts
# #
fonts = {
    'fonts_Button': ("Ubunto", 17),
    'fonts': ("Ubunto", 12),
    'fonts_list': ("Ubunto", 15),
}

##
# Default values by colors
# #
colors = {
    'blue': 'powder blue',
    'white': 'white',
    'black': 'black',
}