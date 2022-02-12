from django.db import models
from django.template.defaultfilters import slugify # new
from django.contrib.auth.models import User
from django_lifecycle import LifecycleModel, hook, BEFORE_SAVE, BEFORE_UPDATE
from .utils import get_random_code


class Category(LifecycleModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)

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
        ex = False
        to_slug = slugify(self.name)
        ex = Category.objects.filter(slug=to_slug).exists()
        
        while ex:
            to_slug = slugify(to_slug + ' ' + str(get_random_code()))
            ex = Category.objects.filter(slug=to_slug).exists()

        self.slug = to_slug
    
    @hook(BEFORE_SAVE, when='name', has_changed=True)
    def on_title_create(self):
        ex = False
        to_slug = slugify(self.name)
        ex = Category.objects.filter(slug=to_slug).exists()
        
        while ex:
            to_slug = slugify(to_slug + ' ' + str(get_random_code()))
            ex = Category.objects.filter(slug=to_slug).exists()
            
        self.slug = to_slug
    


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/', blank=True, default='no-image.jpg')
    slug = models.SlugField(unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-id']
        

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'

    @hook(BEFORE_UPDATE, when='title', has_changed=True)
    def on_title_change(self):
        ex = False
        to_slug = slugify(self.name)
        ex = Post.objects.filter(slug=to_slug).exists()
        
        while ex:
            to_slug = slugify(to_slug + ' ' + str(get_random_code()))
            ex = Category.objects.filter(slug=to_slug).exists()

        self.slug = to_slug
    
    @hook(BEFORE_SAVE, when='title', has_changed=True)
    def on_title_create(self):
        ex = False
        to_slug = slugify(self.name)
        ex = Post.objects.filter(slug=to_slug).exists()
        
        while ex:
            to_slug = slugify(to_slug + ' ' + str(get_random_code()))
            ex = Category.objects.filter(slug=to_slug).exists()

        self.slug = to_slug
    