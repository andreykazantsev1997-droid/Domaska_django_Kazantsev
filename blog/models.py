from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(upload_to="blog/", verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publication_indicator = models.BooleanField(default=True, verbose_name="Признак публикации")
    count_view = models.IntegerField(default=0, verbose_name="Количество просмотров")
