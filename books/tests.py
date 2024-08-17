import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Book


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_book():
    return Book.objects.create(
        title="Test Book",
        author="Test Author",
        isbn="1234567890123",
        published_date="2023-01-01",
        pages=100,
        cover="http://example.com/cover.jpg",
        language="English"
    )


@pytest.mark.django_db
def test_create_book(api_client):
    url = reverse('book-list')
    data = {
        "title": "New Book",
        "author": "New Author",
        "isbn": "9876543210123",
        "published_date": "2023-01-01",
        "pages": 200,
        "cover": "http://example.com/new-cover.jpg",
        "language": "English"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert Book.objects.count() == 1
    assert Book.objects.get().title == "New Book"


@pytest.mark.django_db
def test_get_books(api_client, create_book):
    url = reverse('book-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data['results']) == 1


@pytest.mark.django_db
def test_get_book_detail(api_client, create_book):
    url = reverse('book-detail', args=[create_book.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['title'] == create_book.title


@pytest.mark.django_db
def test_update_book(api_client, create_book):
    url = reverse('book-detail', args=[create_book.id])
    data = {
        "title": "Updated Title",
        "author": "Updated Author",
        "isbn": create_book.isbn,
        "published_date": "2023-01-01",
        "pages": 150,
        "cover": "http://example.com/updated-cover.jpg",
        "language": "English"
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == 200
    create_book.refresh_from_db()
    assert create_book.title == "Updated Title"


@pytest.mark.django_db
def test_delete_book(api_client, create_book):
    url = reverse('book-detail', args=[create_book.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert Book.objects.count() == 0


@pytest.mark.django_db
def test_filter_books_by_author(api_client, create_book):
    url = reverse('book-list')
    response = api_client.get(url, {'author': 'Test Author'})
    assert response.status_code == 200
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['author'] == 'Test Author'


@pytest.mark.django_db
def test_filter_books_by_published_date(api_client, create_book):
    url = reverse('book-list')
    response = api_client.get(url, {'published_date': '2023-01-01'})
    assert response.status_code == 200
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['published_date'] == '2023-01-01'


@pytest.mark.django_db
def test_filter_books_by_language(api_client, create_book):
    url = reverse('book-list')
    response = api_client.get(url, {'language': 'English'})
    assert response.status_code == 200
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['language'] == 'English'


@pytest.mark.django_db
def test_pagination(api_client):
    for i in range(15):
        Book.objects.create(
            title=f"Book {i}",
            author="Author",
            isbn=f"12345678901{i:02}",  # Ensure ISBNs are 13 characters long
            published_date="2023-01-01",
            pages=100,
            cover="http://example.com/cover.jpg",
            language="English"
        )
    url = reverse('book-list')
    response = api_client.get(url, {'page': 2})
    assert response.status_code == 200
    assert len(response.data['results']) == 5  # assuming 10 per page
    assert response.data['count'] == 15


@pytest.mark.django_db
def test_invalid_isbn(api_client):
    url = reverse('book-list')
    data = {
        "title": "Invalid Book",
        "author": "Invalid Author",
        "isbn": "invalidisbn",
        "language": "English"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'isbn' in response.data


@pytest.mark.django_db
def test_update_non_existent_book(api_client):
    url = reverse('book-detail', args=[9999])  # Assuming this ID doesn't exist
    data = {
        "title": "Non-existent Book",
        "author": "Non-existent Author",
        "isbn": "1234567890123",
        "published_date": "2023-01-01",
        "pages": 100,
        "cover": "http://example.com/cover.jpg",
        "language": "English"
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_non_existent_book(api_client):
    url = reverse('book-detail', args=[9999])  # Assuming this ID doesn't exist
    response = api_client.delete(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_create_book_with_missing_required_fields(api_client):
    url = reverse('book-list')

    # Test missing title and language
    data = {
        "author": "Author",
        "isbn": "1234567890123"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'title' in response.data
    assert 'language' in response.data

    # Test missing author
    data = {
        "title": "Test Book",
        "isbn": "1234567890123",
        "language": "English"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'author' in response.data

    # Test missing isbn
    data = {
        "title": "Test Book",
        "author": "Author",
        "language": "English"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 400
    assert 'isbn' in response.data
