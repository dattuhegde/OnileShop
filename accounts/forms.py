from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_staff')
        widgets = {'is_staff': forms.HiddenInput()}

    def save(self, commit=True):
        user = super(NewForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        self.fields['is_staff'].widget = forms.HiddenInput()
        if commit:
            user.save()
        return user

