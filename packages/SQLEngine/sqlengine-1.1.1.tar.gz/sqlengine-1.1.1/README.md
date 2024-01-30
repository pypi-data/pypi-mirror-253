# SQLEngine

SQLEngine is a basic wrapper around the SQLAlchemy library - specifically focused on simple Engine creation.

## Usage

```python
from sqlengine import build_engine

engine = build_engine(  # This gives you an SQLAlchemy Engine object with which you can .connect() 
    driver="mssql",
    host="127.0.0.1/DB_Server",
    database="DB_Name"
)
```
Connecting to a more obscure DBMS such as Microsoft's Access is also supported.:
```python
from sqlengine import build_engine

# The driver, host, and database parameters are ignored when using Access. 
# The wrapper deals with obscure necessities such as DBMS-specific connection parameters.
engine = build_engine(  
    driver="access",
    local_db_filepath="C:\\Users\\User\\Desktop\\Database.accdb"
)
```
Whilst yet untested, connecting to pretty much any DBMS should be supported:
```python
from sqlengine import build_engine

engine = build_engine(
    driver="mysql",
    host="https://www.mycompany.fake/DB_Server",
    database="DB_Name",
    username="my_username",  # Note the additional keyword arguments
    password="my_password"
)
```
