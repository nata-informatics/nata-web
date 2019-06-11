from django.test import TestCase

# Create your tests here.

class VendorTest(TestCase):

	def test_vendor_url_exists(self):
		response = Client().get('/vendor/')
		self.assertEqual(response.status_code, 200)

	def test_vendor_using_vendor_template(self):
		response = Client().get('/vendor/')
		self.assertTemplateUsed(response, 'Vendor.html')	

