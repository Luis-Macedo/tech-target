from django.contrib import admin
from .models import *


admin.site.register(Question_type)
admin.site.register(Form)
admin.site.register(Question)
admin.site.register(User_answer)

