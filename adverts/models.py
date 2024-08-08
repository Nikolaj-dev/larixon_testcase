from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название города")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Advert(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Город")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    views = models.IntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
