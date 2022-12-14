from django import forms
from .models import Account, UserProfile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control',
    }))

    first_name = forms.CharField( widget=forms.TextInput(attrs={
        'placeholder':'Enter First Name',
        'class':'form-control'})
    )
    last_name = forms.CharField( widget=forms.TextInput(attrs={
        'placeholder':'Enter last Name',
        'class':'form-control'})
    )
    phone_number = forms.CharField( widget=forms.TextInput(attrs={
        'placeholder':'Enter Phone Number',
        'class':'form-control'})
    )
    email = forms.CharField( widget=forms.EmailInput(attrs={
        'placeholder':'Enter Email Address',
        'class':'form-control'})
    )

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def clean(self):
        # cleaned_data = super(RegistrationForm, self).clean()
        # password = cleaned_data.get('password')
        # confirm_password = cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )


class UserForm(forms.ModelForm):
    first_name = forms.CharField( widget=forms.TextInput(attrs={
        'class':'form-control'})
    )
    last_name = forms.CharField( widget=forms.TextInput(attrs={
        'class':'form-control'})
    )
    phone_number = forms.CharField( widget=forms.TextInput(attrs={
        'class':'form-control'})
    )
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)

    address_line_1 = forms.CharField( widget=forms.TextInput(attrs={
        'class':'form-control'})
    )
    address_line_2 = forms.CharField( widget=forms.TextInput(attrs={
        'class':'form-control'})
    )
    city = forms.CharField( widget=forms.TextInput(attrs={
        'class':'form-control'})
    )
    state = forms.CharField( widget=forms.TextInput(attrs={
        'class':'form-control'})
    )
    country = forms.CharField( widget=forms.TextInput(attrs={
        'class':'form-control'})
    )

    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture')
