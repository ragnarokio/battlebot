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


# creeate using Database.create()
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
        cur = self.conn.cursor()
        await cur.execute(
            """
			INSERT INTO players (id, character_name) VALUES (%s, %s)
		""",
            (discord_id, character_name),
        )

        await self.conn.commit()

    async def delete_player(self, discord_id):
        cur = self.conn.cursor()
        await cur.execute(
            "DELETE FROM players WHERE id=%s",
            [
                discord_id,
            ],
        )
        await self.conn.commit()
