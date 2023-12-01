import unittest
from tdd_app import app, users

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        users.clear()  # Resetowanie stanu przed każdym testem

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        user = {"name": "Jan", "lastname": "Kowalski"}
        response = self.app.post('/users', json=user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(users), 1)

    def test_update_user(self):
        user = {"name": "Jan", "lastname": "Kowalski"}
        response = self.app.post('/users', json=user)
        user_id = response.json['id']
        update = {"name": "Janek"}
        response = self.app.patch(f'/users/{user_id}', json=update)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(users[user_id]['name'], "Janek")

    def test_replace_user(self):
        user = {"name": "Jan", "lastname": "Kowalski"}
        response = self.app.post('/users', json=user)
        user_id = response.json['id']
        replace = {"name": "Piotr", "lastname": "Nowak"}
        response = self.app.put(f'/users/{user_id}', json=replace)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(users[user_id], replace)

    def test_delete_user(self):
        user = {"name": "Jan", "lastname": "Kowalski"}
        response = self.app.post('/users', json=user)
        user_id = response.json['id']
        response = self.app.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 204)
        self.assertNotIn(user_id, users)



if __name__ == '__main__':
    unittest.main()
