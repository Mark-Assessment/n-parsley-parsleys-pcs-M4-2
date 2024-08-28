from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Order
from .forms import CheckoutForm
from cart.models import CartItem
from products.models import Product, Brand, Category

User = get_user_model()


class OrderModelTest(TestCase):
    def test_order_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        order = Order.objects.create(
            user=user,
            first_name='John',
            last_name='Doe',
            total_amount=100.00,
            address_line_1='123 Test St',
            city='Test City',
            postcode='12345',
            country='Test Country'
        )
        self.assertEqual(order.__str__(), f"Order {order.id} by {order.user}")
        self.assertEqual(order.total_amount, 100.00)


class CheckoutFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'address_line_1': '123 Test St',
            'address_line_2': 'Apt 1',
            'city': 'Test City',
            'county': 'Test County',
            'postcode': '12345',
            'country': 'Test Country',
        }
        form = CheckoutForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'first_name': '',
            'last_name': '',
            'address_line_1': '',
            'city': '',
            'postcode': '',
            'country': '',
        }
        form = CheckoutForm(data=data)
        self.assertFalse(form.is_valid())


class CheckoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.brand = Brand.objects.create(name='Test Brand')
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            price=100.00,
            description='Test Description',
            available_quantity=10,
            brand=self.brand,
            category=self.category,
            sku='12345',
        )
        self.cart_item = CartItem.objects.create(
            user=self.user,
            product=self.product,
            quantity=1,
            total_price=100.00
        )

    def test_checkout_view_get(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_view_post(self):
        self.client.login(username='testuser', password='12345')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'address_line_1': '123 Test St',
            'city': 'Test City',
            'postcode': '12345',
            'country': 'Test Country',
        }
        response = self.client.post(reverse('checkout'), data)
        self.assertEqual(response.status_code, 302)
        order = Order.objects.get(user=self.user)
        self.assertIsNotNone(order)
        self.assertEqual(order.first_name, 'John')
        self.assertEqual(order.total_amount, self.cart_item.total_price)
