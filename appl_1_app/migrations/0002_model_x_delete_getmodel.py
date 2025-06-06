# Generated by Django 4.1.7 on 2025-05-16 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl_1_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_X',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='Дано вещественное число. Определить, какое это число: положительное, отрицательное, ноль.', max_length=255, verbose_name='Формулировка')),
                ('x', models.IntegerField(default=0, verbose_name='Значение X')),
                ('result', models.CharField(default='Ответ', max_length=255, verbose_name='Ответ')),
                ('current_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения(save)')),
            ],
            options={
                'verbose_name': ' Таблица результатов',
                'verbose_name_plural': 'Таблицы результатов',
                'ordering': ('-pk',),
            },
        ),
        migrations.DeleteModel(
            name='getModel',
        ),
    ]
