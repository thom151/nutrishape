from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Goal)
admin.site.register(ActivityLevel)
admin.site.register(Sex)
admin.site.register(DailyCalorie)
admin.site.register(Thread)

