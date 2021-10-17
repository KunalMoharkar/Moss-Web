from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Blog, Author
from django.contrib.auth.models import User


class BlogTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user('testuser', 'testuser@test.com', 'testpassword')
        author = Author.objects.create(user=user, linked_in ="l", fb ="f", insta="i")
        blog = Blog()
        blog.author = author
        blog.heading = "Test Heading"
        blog.content = "Test Content"
        #blog.image = SimpleUploadedFile(name='test_image.jpg', content=open('C://Users//kumar//Desktop//axis-website//website//accounts//static//accounts//images//img_avatar.png', 'rb').read())
        blog.save()

    
    def test_blog_insertion(self):
        self.assertEqual(Blog.objects.count(), 1)

    def test_list_blogs(self):
        response = self.client.get('/blogs/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['blogs'].count(),1)

    def test_blog_details(self):

        #test response code on valid id
        blog = Blog.objects.get(pk = 1)
        response = self.client.get(f"/blogs/blog/{blog.pk}")
        self.assertEqual(response.status_code,200)

        #chek if error page is being invoked
        response = self.client.get(f"/blogs/blog/2")
        self.assertTemplateUsed(response, 'error.html')





    







