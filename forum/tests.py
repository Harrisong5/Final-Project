from django.test import TestCase
from django.contrib.auth.models import User
from forum.models import Post
from forum.forms import CreateUserForm

class CreateUserFormTest(TestCase):

    def test_create_user_form_valid_data(self):
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'complex_password123',
            'password2': 'complex_password123',
        }
        form = CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.username, 'newuser')
        self.assertEqual(user.email, 'newuser@example.com')
        self.assertTrue(user.check_password('complex_password123'))

    def test_create_user_form_invalid_data(self):
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'complex_password123',
            'password2': 'different_password123', 
        }
        form = CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)
        self.assertEqual(form.errors['password2'], ["The two password fields didn't match."])

    def test_create_user_form_missing_username(self):
        form_data = {
            'username': '',
            'email': 'newuser@example.com',
            'password1': 'complex_password123',
            'password2': 'complex_password123',
        }
        form = CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertEqual(form.errors['username'], ["This field is required."])

    def test_create_user_form_invalid_email(self):
        form_data = {
            'username': 'newuser',
            'email': 'invalidemail', 
            'password1': 'complex_password123',
            'password2': 'complex_password123',
        }
        form = CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'], ["Enter a valid email address."])
