from django.db import models

# Create your models here.
from django.db.models import CharField, IntegerField, FileField, ForeignKey, TextField, DateField


class Home(models.Model):
    home_name = CharField(max_length=100)
    home_location = CharField(max_length=255)
    home_address = CharField(max_length=255)
    home_rent = IntegerField()
    home_floor = CharField(max_length=20)
    home_painting_money = IntegerField()

    def __str__(self):
        return '%s %s ' % (self.home_name, self.home_location)


class Tenent(models.Model):
    tenent_name = CharField(max_length=200)
    tenent_start_date = DateField()
    tenent_end_date = DateField()
    tenent_home_id = ForeignKey(Home, on_delete=models.CASCADE)
    tenent_advance = IntegerField()
    tenent_note = TextField(max_length=500)

    def __str__(self):
        return '%s %s ' % (self.tenent_name, self.tenent_note)


class Rent(models.Model):

    rent_tenent_id = ForeignKey(Tenent, on_delete=models.CASCADE)
    rent_month_year = DateField()
    rent_recived_date = DateField()
    rent_amount = IntegerField()

    def __str__(self):
        return '%s %s' % (self.rent_tenent_id, self.rent_month_year)


class Document(models.Model):
    document_type = TextField(max_length=30)
    document_tenant = ForeignKey(Tenent, on_delete=models.CASCADE)
    document_upload = FileField(upload_to='media')

    def __str__(self):
        return f"{self.document_tenant.tenent_name}"