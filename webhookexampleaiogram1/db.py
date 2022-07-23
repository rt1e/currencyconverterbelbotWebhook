from databases import Database


database = Database("sqlite+aiosqlite:///bot.db")


async def create_table(database):
    await database.connect()
    query = """CREATE TABLE messages (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                telegram_id INTEGER NOT NULL,
                                text text NOT NULL
                                );"""
    await database.execute(query=query)
    return database


database = create_table(database)
