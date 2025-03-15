from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author
from django.urls import reverse


class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='Test Author')
        self.book_data = {
            'title': 'Test Book',
            'author': self.author,
            'publication_date': '2023-01-01',
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            'title': 'New Book',
            'author': self.author.id,
            'publication_date': '2023-02-01',
        }
        response = self.client.post(reverse('book-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, 'New Book')

    def test_update_book(self):
        self.client.login(username='testuser', password='testpass')
        updated_data = {
            'title': 'Updated Test Book',
            'author': self.author.id,
            'publication_date': '2023-01-02',
        }
        response = self.client.put(f'/api/books/{self.book.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Test Book')

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_book(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_unauthenticated_create(self):
        data = {
            'title': 'New Book',
            'author': self.author.id,
            'publication_date': '2023-02-01',
        }
        response = self.client.post(reverse('book-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_update(self):
        updated_data = {
            'title': 'Updated Test Book',
            'author': self.author.id,
            'publication_date': '2023-01-02',
        }
        response = self.client.put(f'/api/books/{self.book.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_delete(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)