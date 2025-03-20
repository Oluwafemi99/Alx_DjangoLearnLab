from django.test import TestCase
from django.contrib.auth.models import User


class AuthTests(TestCase):
    def test_registration(self):
        response = self.client.post('/register/', {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'confirm_password': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Ensure redirection on success
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login(self):
        user = User.objects.create_user(username='testuser', password='password123')
        response = self.client.post('/login/', {
            'username': 'testuser',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 302)
    
    def test_profile_update(self):
        user = User.objects.create_user(username='testuser', password='password123', email='old@example.com')
        self.client.login(username='testuser', password='password123')
        response = self.client.post('/profile/', {
            'username': 'updateduser',
            'email': 'new@example.com',
        })
        user.refresh_from_db()
        self.assertEqual(user.username, 'updateduser')
        self.assertEqual(user.email, 'new@example.com')
