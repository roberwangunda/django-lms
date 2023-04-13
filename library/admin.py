from django.contrib import admin
from library import models

# Register your models here.
admin.site.register(models.SubCategory)
admin.site.register(models.Books)
admin.site.register(models.Category)
admin.site.register(models.Students)
# admin.site.register(models.Borrow)
# admin.site.register(models.BorrowProfile)