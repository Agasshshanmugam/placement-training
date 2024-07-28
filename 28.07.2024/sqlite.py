import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                              (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
        self.conn.commit()

    def insert_user(self, name, email):
        self.cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        self.conn.commit()

    def fetch_users(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

def main():
    db = Database('example.db')
    db.create_table()
    db.insert_user('Alice', 'alice@example.com')
    db.insert_user('Bob', 'bob@example.com')
    users = db.fetch_users()
    for user in users:
        print(user)
    db.close()

if __name__ == "__main__":
    main()
