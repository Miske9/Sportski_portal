from django.contrib import admin # type: ignore
from .models import *

model_list = [Natjecanje, Tim, Utakmica, Igrac]
admin.site.register(model_list)
