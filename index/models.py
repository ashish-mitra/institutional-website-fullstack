from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, default=None , null=True)
    dob = models.PositiveIntegerField(default=None, blank=True)
    email = models.EmailField(max_length=200, default=None, blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    gender = models.CharField(max_length=10, default=None, blank=True)
    branch = models.CharField(max_length=50, default=None, blank=True)
    passing_year = models.PositiveIntegerField(default=None, blank=True)
    percentage = models.PositiveIntegerField(default=None, blank=True)
    school = models.CharField(max_length=200, default=None, blank=True)
    school_district = models.CharField(max_length=50, default=None, blank=True)
    admit_card = models.ImageField(upload_to='admitcard/', default=None, null=True, blank=True)
    marksheet = models.ImageField(upload_to='marksheet/', default=None, null=True, blank=True)
    street = models.CharField(max_length=20, default=None, null=True, blank=True)
    village = models.CharField(max_length=60, default=None, blank=True)
    state = models.CharField(max_length=20, default=None, blank=True)
    district = models.CharField(max_length=20, default=None, blank=True)
    block = models.PositiveIntegerField(default=None, blank=True)
    pin = models.CharField(max_length=7, default=None, blank=True)  
    class Meta:
        db_table = "Student_table"

    def __str__(self):
        return self.name
