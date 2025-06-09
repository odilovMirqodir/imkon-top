import aiosqlite


class UserDatabase:
    def __init__(self, db_path: str = "users.db"):
        self.db_path = db_path

    async def create_table(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    first_name TEXT,
                    full_name TEXT,
                    language TEXT
                );
            """)
            await db.commit()

    async def add_user(self, user_id: int, username: str, first_name: str, full_name: str, language: str):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT OR IGNORE INTO users (user_id, username, first_name, full_name, language)
                VALUES (?, ?, ?, ?, ?);
            """, (user_id, username, first_name, full_name, language))
            await db.commit()

    async def get_user(self, user_id: int):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)) as cursor:
                row = await cursor.fetchone()
                return row

    async def get_user_language(self, user_id):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute("SELECT language FROM users WHERE user_id = ?", (user_id,)) as cursor:
                row = await cursor.fetchone()
                return row

    async def user_exists(self, user_id: int) -> bool:
        return await self.get_user(user_id) is not None

    async def update_language(self, user_id: int, language: str):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                UPDATE users SET language = ? WHERE user_id = ?;
            """, (language, user_id))
            await db.commit()

    async def select_all_users_count(self):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute("SELECT COUNT(*) FROM users") as cursor:
                row = await cursor.fetchone()
                return row[0] if row else 0
