from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import UserDefaults
from checkout.models import Order
from .forms import UserDefaultsForm

User = get_user_model()

class UserDefaultsModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.defaults = UserDefaults.objects.create(
            user=self.user,
            first_name='Test',
            last_name='User',
            phone_number='1234567890',
            address_line1='123 Test Street',
            address_line2='Apt 4',
            town_or_city='Testville',
            county='Testshire',
            postcode='TEST123',
            country='GB'
        )

    def test_defaults_str(self):
        self.assertEqual(str(self.defaults), "testuser's defaults")

class UserProfileViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.defaults = UserDefaults.objects.create(
            user=self.user,
            first_name='Test',
            last_name='User',
            phone_number='1234567890',
            address_line1='123 Test Street',
            address_line2='Apt 4',
            town_or_city='Testville',
            county='Testshire',
            postcode='TEST123',
            country='GB'
        )
        self.order = Order.objects.create(
            user=self.user,
            first_name='Test',
            last_name='User',
            total_amount=100.00,
            address_line_1='123 Test Street',
            address_line_2='Apt 4',
            city='Testville',
            county='Testshire',
            postcode='TEST123',
            country='GB',
        )

    def test_profile_view_get(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'Test')
        self.assertContains(response, 'User')
        self.assertContains(response, '123 Test Street')
        self.assertContains(response, 'Order History')
        self.assertContains(response, 'Order ID')

    def test_profile_view_post(self):
        data = {
            'first_name': 'Updated',
            'last_name': 'User',
            'phone_number': '0987654321',
            'address_line1': '321 Updated Street',
            'address_line2': 'Apt 5',
            'town_or_city': 'Updatedville',
            'county': 'Updatedshire',
            'postcode': 'UPDATED',
            'country': 'GB'
        }
        response = self.client.post(reverse('profile'), data)
        self.assertRedirects(response, reverse('profile'))
        self.defaults.refresh_from_db()
        self.assertEqual(self.defaults.first_name, 'Updated')
        self.assertEqual(self.defaults.last_name, 'User')
        self.assertEqual(self.defaults.phone_number, '0987654321')

class UserDefaultsFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.defaults = UserDefaults.objects.create(
            user=self.user,
            first_name='Test',
            last_name='User',
            phone_number='1234567890',
            address_line1='123 Test Street',
            address_line2='Apt 4',
            town_or_city='Testville',
            county='Testshire',
            postcode='TEST123',
            country='GB'
        )

    def test_user_defaults_form_valid(self):
        data = {
            'first_name': 'Updated',
            'last_name': 'User',
            'phone_number': '0987654321',
            'address_line1': '321 Updated Street',
            'address_line2': 'Apt 5',
            'town_or_city': 'Updatedville',
            'county': 'Updatedshire',
            'postcode': 'UPDATED',
            'country': 'GB'
        }
        form = UserDefaultsForm(data, instance=self.defaults)
        self.assertTrue(form.is_valid())
        form.save()
        self.defaults.refresh_from_db()
        self.assertEqual(self.defaults.first_name, 'Updated')
        self.assertEqual(self.defaults.last_name, 'User')
        self.assertEqual(self.defaults.phone_number, '0987654321')