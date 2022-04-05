from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models
from django.template.defaultfilters import slugify # new
from django.contrib.auth.models import User
from django_lifecycle import LifecycleModel, hook, BEFORE_SAVE, BEFORE_UPDATE
from .utils import get_random_code
from sorl.thumbnail import get_thumbnail

class Category(LifecycleModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    

    @hook(BEFORE_UPDATE, when='name', has_changed=True)
    def on_title_change(self):
        to_slug = slugify(self.name)
        self.slug = to_slug
    
    @hook(BEFORE_SAVE, when='name', has_changed=True)
    def on_title_create(self):
        to_slug = slugify(self.name)
        self.slug = to_slug
    


class Post(LifecycleModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/', blank=True, default='no-image.jpg')
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="posts-thumbnail/", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    class Meta:
        ordering = ['-id']

    @hook(BEFORE_UPDATE, when='title', has_changed=True)
    def on_title_change(self):
        ex = False
        to_slug = slugify(str(self.title))
        ex = Post.objects.filter(slug=to_slug).exists()

        while ex:
            to_slug = slugify(to_slug + ' ' + str(get_random_code()))
            ex = Post.objects.filter(slug=to_slug).exists()
        
        self.slug = to_slug
    
    

    @hook(BEFORE_SAVE, when='title', has_changed=True)
    def on_title_create(self):
        ex = False
        to_slug = slugify(str(self.title))
        ex = Post.objects.filter(slug=to_slug).exists()
        print(ex)

        while ex:
            to_slug = slugify(to_slug + ' ' + str(get_random_code()))
            ex = Post.objects.filter(slug=to_slug).exists()
        
        self.slug = to_slug
    
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()

            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else: 
            return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

LIKE_CHOISES = (
    ('Like', 'Like'),
    ('UnLike', 'UnLike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userlikes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postlikes')
    status = models.CharField(choices=LIKE_CHOISES, max_length=8)

    def __str__(self):
        return f'{self.user}-{self.post}'