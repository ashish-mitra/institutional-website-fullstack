from django import forms
from .models import Student
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from .models import Student

class registration_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'dob', 'email', 'phone', 'gender', 'branch', 'passing_year', 'percentage','school', 'school_district', 'admit_card', 'marksheet', 'street', 'village', 'state', 'district', 'block', 'pin')