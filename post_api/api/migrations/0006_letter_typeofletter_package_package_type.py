# Generated by Django 5.1.7 on 2025-03-26 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_packagetype_typeofletter_remove_letter_typeofletter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='typeofletter',
            field=models.CharField(choices=[('письмо', 1), ('заказное письмо', 2), ('ценное письмо', 3), ('экспресс-письмо', 4)], default=None, max_length=20, verbose_name='Тип письма'),
        ),
        migrations.AddField(
            model_name='package',
            name='package_type',
            field=models.CharField(choices=[('мелкий пакет', 'мелкий пакет'), ('посылка', 'посылка'), ('посылка 1 класса', 'посылка 1 класса'), ('ценная посылка', 'ценная посылка'), ('посылка международная', 'посылка международная'), ('экспресс-посылка', 'экспресс-посылка')], default=0, max_length=50, verbose_name='Тип посылки'),
        ),
    ]
