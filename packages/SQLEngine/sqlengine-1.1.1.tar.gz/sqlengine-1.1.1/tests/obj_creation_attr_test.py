import unittest
from sqlalchemy import create_engine, URL
from sqlengine import SQLEngine, MSSQLEngine, AccessEngine, build_engine


class TestSQLEngine(unittest.TestCase):
    """Test case for the SQLEngine class."""
    def setUp(self):
        self.sqle = SQLEngine(driver='mysql+pymysql', host='localhost', database='test_db', query={'charset': 'utf8mb4'})

    def test_create_sqle(self):
        self.assertIsInstance(self.sqle, SQLEngine)
        self.assertEqual(self.sqle.driver, 'mysql+pymysql')
        self.assertEqual(self.sqle.host, 'localhost')
        self.assertEqual(self.sqle.database, 'test_db')
        self.assertEqual(self.sqle.query, {'charset': 'utf8mb4'})

    def test_create_url(self):
        url = URL.create(
            drivername=self.sqle.driver,
            host=self.sqle.host,
            database=self.sqle.database,
            query=self.sqle.query
        )
        self.assertEqual(self.sqle.url, url)

    def test_create_engine(self):
        self.assertIsInstance(self.sqle.engine, create_engine(url=self.sqle.url).__class__)


class TestMSSQLEngine(unittest.TestCase):
    """
    Set up the test case by creating an instance of MSSQLEngine.
    """
    def setUp(self):
        self.ms_sqle = MSSQLEngine(host='localhost', database='test_db')

    def test_create_mssql(self):
        self.assertIsInstance(self.ms_sqle, MSSQLEngine)
        self.assertEqual(self.ms_sqle.driver, 'mssql+pyodbc')
        self.assertEqual(self.ms_sqle.host, 'localhost')
        self.assertEqual(self.ms_sqle.database, 'test_db')
        self.assertEqual(self.ms_sqle.query, {"driver": "SQL Server Native Client 11.0"})


class TestAccessEngine(unittest.TestCase):
    """TestAccessEngine

    This class defines unit tests for the AccessEngine module.

    Attributes:
        access_sqle (AccessEngine): An instance of the AccessEngine class initialized with a valid local Access database file.

    Methods:
        setUp(): Method that is executed before each test method to set up the necessary environment.
        test_create_access(): Method that performs unit testing for the creation of an AccessEngine instance.

    """
    def setUp(self):
        # another.db should be a valid local Access database file
        self.access_sqle = AccessEngine(db_path='another.db')

    def test_create_access(self):
        self.assertIsInstance(self.access_sqle, AccessEngine)
        self.assertEqual(self.access_sqle.driver, 'access+pyodbc')
        self.assertEqual(self.access_sqle.query["driver"], "Microsoft Access Driver (*.mdb, *.accdb)")
        self.assertEqual(self.access_sqle.query["ExtendedAnsiSql"], "1")


class TestBuildEngine(unittest.TestCase):
    """
    This class contains unit tests for the `build_engine` function.

    """
    def test_build_engine(self):
        engine = build_engine(
            driver='mysql+pymysql',
            host='localhost',
            database='test_db',
            query={'charset': 'utf8mb4'},
            local_db_filepath='another.db'
        )
        self.assertIsInstance(engine, create_engine().__class__)


if __name__ == '__main__':
    unittest.main()
