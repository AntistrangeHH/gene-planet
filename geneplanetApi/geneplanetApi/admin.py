from django.contrib import admin
from geneplanetApi.models import Genotype


# registering model to admin.py so I can see changes in admin panel
admin.site.register(Genotype)
