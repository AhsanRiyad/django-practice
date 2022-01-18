from .models import MyModel
from django.contrib.admin import AdminSite
from django.contrib import admin
from django.db.models.signals import post_save
# Register your models here.
from .models import Room
from .models import Book
admin.site.register(Room)
admin.site.register(Book)


class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'




def on_risk_assessment_save(sender, instance, **kwargs):
    b = Book()
    b.name = "book1"
    b.save()

# links RiskAssessment saving with the function just above ^
post_save.connect(on_risk_assessment_save, sender=Room)



admin_site = MyAdminSite(name='myadmin')
admin_site.register(MyModel)
