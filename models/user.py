import sqlite3


class User:
    def __init__(self) -> None:
        self.db = sqlite3.connect("sql.db")
        self.cursor = self.db.cursor()
        self.username = None
        self.password = None
        self.firstName = None
        self.lastName = None

    def create(
        self, username: str, password: str, firstName: str, lastName: str
    ) -> int:
        # create new user
        try:
            db = self.db
            db.execute(
                """INSERT INTO user(username, password, firstname, lastname) VALUES (?, ?, ?, ?)""",
                (username, password, firstName, lastName),
            )
            db.commit()
            return 1
        except sqlite3.Error as e:
            print(f"Error inserting user: {e}")
            return None

    def updateLoginInfo(self, username, password):
        # update username and password of a user
        pass

    def updateInfo(self, userID: int, firstName: str, lastName: str):
        try:
            db = self.db
            db.execute(
                f"UPDATE user SET firstname = ?, lastname = ? WHERE id = ?",
                (firstName, lastName, userID),
            )
            db.commit()
            return 1
        except sqlite3.Error as e:
            print(f"Error updating user: {e}")
            return None

    def fetch(self, userID: int):
        res = {"username": "", "password": "", "firstName": "", "lastName": ""}

        try:
            db = self.db
            cursor = db.cursor()
            cursor.execute(
                "SELECT username, password, firstname, lastname FROM user WHERE id = ?",
                (userID,),
            )
            result = cursor.fetchall()
            for row in result:
                res["username"] = row[0]
                res["password"] = row[1]
                res["firstName"] = row[2]
                res["lastName"] = row[3]
                
            return res
        except sqlite3.Error as e:
            print(f"Error fetching user details: {e}")
            return []

    def close(self):
        self.cursor.close()
        self.db.close()
