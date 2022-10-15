from django.db import models


class Ads(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=150)
    author = models.CharField(verbose_name='Автор',
                              max_length=150)
    price = models.DecimalField(verbose_name='Цена',
                                max_digits=10,
                                decimal_places=2)
    description = models.TextField(verbose_name='Описание',
                                   max_length=1000,
                                   help_text='Полное описание 1000 символов максимум!')
    address = models.CharField(verbose_name='Адрес',
                               max_length=250)
    is_published = models.BooleanField(verbose_name='Активно',
                                       default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Category(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=150)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
