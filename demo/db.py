from langchain_community.utilities import SQLDatabase

def getDB():
    db = SQLDatabase.from_uri("sqlite:///Chinook.db")
    return db

if __name__ == "__main__":
    db=getDB()
    print(db.dialect)
    print(db.get_usable_table_names())
    db.run("SELECT * FROM Artist LIMIT 10;")