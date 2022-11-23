from django.contrib import admin
from .models import Catogory, Cluster,Competition, Unit, Result
# Register your models here.
admin.site.register(Cluster)
admin.site.register(Unit)
admin.site.register(Catogory)
admin.site.register(Competition)
admin.site.register(Result)