import os
from configparser import ConfigParser
import psycopg2

thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'db.ini')

parser = ConfigParser()
parser.read(initfile)

conn = psycopg2.connect(
    dbname = parser["database"]["dbname"],
    user = parser["database"]["user"],
    host = parser["database"]["host"],
    password = parser["database"]["password"]
)