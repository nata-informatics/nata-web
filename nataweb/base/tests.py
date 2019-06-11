from django.test import TestCase

# Create your tests here.

class BaseTest(TestCase):

	def test_base_not_error(self):
		response = Client().get('/')
		self.assertEqual(response.status_code, 200)

