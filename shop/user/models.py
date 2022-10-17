from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class UserModel(AbstractUser):
    username = models.CharField(max_length=15, unique=True, verbose_name='Логін')
    slug = models.SlugField(max_length=15, )
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='Вік')
    cash = models.PositiveIntegerField(null=False, default=10000)

    class Meta:
        db_table = 'auth_user'
        verbose_name = "user"
        verbose_name_plural = "users"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)
