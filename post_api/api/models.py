from django.db import models


class Typeofletter(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Тип письма')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Typeofletter"
        verbose_name = "Тип письма"
        verbose_name_plural = "Тип писем"


class Packagetype(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,  verbose_name='Тип посылки')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Packagetype"
        verbose_name = "Тип посылки"
        verbose_name_plural = "Тип посылок"


class Letter(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=100, verbose_name='ФИО отправиеля')
    recipient = models.CharField(max_length=100, verbose_name='Фио получателя')
    sending = models.CharField(max_length=100, verbose_name='Пункт отправки')
    receiving = models.CharField(max_length=100, verbose_name='Пункт получения')
    senders_index = models.CharField(max_length=6, verbose_name='Индекс места отправителя')
    recipients_index = models.CharField(max_length=6, verbose_name='Индекс места получателя')
    type_of_letter = models.ForeignKey(Typeofletter, null=True, on_delete=models.CASCADE, verbose_name='Тип письма')
    letter_weight = models.FloatField(default=0, verbose_name='Вес письма')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "Letter"
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"



class Package(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=100, verbose_name='ФИО отправиеля')
    recipient = models.CharField(max_length=100, verbose_name='Фио получателя')
    sending = models.CharField(max_length=100, verbose_name='Пункт отправки')
    receiving = models.CharField(max_length=100, verbose_name='Пункт получения')
    senders_index = models.CharField(max_length=6, verbose_name='Индекс места отправителя')
    recipients_index = models.CharField(max_length=6, verbose_name='Индекс места получателя')
    package_type = models.ForeignKey(Packagetype, null=True, on_delete=models.CASCADE, verbose_name='Тип письма')
    package_weight = models.FloatField(default=0, verbose_name='Вес посылки')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "Package"
        verbose_name = "Посылка"
        verbose_name_plural = "Посылки"
