from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
# Create your models here.

def translit_to_eng(s: str) -> str:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}
    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))
class Underground(models.Model):
    def save(self, *args, **kwargs):
        self.page_name = translit_to_eng(self.animal)
        super().save(*args, **kwargs)
    class Status(models.IntegerChoices):
        USUAL = 0, 'Распространенное'
        RARE = 1, 'Редкое'
    class Meta:
        verbose_name = 'Подземные обитатели'
        verbose_name_plural = 'Подземные обитатели'
    # Название страницы с животным
    page_name = models.CharField(max_length=255,default='underground',verbose_name="Слаг")
    # Название животного
    animal = models.CharField(max_length=255,verbose_name="Имя животного")
    # Информация о животном
    content = models.TextField(blank=True,verbose_name="Текст о животном")
    # Время создания страницы о животном
    time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
    # Время обновления информации о животном
    time_update = models.DateTimeField(auto_now=True,verbose_name="Время изменения")
    # Занесено ли животное в красную книгу
    is_red_book = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                      default=Status.USUAL, verbose_name="Красная книга")
    # Класс животного
    class_of_animal = models.ForeignKey('Underground_Kinds', on_delete=models.PROTECT, null=True,
                                        verbose_name="Класс животного")
    # Особенность животного
    unique_fact = models.OneToOneField('Underground_Facts', on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='fact', verbose_name="Факт о животном")
    # Теги
    tags = models.ManyToManyField('UndergroundTags', blank=True, related_name='tags',verbose_name="Теги")
    # Фото животного
    image = models.ImageField(upload_to="images/%Y/%m/%d/", default=None, blank=True, null=True,
                              verbose_name="Изображение")
    # Автор статьи
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None)
class UndergroundTags(models.Model):
    tag = models.CharField(max_length=100, db_index=True, verbose_name="Теги")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag
    def get_absolute_url(self):
        return reverse('tag', kwargs={'underground_tag_slug':self.slug})

class Underground_Facts(models.Model):
    content = models.TextField(blank=True)
    class Meta:
        verbose_name = 'Интересный факт'
        verbose_name_plural = 'Интересный факт'

class Underground_Kinds(models.Model):
    # Имя класса
    name = models.CharField(max_length=50, db_index=True, verbose_name="Класс")
    # Имя страницы
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name


class UploadImage(models.Model):
    # Заголовок изображения
    caption = models.CharField(max_length=255)
    # Изображение
    photo = models.ImageField(upload_to='underground/static/images')
