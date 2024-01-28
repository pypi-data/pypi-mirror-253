#!/usr/bin/env python

import os
import random
import string
import unittest
import unittest.mock

from waflibs import error, config
from waflibs import database
from waflibs.dns import mysql


def random_string():
    return "".join(
        random.choice(string.ascii_lowercase)
        for i in range(random.randint(10, 51))
    )


class TestMysql(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cfg = config.parse_yaml_file(
            "{}/.config/test.yml".format(os.environ["HOME"])
        )
        mysql_cfg = cfg["mysql_credentials"]
        cls.db = database.mysql_connect(
            mysql_cfg["host"],
            mysql_cfg["username"],
            mysql_cfg["password"],
            mysql_cfg["database"],
        )
        cls.logger = unittest.mock.Mock()
        cls.ignored_ips = cfg["ignored_ips_prefix"]
        cls.domains = ["example.com"]


class TestAddDnsToMysql(TestMysql):
    def test_wikipedia(self):
        mysql.add_dns_to_mysql(
            self.db,
            self.logger,
            random_string(),
            self.ignored_ips,
            self.domains,
            wikipedia_link=random_string(),
        )

    def test_valid_hostname(self):
        mysql.add_dns_to_mysql(
            self.db,
            self.logger,
            random_string(),
            self.ignored_ips,
            self.domains,
        )

    def test_no_hostname(self):
        with self.assertRaises(error.ValidationError) as e:
            mysql.add_dns_to_mysql(
                self.db, self.logger, None, self.ignored_ips, self.domains
            )

        self.assertRegex(e.exception.message, r"hostname")

    def test_no_domains(self):
        mysql.add_dns_to_mysql(
            self.db, self.logger, random_string(), self.ignored_ips
        )

    def test_add_cname(self):
        mysql.add_dns_to_mysql(
            self.db,
            self.logger,
            random_string(),
            self.ignored_ips,
            record_type="CNAME",
            content=random_string(),
        )

    def test_add_existing_cname(self):
        string = random_string()
        name = "EXISTINGCNAME"
        mysql.add_dns_to_mysql(
            self.db,
            self.logger,
            name,
            self.ignored_ips,
            record_type="CNAME",
            content=string,
        )
        cursor = self.db.cursor(buffered=True, dictionary=True)
        cursor.execute(
            "SELECT * FROM non_numeric_records \
                WHERE name = '{}'".format(
                name
            )
        )
        results = cursor.fetchall()
        self.assertEqual(len(results), 1)
