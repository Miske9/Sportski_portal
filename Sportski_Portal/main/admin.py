from django.contrib import admin # type: ignore
from .models import Natjecanje, Tim, Utakmica, Igrac

admin.site.register(Natjecanje)
admin.site.register(Tim)
admin.site.register(Utakmica)
admin.site.register(Igrac)
