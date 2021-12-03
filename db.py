import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

db_name = os.environ["DB_NAME"]
db_user = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_host = os.environ["DB_HOST"]
db_port = os.environ["DB_PORT"]


class Database:
	@classmethod
	async def create(self):
		# connect to db
		self.conn = await psycopg.AsyncConnection.connect(
			f"dbname={db_name} user={db_user} host={db_host} port={db_port} password={db_password}"
		)
