import requests
import unittest


class TestAPI(unittest.TestCase):

    API_URL = 'https://jsonplaceholder.typicode.com/users'

    def test_get_users(self):


        response = requests.get(self.API_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)

    def test_get_user_by_id(self):


        user_id = 1
        response = requests.get(f'{self.API_URL}/{user_id}')
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user['id'], user_id)

    def test_invalid_endpoint(self):


        response = requests.get(f'{self.API_URL}/invalid')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()

