import unittest

from dbfactory.database import Database


class DatabaseConnectionTest(unittest.TestCase):

    def testDatabaseClass(self):
        database_impls = Database.__subclasses__()

        self.assertEqual(
            len(database_impls),
            3,
            "There should be 3 implementations of Database class in package. Make sure to expose them in __init__.py"
        )


