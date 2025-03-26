from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class Typeofletter(models.Model):
    TYPEOFLETTER = (
        ('письмо', 'письмо'),
        ('заказное письмо', 'заказное письмо'),
        ('ценное письмо', 'ценное письмо'),
        ('экспресс-письмо', 'экспресс-письмо'),)

    id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=50, null=True, blank=True, default='Отсутствует', verbose_name='Имя CVE')
    name = models.CharField(max_length=20, choices=TYPEOFLETTER, verbose_name='Тип письма')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Typeofletter"
        verbose_name = "Тип писем"
        verbose_name_plural = "Тип письма"


class Packagetype(models.Model):
    PACKAGETYPE= (
        ('мелкий пакет', 'мелкий пакет'),
        ('посылка', 'посылка'),
        ('посылка 1 класса', 'посылка 1 класса'),
        ('ценная посылка', 'ценная посылка'),
        ('посылка международная', 'посылка международная'),
        ('экспресс-посылка', 'экспресс-посылка'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, choices=PACKAGETYPE, verbose_name='Тип посылки')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Packagetype"
        verbose_name = "Тип посылок"
        verbose_name_plural = "Тип посылки"


class Letter(models.Model):

    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=100, verbose_name='ФИО отправиеля')
    recipient = models.CharField(max_length=100, verbose_name='Фио получателя')
    sending = models.CharField(max_length=100, verbose_name='Пункт отправки')
    receiving = models.CharField(max_length=100, verbose_name='Пункт получения')
    senders_index = models.PositiveIntegerField(default=0, validators=[MinValueValidator(999), MaxValueValidator(999999)],
                                                verbose_name='Индекс места отправителя')
    recipients_index = models.PositiveIntegerField(default=0,
                                                   validators=[MinValueValidator(999), MaxValueValidator(999999)],
                                                   verbose_name='Индекс места получателя')
    type_of_letter = models.ForeignKey(Typeofletter, null= True, on_delete=models.CASCADE, verbose_name='Тип письма')
    letter_weight = models.FloatField(default=0, verbose_name='Вес письма')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "Letter"
        verbose_name = "Письма"
        verbose_name_plural = "Письмо"


class Packagetype(models.Model):
    PACKAGETYPE= (
        ('мелкий пакет', 'мелкий пакет'),
        ('посылка', 'посылка'),
        ('посылка 1 класса', 'посылка 1 класса'),
        ('ценная посылка', 'ценная посылка'),
        ('посылка международная', 'посылка международная'),
        ('экспресс-посылка', 'экспресс-посылка'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, choices=PACKAGETYPE, verbose_name='Тип посылки')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Packagetype"
        verbose_name = "Тип посылок"
        verbose_name_plural = "Тип посылки"


class Package(models.Model):



    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=100, verbose_name='ФИО отправиеля')
    recipient = models.CharField(max_length=100, verbose_name='Фио получателя')
    sending = models.CharField(max_length=100, verbose_name='Пункт отправки')
    receiving = models.CharField(max_length=100, verbose_name='Пункт получения')
    senders_index = models.PositiveIntegerField(default=000000, validators=[MinValueValidator(999), MaxValueValidator(999999)],
                                                verbose_name='Индекс места отправителя')
    recipients_index = models.PositiveIntegerField(default=000000,
                                                   validators=[MinValueValidator(999), MaxValueValidator(999999)],
                                                   verbose_name='Индекс места получателя')
    package_type = models.ForeignKey(Packagetype, null=True, on_delete=models.CASCADE, verbose_name='Тип письма')
    package_weight = models.FloatField(default=0,  verbose_name='Вес посылки')


    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "Package"
        verbose_name = "Посылки"
        verbose_name_plural = "Посылка"
