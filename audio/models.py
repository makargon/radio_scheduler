from django.conf import settings
from django.db import models


class AudioFile(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    file_path = models.FileField(upload_to="media/audio", verbose_name='Файл')
    add_time = models.DateTimeField(verbose_name='Дата добавления')
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    reusable = models.BooleanField(verbose_name='Многоразовый', default=True)

    def __str__(self):
        return f'{self.name}'


class AudioPack(models.Model):
    name = models.CharField(max_length=255)
    audio_list = models.ManyToManyField(AudioFile)
    last_edit = models.DateTimeField(verbose_name='Последнее редактирование')
    last_editor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Последний редактор'
    )

    def __str__(self):
        return f'{self.name} (Тут небольшой список)'