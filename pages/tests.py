from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your tests here.

class Blog_Post_test(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='test-user1')
        cls.post1 = Post.objects.create(
            title= 'test title',
            author = cls.user,
            text= 'salam in yek matn test hast',
            status= Post.STATUS_CHOICES[0][0],  # published
        )
        cls.post2 = Post.objects.create(
            title='post2 draft',
            author=cls.user,
            text='lorem impsum post2',
            status=Post.STATUS_CHOICES[1][0],  # draft
        )

    # def setUp(self):
    #     self.user = User.objects.create(username= 'test-user1')
    #     self.post1 = Post.objects.create(
    #         title= 'test title',
    #         author= self.user ,
    #         text= 'salam in yek matn test hast',
    #         status= Post.STATUS_CHOICES[0][0],#published
    #     )
    #     self.post2 = Post.objects.create(
    #         title = 'post2 draft',
    #         author = self.user,
    #         text = 'lorem impsum post2',
    #         status = Post.STATUS_CHOICES[1][0],#draft
    #     )

    def test_post_model_str(self):
        post = self.post1
        self.assertEquals(str(post), post.title)

    def test_post_detail(self):
        self.assertEquals(self.post1.title, 'test title')
        self.assertEquals(self.post1.text, 'salam in yek matn test hast')



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


    def test_postdetail_url_byname(self):

        response = self.client.get(reverse('post-detail', args= [self.post1.id] ))
        self.assertEquals(response.status_code, 200)

    def test_404_if_does_n_exist(self):
        response = self.client.get(reverse('post-detail', args=[99999999999999]))
        self.assertEquals(response.status_code, 404)

    def test_draft_post_not_show_postlist(self):# TDD - test driven development
        response = self.client.get(reverse('blog-page'))
        self.assertContains(response,self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_create_post_view(self):
        response= self.client.post(reverse('new-post'),{
            'title':'some title',
            'text':'some test text',
            'status':'pub',
            'author':self.user.id,
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.last().title, 'some title')
        self.assertEquals(Post.objects.last().text, 'some test text')

    def test_update_post_view(self):
        response= self.client.post(reverse('update-post', args=[self.post2.id]), {
            'title':' post 2 some title updated ',
            'text':'this text updated',
            'status': 'pub',
            'author': self.post2.author.id,
             })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.last().title, 'post 2 some title updated')
        self.assertEquals(Post.objects.last().text, 'this text updated')

    def test_delete_post_view(self):
        response = self.client.post(reverse('delete-post',args=[self.post1.id]))
        self.assertEquals(response.status_code, 302)

