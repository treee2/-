from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='Just a test post')

    def test_post_content(self):
        # проверка, что текст поста соответствует ожидаемому значению
        post = Post.objects.get(id=1)
        # проверка, что текст поста равен 'Just a test post'
        expected_object_name = f'{post.text}'
        # сравнение с ожидаемым значением
        self.assertEqual(expected_object_name, 'Just a test post')


class home_pages_view_test(TestCase):

    def setUp(self):
        Post.objects.create(text='это другой тест')

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
       resp = self.client.get(reverse('home'))
       self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
