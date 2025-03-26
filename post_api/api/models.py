from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class Typeofletter(models.Model):
    TYPEOFLETTER = (
        (1, 'письмо'),
        (2, 'заказное письмо'),
        (3, 'ценное письмо'),
        (4, 'экспресс-письмо'),)

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
    TYPEOFLETTER = (
        ('письмо', 1),
        ('заказное письмо', 2),
        ('ценное письмо', 3),
        ('экспресс-письмо', 4),)
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
    # type_of_letter = models.ForeignKey(Typeofletter, default=None, on_delete=models.CASCADE, verbose_name='Тип письма')
    letter_weight = models.FloatField(default=0, verbose_name='Вес письма')
    typeofletter = models.CharField(max_length=20, default=None, choices=TYPEOFLETTER, verbose_name='Тип письма')

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
    PACKAGETYPE= (
        ('мелкий пакет', 1),
        ('посылка', 2),
        ('посылка 1 класса', 3),
        ('ценная посылка', 4),
        ('посылка международная', 5),
        ('экспресс-посылка', 6),
    )


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
    # type_of_letter = models.ForeignKey(Packagetype, default=None, on_delete=models.CASCADE, verbose_name='Тип письма')
    package_weight = models.FloatField(default=0,  verbose_name='Вес посылки')
    package_type = models.CharField(max_length=50, default=0, choices=PACKAGETYPE, verbose_name='Тип посылки')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "Package"
        verbose_name = "Посылки"
        verbose_name_plural = "Посылка"
