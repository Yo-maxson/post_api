from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

# class Typeofletter(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50, null=True, blank=True, default='Отсутствует', verbose_name='Имя CVE')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "Typeofletter"
#         verbose_name = "Тип писем"
#         verbose_name_plural = "Тип письма"


class Letter(models.Model):
    TYPEOFLETTER = (
        ('1', 'письмо,'),
        ('2', 'заказное письмо'),
        ('3', 'ценное письмо'),
        ('4', 'экспресс-письмо'),)

    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=100, verbose_name='ФИО отправиеля')
    recipient = models.CharField(max_length=100, verbose_name='Фио получателя')
    sending = models.CharField(max_length=100, verbose_name='Пункт отправки')
    receiving = models.CharField(max_length=100, verbose_name='Пункт получения')
    senders_index = models.PositiveIntegerField(default=000000, validators=[MinValueValidator(6), MaxValueValidator(6)],
                                                verbose_name='Индекс места отправителя')
    recipients_index = models.PositiveIntegerField(default=000000,
                                                   validators=[MinValueValidator(6), MaxValueValidator(6)],
                                                   verbose_name='Индекс места получателя')
    # type_of_letter = models.ForeignKey(Typeofletter, on_delete=models.CASCADE, verbose_name='Тип письма')
    letter_weight = models.FloatField(default=0, verbose_name='Вес письма')
    typeofletter = models.CharField(max_length=20, choices=TYPEOFLETTER,
                                    verbose_name='Тип письма')

    def __str__(self):
        return self.id

    class Meta:
        db_table = "Letter"
        verbose_name = "Письма"
        verbose_name_plural = "Письмо"


# class Packagetype(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50, default=None, verbose_name='Тип посылки')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "Packagetype"
#         verbose_name = "Тип посылок"
#         verbose_name_plural = "Тип посылки"


class Package(models.Model):
    PACKAGETYPE= (
        ('1', 'мелкий пакет'),
        ('2', 'посылка,'),
        ('3', 'посылка 1 класса'),
        ('4', 'ценная посылка'),
        ('5', 'посылка международная,'),
        ('6', 'экспресс-посылка'),
    )

    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=100, verbose_name='ФИО отправиеля')
    recipient = models.CharField(max_length=100, verbose_name='Фио получателя')
    sending = models.CharField(max_length=100, verbose_name='Пункт отправки')
    receiving = models.CharField(max_length=100, verbose_name='Пункт получения')
    senders_index = models.PositiveIntegerField(default=000000, validators=[MinValueValidator(6), MaxValueValidator(6)],
                                                verbose_name='Индекс места отправителя')
    recipients_index = models.PositiveIntegerField(default=000000,
                                                   validators=[MinValueValidator(6), MaxValueValidator(6)],
                                                   verbose_name='Индекс места получателя')
    # type_of_letter = models.ForeignKey(Typeofletter, on_delete=models.CASCADE, verbose_name='Тип письма')
    package_weight = models.FloatField(default=0, verbose_name='Вес посылки')
    package_type = models.CharField(max_length=20, choices=PACKAGETYPE, verbose_name='Тип посылки')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Package"
        verbose_name = "Посылки"
        verbose_name_plural = "Посылка"
