from django.test import TestCase

from django.urls import reverse, resolve
from shop.views import login_view, signup_view, home_view

class URLTests(TestCase):
    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_view)

    def test_signup_url(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signup_view)

    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home_view)

    def test_shop_urls_included(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home_view)
