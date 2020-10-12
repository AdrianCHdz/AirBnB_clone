#!/usr/bin/python3

from models.base_model import BaseModel
import unittest


class Test_BaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.Base = BaseModel()
        cls.Base.name = "Julian"
        cls.Base.cod = 1193

    def test_save(self):

        self.Base.save()
        self.assertNotEqual(self.Base.created_at, self.Base.updated_at)

    def test_to_dict(self):

        test_dict = self.Base.to_dict()
        self.assertTrue(test_dict.get("__class__"))
        self.assertTrue(type(test_dict) is dict)
        self.assertTrue("to_dict" in dir(self.Base))


if __name__ == "__main__":
    unittest.main()
