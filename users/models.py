from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(verbose_name="Nome de usuário", max_length=50, unique=True)
    email = models.EmailField(verbose_name="E-mail", max_length=150, unique=True)
    password = models.CharField(verbose_name="Senha", max_length=50)
    first_name = models.CharField(editable=False, max_length=10)
    last_name = models.CharField(editable=False, max_length=10)
    is_staff = models.BooleanField(default=True, editable=False)
    is_superuser = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.username