import unittest
from models.base_model import BaseModel

"""this is unit test"""


class TesrBaseModel(unittest.TestCase):

    def in_test(self):
        my_base = BaseModel()

        self.assertIsNone(my_base.id)
        self.assertIsNone(my_base.created_at)
        self.assertIsNone(my_base.updated_at)

    def sa_test(self):
        my_base = BaseModel()

        define_update = my_base.update.at
        cuurnt_update = my_base.save()

        self.assertNotEqual(define_update, cuurnt_update)

    def di_test(self):
        my_base = BaseModel()
        my_base_dict = my_base.to_dict()

        self.assertIsInstance(my_base_dict, dict)
        self.assertEqual(my_base_dict['__class__'], my_base)
        self.assertEqual(my_base_dict['id'], my_base.id)
        self.assertEqual(my_base_dict['created_at'], my_base.iso_created)
        self.assertEqual(my_base_dict['updated_at'], my_base.iso_updated)

    def st_test(self):
        my_base = BaseModel()

        self.assertTrue(str(my_base).startswith("[BaseModel]"))
        self.assertIn(my_base.id, str(my_base))
        self.assertIn(str(my_base.__dict__), str(my_base))


if __name__ == '__main__':
    unittest.main()
