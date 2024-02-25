Run `sqlite3 Chinook.db`
Run `.read Chinook_Sqlite.sql`
Test `SELECT * FROM Artist LIMIT 10;`

Now, Chinhook.db is in our directory and we can interface with it using the SQLAlchemy-driven SQLDatabase class:

```
from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM Artist LIMIT 10;")
```