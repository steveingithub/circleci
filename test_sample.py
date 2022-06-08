import sample
import unittest


class TestSample(unittest.TestCase):

    def setUp(self):
        self.app = sample.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_greeting_message(self):
        greeting = 'Welcome to CI/CD'
        self.assertEqual(sample.greet(), greeting)


if __name__ == '__main__':
    unittest.main()
