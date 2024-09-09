from django.test import TestCase, Client
from django.utils import timezone
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        name = Product.objects.create(
          name="konohapedia",
          description = "Semua produk yang dijual di tempat kami, 1000 persen ori",
          price = 8,
          rating = 6.0,
          date = 7,
          
        )
        self.assertTrue(name.is_mood_strong)
        