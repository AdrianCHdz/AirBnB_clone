#!/usr/bin/python3

from models.engine.file_storage import FileStorage
import unittest


class Test_FileStorage(unittest.TestCase):

    def test_all(self):

        self.assertIsNotNone(FileStorage.all)


if __name__ == "__main__":
    unittest.main()
