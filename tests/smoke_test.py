import unittest
from app import app

class TestAppSmoke(unittest.TestCase):
	def setUp(self):
		app.testing = True
		self.client = app.test_client()
        
	# Check that the application responds successfully
	def test_prediction_route_success(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	# Check that the weather input form is rendered
	def test_get_form(self):
		response = self.client.get('/')
		self.assertIn(b'<form', response.data)
		self.assertIn(b'name="temperature"', response.data)
		self.assertIn(b'Predict', response.data)

if __name__ == '__main__':
	unittest.main()
