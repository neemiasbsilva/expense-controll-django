from django.contrib import admin
from .models import Category
from .models import Transactions
# Register your models here.

admin.site.register(Category)
admin.site.register(Transactions)
