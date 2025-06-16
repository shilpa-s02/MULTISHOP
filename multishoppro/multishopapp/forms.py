from django import forms
from .models import products,ModelRegister

class ProductForm(forms.ModelForm):
    class Meta:
        model= products
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    confirmPassword = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(),max_length=100,required=True)
    class Meta:
        model= ModelRegister
        fields='__all__'
        # widgets = {
        #     'password': forms.PasswordInput(),
        #     'confirmPassword': forms.PasswordInput(),
        # }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if ModelRegister.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_password(self):
        
        password = self.cleaned_data.get('password')
        # confirm_password = self.cleaned_data.get('confirmPassword')

        # if password != confirm_password:
        #     raise forms.ValidationError("password do not match")
        
        if len(password) < 8:
            raise forms.ValidationError("password must be atleast 8 characters long")
        
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('password must contain atleast one character')
        if not any(char.isalpha() for char in password):
            raise forms.ValidationError('password must contain atleast one letter')
        
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirmPassword")
    
        if password and confirm_password and password != confirm_password:
            self.add_error('confirmPassword',"password do not match.")