from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.conf import settings
from .validators import (
    validate_category,
    validate_name, 
)

# Create your models here.

class myprojects(models.Model):
    name                   = models.CharField(max_length=120, blank=True, null=False)
    imageorganization      = models.ImageField(upload_to='images/organization')
    image                  = models.ImageField(upload_to='images/projects')
    organization           = models.CharField(max_length=120, blank=True, null=False)
    year                   = models.CharField(max_length=120, blank=True, null=False)
    description            = models.TextField(blank=True, null=True)
    slug                   = models.SlugField(unique=True, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('name:detail', kwargs={'slug': self.slug})
        
    def get_description(self):
        return self.description.split(",")

    # def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    #     instance.category = instance.category.capitalize()
    #     if not instance.slug:
    #         instance.slug = unique_slug_generator(instance)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    title = models.CharField(max_length=255)
    message = models.TextField()