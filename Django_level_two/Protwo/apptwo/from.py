from django import forms
from apptwo.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        field = '__all__'
