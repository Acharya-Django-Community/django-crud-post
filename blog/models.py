from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    