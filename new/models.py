from django.db import models

class table(models.Model):
    name = models.CharField('Название', max_length=100)
    title = models.CharField('Название 2', max_length=100)
    ful_tex = models.TextField('Текст')
    data = models.DateTimeField('Дата публикации')

