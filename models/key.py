from datetime import datetime, timedelta
import sqlite3
import string
import secrets
import time
import datetime


class Key:
    def __init__(self) -> None:
        self.db = sqlite3.connect("sql.db")
        self.cursor = self.db.cursor()

    def generateKey(self, userID: int) -> dict:
        # Define the characters to use in the password
        characters = string.ascii_letters + string.digits
        # Generate a random password of the specified length
        key = "".join(secrets.choice(characters) for _ in range(32))
        res = self.saveKey(key, userID)
        if res:
            return {"key": key}
        else:
            return {"key": None}

    def saveKey(self, key: str, userID: int):
        currentTimestamp = int(time.time())
        expirationTimestamp = int((datetime.datetime.fromtimestamp(currentTimestamp) + timedelta(days=30)).timestamp())
        try:
            db = self.db
            db.execute(
                """INSERT INTO access_key(fk_user_id, user_key, created, valid_until) VALUES (?, ?, ?, ?)""",
                (userID, key, currentTimestamp, expirationTimestamp),
            )
            db.commit()
            return 1
        except sqlite3.Error as e:
            print(f"Error inserting user: {e}")
            return None

    def verifyKey(self, key):
        # verify key if valid or already expired
        pass
    
    def close(self):
        self.cursor.close()
        self.db.close()

