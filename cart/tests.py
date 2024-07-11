from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CartItem
from products.models import Product, Brand, Category

User = get_user_model()

class CartTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
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

    def test_add_to_cart_logged_in(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]), {'quantity': 1})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CartItem.objects.filter(user=self.user, product=self.product).exists())

    def test_add_to_cart_not_logged_in(self):
        session = self.client.session
        session.create()
        session_key = session.session_key
        session.save()

        self.client.cookies['sessionid'] = session_key
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]), {'quantity': 1})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CartItem.objects.filter(session_key=session_key, product=self.product).exists())

    def test_cart_detail_view_logged_in(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('cart_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart_detail.html')
        self.assertContains(response, 'Test Product')

    def test_cart_detail_view_not_logged_in(self):
        session = self.client.session
        session.create()
        session_key = session.session_key
        session.save()

        CartItem.objects.create(
            session_key=session_key,
            product=self.product,
            quantity=1,
            total_price=100.00
        )

        self.client.cookies['sessionid'] = session_key
        response = self.client.get(reverse('cart_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart_detail.html')
        self.assertContains(response, 'Test Product')

    def test_remove_from_cart_logged_in(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('remove_from_cart', args=[self.cart_item.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(CartItem.objects.filter(user=self.user, product=self.product).exists())

    def test_remove_from_cart_not_logged_in(self):
        session = self.client.session
        session.create()
        session_key = session.session_key
        session.save()

        cart_item = CartItem.objects.create(
            session_key=session_key,
            product=self.product,
            quantity=1,
            total_price=100.00
        )

        self.client.cookies['sessionid'] = session_key
        response = self.client.post(reverse('remove_from_cart', args=[cart_item.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(CartItem.objects.filter(session_key=session_key, product=self.product).exists())