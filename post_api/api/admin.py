from django.contrib import admin
from .models import *


# Register your models here.

class Letter_det(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'sending', 'receiving', 'senders_index', 'recipients_index',
                    'letter_weight', 'typeofletter')


class Package_det(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'sending', 'receiving', 'senders_index', 'recipients_index',
                    'package_weight', 'package_type')


admin.site.register(Letter, Letter_det)
admin.site.register(Package, Package_det)
admin.site.register(Typeofletter)
admin.site.register(Packagetype)
