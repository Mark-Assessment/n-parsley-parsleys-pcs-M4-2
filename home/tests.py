from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from products.models import Product, Brand, Category

User = get_user_model()

class HomeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.brand = Brand.objects.create(name='Test Brand')
        self.category = Category.objects.create(name='Test Category')
        self.discounted_product = Product.objects.create(
            name='Discounted Product',
            price=100.00,
            description='Discounted Product Description',
            available_quantity=10,
            brand=self.brand,
            category=self.category,
            sku='12345',
            is_discounted=True,
            discount_price=80.00,
        )
        self.featured_product = Product.objects.create(
            name='Featured Product',
            price=150.00,
            description='Featured Product Description',
            available_quantity=10,
            brand=self.brand,
            category=self.category,
            sku='67890',
            is_featured=True,
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertContains(response, 'Discounted Product')
        self.assertContains(response, 'Featured Product')

class SetCurrencyViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_set_currency_to_usd(self):
        response = self.client.get(reverse('set_currency', args=['USD']))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['currency_info'], 'USD:1.33')
        self.assertEqual(self.client.session['currency'], 'USD')

    def test_set_currency_to_eur(self):
        response = self.client.get(reverse('set_currency', args=['EUR']))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['currency_info'], 'EUR:1.13')
        self.assertEqual(self.client.session['currency'], 'EUR')

    def test_set_currency_to_gbp(self):
        response = self.client.get(reverse('set_currency', args=['GBP']))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['currency_info'], 'GBP:1.0')
        self.assertEqual(self.client.session['currency'], 'GBP')

    def test_set_currency_to_invalid(self):
        response = self.client.get(reverse('set_currency', args=['AUD']))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['currency_info'], 'AUD:0.75')
        self.assertEqual(self.client.session['currency'], 'AUD')