from src.sqlengine.sqlengine import build_engine, Engine


driver: str = input("Enter the driver: ")

if driver == "access":
    db_path: str = input("Enter the path to the database: ")
    engine: Engine = build_engine(
        local_db_filepath=db_path
    )
else:
    host: str = input("Enter the host: ")
    database: str = input("Enter the database: ")
    engine: Engine = build_engine(
        driver=driver,
        host=host,
        database=database
    )

print(engine.url)
print(engine.connect())
