#!/usr/bin/env python

import os
import pathlib
import tempfile
import unittest

from waflibs import utils


class TestUtils(unittest.TestCase):
    def test_origin_full_domain_shared_two(self):
        origin = utils.convert_origin(
            "test.foo.example.com", "example.com", shared=True
        )

        self.assertEqual(origin, r"test.foo.")

    def test_origin_full_domain_shared_multiple(self):
        origin = utils.convert_origin(
            "test.foo.bar.example.com", "example.com", shared=True
        )

        self.assertEqual(origin, r"test.foo.bar.")

    def test_origin_full_domain(self):
        origin = utils.convert_origin("test.example.com", "example.com")

        self.assertEqual(origin, r"test.example.com.example.com.")

    def test_origin(self):
        origin = utils.convert_origin("test", "example.com")

        self.assertEqual(origin, r"test.example.com.")

    def test_origin_two(self):
        origin = utils.convert_origin("test.foo", "example.com")

        self.assertEqual(origin, r"test.foo.example.com.")

    def test_origin_multiple(self):
        origin = utils.convert_origin("test.foo.bar.baz", "example.com")

        self.assertEqual(origin, r"test.foo.bar.baz.example.com.")

    def test_origin_shared_single(self):
        origin = utils.convert_origin("test", "example.com", shared=True)

        self.assertEqual(origin, r"test")

    def test_origin_shared_multiple(self):
        origin = utils.convert_origin(
            "test.foo.bar.baz", "example.com", shared=True
        )

        self.assertEqual(origin, r"test.foo.bar.baz")

    def test_origin_shared_two(self):
        origin = utils.convert_origin("test.foo", "example.com", shared=True)

        self.assertEqual(origin, r"test.foo")

    def test_divider_default(self):
        self.assertEqual(utils.divider(), "=" * 30)

    def test_divider_char(self):
        self.assertEqual(utils.divider(char="-"), "-" * 30)

    def test_divider_times(self):
        self.assertEqual(utils.divider(times=8), "=" * 8)

    def test_divider_all(self):
        self.assertEqual(utils.divider(char="_", times=9), "_" * 9)

    def test_shell_command(self):
        stdout, stderr, _ = utils.shell_command(["echo", "hello", "there"])
        self.assertEqual(stdout, "hello there\n")
        self.assertEqual(stderr, "")

    def test_dest_location_dotfile_single_path(self):
        dest = utils.get_dest_location("fake")

        self.assertEqual(pathlib.Path(f"/tmp/.fake"), dest)

    def test_dest_location_dotfile_path(self):
        dest = utils.get_dest_location("something/real/fake")

        self.assertEqual(pathlib.Path(f"/tmp/.something/real/fake"), dest)

    def test_dest_location_single_path(self):
        dest = utils.get_dest_location("nothomefake", dotfile=False)

        self.assertEqual(
            pathlib.Path(f"{os.environ['HOME']}/nothomefake"), dest
        )

    def test_dest_location_parent_dir(self):
        dest = utils.get_dest_location(
            "nothomefake", parent_dir="/something/else", dotfile=False
        )

        self.assertEqual(pathlib.Path("/something/else/nothomefake"), dest)

    def test_dest_location_parent_dir_dotfile_single(self):
        dest = utils.get_dest_location(
            "nothomefake", parent_dir="/something/else"
        )

        self.assertEqual(pathlib.Path("/something/else/.nothomefake"), dest)

    def test_dest_location_parent_dir_dotfile_multiple(self):
        dest = utils.get_dest_location(
            "not/omefake", parent_dir="/something/else"
        )

        self.assertEqual(pathlib.Path("/something/else/not/.omefake"), dest)

    def test_dest_location_path(self):
        dest = utils.get_dest_location("rel/sub/not/omefake", dotfile=False)

        self.assertEqual(pathlib.Path(f"/tmp/rel/sub/not/omefake"), dest)

    def test_json_write(self):
        tf = tempfile.NamedTemporaryFile()
        filename = tf.name

        json_string = """{
  "test": "yes",
  "no": "stuff"
}"""
        json_dict = {
            "test": "yes",
            "no": "stuff",
        }

        utils.write_json_file(json_dict, filename)
        tf.seek(0)

        f = open(filename, "r")
        self.assertEqual(f.read(), json_string)


if __name__ == "__main__":
    unittest.main()
