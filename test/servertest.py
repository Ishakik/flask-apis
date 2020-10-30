import unittest
import json
from server import app


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_server_health(self):
        response = self.app.get('/api/health')
        self.assertEqual('GREEN', response.json['server health'])
        self.assertEqual(200, response.status_code)

    def test_successful_encryption(self):
        request_payload = json.dumps({
            'Input': 'plain text'
        })
        response = self.app.post('/api/encrypt', headers={"Content-Type": "application/json"}, data=request_payload)
        self.assertEqual('Encrypted_plain text_String', response.json['Output'])
        self.assertEqual('plain text', response.json['Input'])
        self.assertEqual('success', response.json['Status'])
        self.assertEqual('encryption successful', response.json['Message'])
        self.assertEqual(200, response.status_code)

    def test_encryption_with_empty_input(self):
        request_payload = json.dumps({
            'Input': ''
        })
        response = self.app.post('/api/encrypt', headers={"Content-Type": "application/json"}, data=request_payload)
        self.assertEqual('', response.json['Output'])
        self.assertEqual('', response.json['Input'])
        self.assertEqual('failure', response.json['Status'])
        self.assertEqual('input should not be empty', response.json['Message'])
        self.assertEqual(400, response.status_code)

    def test_successful_decryption(self):
        request_payload = json.dumps({
            'Input': 'Encrypted_plain text_String'
        })
        response = self.app.post('/api/decrypt', headers={"Content-Type": "application/json"}, data=request_payload)
        self.assertEqual('plain text', response.json['Output'])
        self.assertEqual('Encrypted_plain text_String', response.json['Input'])
        self.assertEqual('success', response.json['Status'])
        self.assertEqual('decryption successful', response.json['Message'])
        self.assertEqual(200, response.status_code)

    def test_decryption_with_empty_input(self):
        request_payload = json.dumps({
            'Input': ''
        })
        response = self.app.post('/api/encrypt', headers={"Content-Type": "application/json"}, data=request_payload)
        self.assertEqual('', response.json['Output'])
        self.assertEqual('', response.json['Input'])
        self.assertEqual('failure', response.json['Status'])
        self.assertEqual('input should not be empty', response.json['Message'])
        self.assertEqual(400, response.status_code)


if __name__ == '__main__':
    unittest.main()
