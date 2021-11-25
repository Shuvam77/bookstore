from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls.base import reverse, resolve

# from users.forms import CustomUserCreationForm
# from users.views import SignupPageView

# Create your tests here.


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='prakash',
            email='prakash@gmail.com',
            password='shahi123'
        )

        self.assertEqual(user.username, 'prakash')
        self.assertEqual(user.email, 'prakash@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@gmail.com',
            password='shahi123'
        )

        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class SignupTest(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi! I should not be on the page.')

    # def test_signup_form(self):
    #     form = self.response.context.get('form')
    #     self.assertIsInstance(form, CustomUserCreationForm)
    #     self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)


    # def test_signup_view(self):
    #     view = resolve('/accounts/signup/')
    #     self.assertEqual(
    #         view.func.__name__,
    #         SignupPageView.as_view().__name__
    #     )
