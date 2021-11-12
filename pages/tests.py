from django.conf.urls import url
from django.http import response
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from pages.views import HomePageView

# Create your tests here.


class HomePageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        # response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        # response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        # response = self.client.get('/')
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contains_incorrect_html(self):
        # response = self.client.get('/')
        self.assertNotContains(self.response, 'Hi there! I should not be here.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )