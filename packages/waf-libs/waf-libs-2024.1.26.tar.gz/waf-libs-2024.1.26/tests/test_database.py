#!/usr/bin/env/python

import unittest
import unittest.mock
import os

from waflibs import database, config


class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = config.parse_yaml_file(
            "{}/.config/test.yml".format(os.environ["HOME"])
        )


#    @classmethod
#    def tearDownClass(cls):
#        import mysql.connector
#        mysql.connector = mysql.connector


class TestMysqlConnect(TestDatabase):
    def test_mysql_connect(self):
        mysql_config = self.config["mysql_credentials"]
        import mysql.connector

        mysql.connector.connect = unittest.mock.MagicMock()

        database.mysql_connect(
            mysql_config["host"],
            mysql_config["username"],
            mysql_config["password"],
            mysql_config["database"],
        )

        mysql.connector.connect.assert_called_with(
            host=mysql_config["host"],
            user=mysql_config["username"],
            password=mysql_config["password"],
            db=mysql_config["database"],
        )


class TestPostgresqlConnect(TestDatabase):
    def test_postgresql_connect(self):
        postgres_config = self.config["postgres_credentials"]
        import psycopg2

        psycopg2.connect = unittest.mock.MagicMock()

        database.postgresql_connect(
            postgres_config["host"],
            postgres_config["username"],
            postgres_config["password"],
            postgres_config["database"],
        )

        psycopg2.connect.assert_called_with(
            host=postgres_config["host"],
            user=postgres_config["username"],
            password=postgres_config["password"],
            dbname=postgres_config["database"],
        )


if __name__ == "__main__":
    unittest.main()
