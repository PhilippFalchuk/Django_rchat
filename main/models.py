from django.db import models


class Messages(models.Model):
    name = models.CharField('Имя', max_length=50)
    message = models.TextField("Сообщение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class NewTable(models.Model):
    upperfield = models.CharField('верхнее поле', max_length=50)
    lowerfield = models.TextField("нижнее поле")

    def __str__(self):
        return self.upperfield
