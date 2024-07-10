from django.test import TestCase

# Create your tests here.
class DeleteFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='complex_password123')
        self.post = Post.objects.create(title='Test Post', content='test content', author=self.user)

    def test_delete_form_valid(self):
        form_data = {
            'id': self.post.id
        }
        form = DeleteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_delete_form_invalid(self):
        form_data = {
            'id': 999
        }
        form = DeleteForm(data=form_data)
        self.assertFalse(form.is_valid())