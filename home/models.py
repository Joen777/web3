from django.db import models

class Comment(models.Model):#Коментарии
    name = models.CharField("Имя", max_length=100)
    tittle = models.TextField('Текст')


class Feedback(models.Model):#Обратная связь
    feed_email = models.TextField("email для обратной связи")

    def __str__(self):
        return self.feed_email

