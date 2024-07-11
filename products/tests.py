from django.test import TestCase, Client
from django.urls import reverse
from .models import Product, Brand, Category, CPUSocket, RAMTechnology, FormFactor, Motherboard, CPU, RAM, PSU, GPU, Case, Storage

class ProductModelTests(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Test Brand')
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            price=100.00,
            description='Test Product Description',
            available_quantity=10,
            brand=self.brand,
            category=self.category,
            sku='12345',
            is_discounted=True,
            discount_price=80.00,
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_savings(self):
        self.assertEqual(self.product.savings(), 20.00)

class ProductListViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.brand = Brand.objects.create(name='Test Brand')
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            price=100.00,
            description='Test Product Description',
            available_quantity=10,
            brand=self.brand,
            category=self.category,
            sku='12345',
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('all_products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products.html')
        self.assertContains(response, 'Test Product')

class ProductDetailViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.brand = Brand.objects.create(name='Test Brand')
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            price=100.00,
            description='Test Product Description',
            available_quantity=10,
            brand=self.brand,
            category=self.category,
            sku='12345',
        )

    def test_product_detail_view(self):
        response = self.client.get(reverse('product_detail', args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertContains(response, 'Test Product')

class ProductSearchTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.brand = Brand.objects.create(name='Test Brand')
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            price=100.00,
            description='Test Product Description',
            available_quantity=10,
            brand=self.brand,
            category=self.category,
            sku='12345',
        )

    def test_search_view(self):
        response = self.client.get(reverse('search'), {'searchbar': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/search_results.html')
        self.assertContains(response, 'Test Product')

class ProductFilterTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.brand = Brand.objects.create(name='Test Brand')
        self.category = Category.objects.create(name='Test Category')
        self.product1 = Product.objects.create(
            name='Test Product 1',
            price=50.00,
            description='Test Product Description 1',
            available_quantity=10,
            brand=self.brand,
            category=self.category,
            sku='12345',
        )
        self.product2 = Product.objects.create(
            name='Test Product 2',
            price=150.00,
            description='Test Product Description 2',
            available_quantity=10,
            brand=self.brand,
            category=self.category,
            sku='67890',
        )

    def test_filter_by_price(self):
        response = self.client.get(reverse('all_products'), {'price_min': '100'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products.html')
        self.assertNotContains(response, 'Test Product 1')
        self.assertContains(response, 'Test Product 2')

    def test_filter_by_category(self):
        response = self.client.get(reverse('all_products'), {'category': self.category.name})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products.html')
        self.assertContains(response, 'Test Product 1')
        self.assertContains(response, 'Test Product 2')

    def test_filter_by_brand(self):
        response = self.client.get(reverse('all_products'), {'brand': self.brand.name})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products.html')
        self.assertContains(response, 'Test Product 1')
        self.assertContains(response, 'Test Product 2')

    def test_filter_by_rating(self):
        self.product1.rating = 4.5
        self.product1.save()
        self.product2.rating = 3.0
        self.product2.save()
        response = self.client.get(reverse('all_products'), {'rating_min': '4.0'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products.html')
        self.assertContains(response, 'Test Product 1')
        self.assertNotContains(response, 'Test Product 2')

    def test_sort_by_price(self):
        response = self.client.get(reverse('all_products'), {'sort_by': 'price'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products.html')
        products = list(response.context['products'])
        self.assertLess(products[0].price, products[1].price)

    def test_sort_by_name(self):
        response = self.client.get(reverse('all_products'), {'sort_by': 'name'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all_products.html')
        products = list(response.context['products'])
        self.assertEqual(products[0].name, 'Test Product 1')
        self.assertEqual(products[1].name, 'Test Product 2')