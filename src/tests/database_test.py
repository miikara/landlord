import unittest
from database import DataBaseService

class TestDataBaseService(unittest.TestCase):
    def test_create_user(self):
        data_base_service = DataBaseService()
        test_conn = data_base_service.connect()
        data_base_service.create_user(test_conn, 'test_name', 'test_password')
        result = str(data_base_service.get_user(test_conn, 'test_name'))
        data_base_service.delete_user(test_conn, 'test_name')
        test_conn.close()
        self.assertNotEqual(result, None)