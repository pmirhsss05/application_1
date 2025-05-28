# import datetime
from django.db import models


class Model_X(models.Model):
    task = models.CharField(
        verbose_name="Формулировка",
        default="Дано вещественное число. Определить, какое это число: положительное, отрицательное, ноль.",
        max_length=255,
    )
    x = models.IntegerField(
        verbose_name="Значение X",
        default=0,
    )

    result = models.CharField(
        verbose_name="Ответ",
        default="Ответ",
        max_length=255,
    )
    current_date = models.DateTimeField(
        verbose_name="Дата изменения(save)", auto_now=True
    )

    def __str__(self):
        return f"self.task:{self.task}"

    class Meta:
        verbose_name = " Таблица результатов"
        verbose_name_plural = "Таблицы результатов"
        ordering = ("-pk", )


