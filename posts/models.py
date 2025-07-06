from django.db import models
# этот файл определяет модель Post, которая будет использоваться для создания таблицы в базе данных
# модель Post содержит одно поле text, которое представляет собой текстовое поле
# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        '''строковое представление модели Post'''
        return self.text[:50]