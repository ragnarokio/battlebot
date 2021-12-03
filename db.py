import psycopg
import os
from dotenv import load_dotenv
import logging

load_dotenv()

db_name = os.environ["DB_NAME"]
db_user = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_host = os.environ["DB_HOST"]
db_port = os.environ["DB_PORT"]


# create using database.create()
class database:
	def __init__(self, conn):
		self.conn = conn

	@classmethod
	async def create(cls):
		# connect to db
		conn = await psycopg.AsyncConnection.connect(
			f"dbname={db_name} user={db_user} host={db_host} port={db_port} password={db_password}"
		)

		return cls(conn)

	async def does_player_exist(self, discord_id):
		discord_id = str(discord_id)
		cur = self.conn.cursor()
		await cur.execute(
			"SELECT * FROM players WHERE id=%s",
			[
				discord_id,
			],
		)
		player = await cur.fetchall()
		return len(player) != 0

	async def create_player(self, discord_id, character_name):
		discord_id = str(discord_id)
		cur = self.conn.cursor()
		await cur.execute(
			"""
			INSERT INTO players (id, character_name) VALUES (%s, %s)
		""",
			(discord_id, character_name),
		)

		await self.conn.commit()

	async def delete_player(self, discord_id):
		discord_id = str(discord_id)
		cur = self.conn.cursor()
		await cur.execute(
			"DELETE FROM players WHERE id=%s",
			[
				discord_id,
			],
		)
		await self.conn.commit()

	async def get_player(self, discord_id):
		discord_id = str(discord_id)
		cur = self.conn.cursor()
		await cur.execute(
			"SELECT (character_name) FROM players WHERE id=%s",
			[
				discord_id,
			],
		)

		player = await cur.fetchone()
		character_name = player[0]

		# get the units
		cur = self.conn.cursor()
		await cur.execute(
			"SELECT (id, name, life, damage, tags) FROM units WHERE player_id=%s",
			[
				discord_id,
			],
		)
		units = await cur.fetchall()

		unit_instances = []

		for unit in units:
			unit_id = unit[0]
			name = unit[1]
			life = unit[2]
			damage = unit[3]
			tags = unit[4]

			# TODO: create new unit class instance
			u = ()
			unit_instances.append(u)

		# TODO: create player class instance
		player_instance = ()

		return player

	async def create_unit(self, discord_id, name, life, damage, tags):
		discord_id = str(discord_id)
		cur = self.conn.cursor()
		await cur.execute(
			"INSERT INTO units (player_id, name, life, damage, tags) VALUES(%s, %s, %s, %s, %s) RETURNING id",
			(discord_id, name, life, damage, tags),
		)

		id = await cur.fetchone()
		id = id[0]

		await self.conn.commit()

		return id

	async def delete_unit(self, id):
		cur = self.conn.cursor()
		await cur.execute(
			"DELETE FROM units WHERE id=%s",
			[
				id,
			],
		)
		await self.conn.commit()
