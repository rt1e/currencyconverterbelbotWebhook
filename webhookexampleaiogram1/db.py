from databases import Database


database = Database("sqlite+aiosqlite:///bot.db")
await database.connect()
query = """CREATE TABLE messages (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                telegram_id INTEGER NOT NULL,
                                text text NOT NULL
                                );"""
await database.execute(query=query)


database = create_table(database)
