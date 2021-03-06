from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField, DateField, IntegerField, TextField, TimeField, DateTimeField
from django.urls import reverse


class Day(models.Model):
    title = DateField(verbose_name='День') # день недели

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'
        ordering = ['title'] # сортировка по дате дня


class Lesson(models.Model): # все записи на уроки
    pupil_name = CharField(max_length=20, verbose_name='Имя') # имя студента
    pupil_surname = CharField(max_length=20, verbose_name='Фамилия', blank=True) # фамилия студента (необязательно)
    pupils_father = CharField(max_length=20, verbose_name='Отчество', blank=True) # отчество студента (необязательно)
    theme = CharField(max_length=30, verbose_name='Тема', blank=True) # тема урока (необязательно)
    note = TextField(verbose_name='Примечание', blank=True) # примечение (необязательно)
    created_at = DateTimeField(auto_now_add=True, verbose_name='Было создано') # дата создания записи (автоматическая)
    salary = IntegerField(default=700, verbose_name='Зарплата') # зарплата (по умолчанию = 700)
    time = TimeField(verbose_name='Время') # время урока
    date = models.ForeignKey(Day, on_delete=models.PROTECT, related_name='lessons') # ключ к таблице дней. При удалении дня удалаются все его записи

    class Meta:
        verbose_name = 'Урок' # название в админке
        verbose_name_plural = 'Уроки' # название в админке
        ordering = ['time'] # сортировка по умолчанию по дате создания

    def __str__(self):
        return self.pupil_name

    def get_absolute_url(self):
        return reverse('lesson', kwargs={'pk':self.pk}) # для открывания конкретной записи

