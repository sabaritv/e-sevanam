from django import forms
from django.contrib.auth.forms import UserCreationForm

from manageapp1.models import Login, Goverment, Department


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2',)

# def phone_number_validator(value):
#     if not re.compile(r'^[7-9]\d{9}$').match(value):
#         raise ValidationError('This is Not a Valid Phone Number')


class GovernmentRegister(forms.ModelForm):
    # contact_no = forms.CharField()
    department = forms.ModelChoiceField(queryset=Department.objects.all())

    class Meta:
        model = Goverment
        fields = ('name', 'contact_number', 'email', 'address', 'department')


class DepartmentForm(forms.ModelForm):
    contact_no = forms.CharField()

    class Meta:
        model = Department
        fields = ('name', 'place', 'contact_number', 'email')


