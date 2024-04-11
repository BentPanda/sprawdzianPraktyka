import unittest
from tdd_app import app, users

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        users.clear()

    def test_user_creation(self):
        response = self.app.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
        self.assertEqual(response.status_code, 201)



if __name__ == '__main__':
    unittest.main()
