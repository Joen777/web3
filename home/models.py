from django.db import models

class Comment(models.Model):
    name = models.CharField("Имя", max_length=100)
    tittle = models.TextField('Текст')

