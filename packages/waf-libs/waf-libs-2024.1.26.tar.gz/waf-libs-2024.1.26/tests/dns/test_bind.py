#!/usr/bin/env python

import tempfile
import unittest

from waflibs.dns import bind


class TestDns(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bind_dir = tempfile.TemporaryDirectory()

        cls.bind_dir = bind_dir
        cls.domain = "test.com"
        cls.records = [
            {
                "name": "fullname.record.",
                "type": "CNAME",
                "content": "nodot",
                "proxied": False,
            },
            {
                "name": "shortname",
                "type": "CNAME",
                "content": "hasadot.",
                "proxied": False,
            },
            {
                "name": "test",
                "type": "A",
                "content": "1.2.3.4",
                "proxied": False,
            },
            {
                "name": "longtest.",
                "type": "AAAA",
                "content": "123:ABC::4",
                "proxied": False,
            },
            {
                "name": "sigh.test.com.",
                "type": "A",
                "content": "2.3.4.5",
                "proxied": False,
            },
            {
                "name": "test.com.",
                "type": "MX",
                "content": "mx.garbage",
                "proxied": False,
                "priority": 99,
            },
            {
                "name": "nameserver",
                "type": "NS",
                "content": "name.server.",
                "proxied": False,
            },
        ]
        cls.result = """; HEADER

$ORIGIN test.com

{}

fullname.record. IN CNAME nodot
shortname IN CNAME hasadot.
test IN A 1.2.3.4
longtest. IN AAAA 123:ABC::4
sigh.test.com. IN A 2.3.4.5
test.com. IN MX 99 mx.garbage
nameserver IN NS name.server.

; 7 total records found

"""

    @classmethod
    def tearDownClass(cls):
        cls.bind_dir.cleanup()

    def setUp(self):
        serial = bind.generate_serial(self.bind_dir.name)

        template_file = tempfile.TemporaryFile()
        template_file.write(b"; HEADER\n\n$ORIGIN {zone}\n\n{serial}\n")
        template_file.seek(0)

        domain_template_file = tempfile.TemporaryFile()
        domain_template_file.write(b"{records}\n")
        domain_template_file.seek(0)

        serial_file = open("{}/serial".format(self.bind_dir.name), "w")
        serial_file.write("{}\n".format(serial))
        serial_file.seek(0)

        self.serial = serial
        self.domain_template_file = domain_template_file
        self.template_file = template_file
        self.serial_file = serial_file

    def test_generate_bind_file_serial(self):
        zone_file_name = bind.generate_bind_file(
            self.records,
            self.domain,
            serial_number=self.serial,
            bind_dir=self.bind_dir.name,
            template_file_name=self.template_file.name,
            domain_template_file_name=self.domain_template_file.name,
        )

        zone_file = open(zone_file_name)
        self.assertEqual(zone_file.read(), self.result.format(self.serial))
        zone_file.close()

    def test_generate_bind_file_no_serial(self):
        zone_file_name = bind.generate_bind_file(
            self.records,
            self.domain,
            bind_dir=self.bind_dir.name,
            template_file_name=self.template_file.name,
            domain_template_file_name=self.domain_template_file.name,
        )

        zone_file = open(zone_file_name)
        self.assertEqual(zone_file.read(), self.result.format(self.serial + 1))
        zone_file.close()


if __name__ == "__main__":
    unittest.main()
