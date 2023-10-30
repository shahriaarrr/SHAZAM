from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from .models import Thunder, Profile

class ThunderForm(forms.ModelForm):
    class Meta:
        model = Thunder
        fields = ('text',)  # Connect the 'text' field in the model to the form

    text = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'placeholder': "Strike your thunder here...",
                "class": "form-control",
            }
        ),
        label="",
    )

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email Address'
        }
    ))
    first_name = forms.CharField(label="", max_length=100,  widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First name'
        }
    ))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last name'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class UserUpdateForm(BaseUserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label="profile img")
    bio = forms.CharField(label="bio", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'tell us about yourself :)'
        }
    ))
    website = forms.CharField(label="website", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'https://example.domain'
        }
    ))
    social_instagram = forms.CharField(label="instagram", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'your instagram username without @'
        }
    ))
    social_steam = forms.CharField(label="steam", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'steam username'
        }
    ))
    social_github = forms.CharField(label="steam", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'github username'
        }
    ))
    social_linkedin = forms.CharField(label="linkedin", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'example: https://linkedin.com/in/<username>'
        }
    ))

    class Meta:
        model = Profile
        fields = (
            "profile_image",
            "bio",
            "website",
            "social_instagram",
            "social_steam",
            "social_github",
            "social_linkedin",
        )
