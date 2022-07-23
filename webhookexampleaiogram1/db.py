from databases import Database


database = Database("sqlite:///bot.db")


async def run():
    await database.connect()
    await database.execute(
        """CREATE TABLE messages (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                telegram_id INTEGER NOT NULL,
                                text text NOT NULL
                                );"""
    )


run()
