from django.db import models

# Create your models here.

# classe herdada de Model
class Musician(models.Model):

    # dados da classe e tipos    (nome exibido na interface, outros parametros proprios do tipo)
    first_name = models.CharField(verbose_name="Primeiro nome", max_length=15)
    last_name = models.CharField(verbose_name="Ultimo nome", max_length=15)
    instrument = models.CharField(verbose_name="Instrumento", max_length=20)

    # como cada instancia eh exibida na interface
    def __str__(self):
        return f'Nome: {self.first_name} / Instrumento: {self.instrument}'

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.PROTECT)
    name = models.CharField(verbose_name = "Nome", max_length=50)
    date = models.DateField(verbose_name = "Data de lançamento", auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'Nome: {self.name}'
    