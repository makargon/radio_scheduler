from django.conf import settings
from django.db import models
from audio.models import AudioFile, AudioPack


class Schedule(models.Model):
    name = models.CharField(max_length=255)
    audio_file = models.ForeignKey(AudioFile, null=True, blank=True, on_delete=models.CASCADE)
    audio_pack = models.ForeignKey(AudioPack, null=True, blank=True, on_delete=models.CASCADE)
    start_1_time = models.DateTimeField(verbose_name='Первое повторение')
    start_2_time = models.DateTimeField(verbose_name='Второе повторение', null=True, blank=True)
    
    repeat = models.BooleanField()

    еvery_Sun = models.BooleanField(verbose_name='Пн')
    еvery_Mon = models.BooleanField(verbose_name='Вт')
    еvery_Tue = models.BooleanField(verbose_name='Ср')
    еvery_Wed = models.BooleanField(verbose_name='Чт')
    еvery_Thu = models.BooleanField(verbose_name='Пт')
    еvery_Fri = models.BooleanField(verbose_name='Сб')
    еvery_Sat = models.BooleanField(verbose_name='Вс')

    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )


class BlockedPeriod(models.Model):
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()