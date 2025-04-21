from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(verbose_name=_("Category URL"), max_length=250, unique=True, primary_key=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug


class Material(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=2555, null=True, blank=True)
    slug = models.SlugField(verbose_name=_("Material URL"), max_length=250, unique=True, primary_key=True)
    category = models.ForeignKey(Category, null=True, related_name="material", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Snippet(models.Model):
    text = models.TextField(max_length=9990, null=True, blank=True)
    code = models.TextField(max_length=9990, null=True, blank=True)
    image = models.FileField(upload_to='imagefolder/', null=True, blank=False)
    material = models.ForeignKey(Material, null=True, related_name="material_snippet", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

