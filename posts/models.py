from django.db import models
from users.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, related_name='user_posts', verbose_name="Autor", on_delete=models.PROTECT)
    title = models.CharField(verbose_name="Título", max_length=150)
    text = models.TextField(verbose_name="Texto", blank=False)
    post_date = models.TimeField(verbose_name="Data da postagem", auto_now_add=True, editable=False)
    last_edit = models.TimeField(verbose_name="Ultima edição", auto_now=True, editable=False)
    
    def __str__(self):
        return f'"{self.title}", de {self.author}'