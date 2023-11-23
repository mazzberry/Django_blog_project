from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your tests here.

class Blog_Post_test(TestCase):

    def setUp(self):
        self.user = User.objects.create(username= 'test-user1')
        self.post1 = Post.objects.create(
            title= 'test title',
            author= self.user ,
            text= 'salam in yek matn test hast',
            status= Post.STATUS_CHOICES[0],
        )

    def test_postlist_url(self):

        response = self.client.get('/blog/')
        self.assertEquals(response.status_code,200)

        pass

    def test_postlist_url(self):

        response = self.client.get('/blog/')
        self.assertEquals(response.status_code,200)

        pass


    def test_postlist_url_byname(self):

        response = self.client.get(reverse('blog-page'))
        self.assertEquals(response.status_code, 200)

        pass

    def test_title_postlist_view(self):
        response = self.client.get(reverse('blog-page'))
        self.assertContains(response, self.post1.title)

    def test_post_detail_on_detail_page(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)





