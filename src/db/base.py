from databases import Database
from sqlalchemy import create_engine, MetaData

from core.config import DATABASE_URL

database = Database(DATABASE_URL)

# for manage all DB instances: tables, fields etc.
metadata = MetaData()

# only for synchronous requests to DB (use it to init DB during starting APP to create all tables)
engine = create_engine(DATABASE_URL)


