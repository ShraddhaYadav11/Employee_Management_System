


from django import forms
from .models import Login
from .models import Add

class EmployeeLogin(forms.ModelForm):
    class Meta:
        model=Login

        fields=['name','password','email']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),

            'password':forms.PasswordInput(attrs={'class':'form-control'}),

            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class EmployeeAdd(forms.ModelForm):
    class Meta:
        model=Add

        fields=['FirstName','MiddelName','LastName','Password','Email','Phone','Address']

        widgets={
            'FirstName':forms.TextInput(attrs={'class':'form-control'}),

            'MiddelName':forms.TextInput(attrs={'class':'form-control'}),

            'LastName':forms.TextInput(attrs={'class':'form-control'}),

            'Password':forms.PasswordInput( render_value=True, attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Phone':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
        }