from django.contrib import admin
from .models import *


class Letter_det(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'sending', 'receiving', 'senders_index', 'recipients_index',
                    'letter_weight', 'type_of_letter')


class Package_det(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'sending', 'receiving', 'senders_index', 'recipients_index',
                    'package_weight', 'package_type')


class Typeofletter_det(admin.ModelAdmin):
    list_display = ('id', 'name')


class Packagetype_det(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Letter, Letter_det)
admin.site.register(Package, Package_det)
admin.site.register(Typeofletter, Typeofletter_det)
admin.site.register(Packagetype, Packagetype_det)
