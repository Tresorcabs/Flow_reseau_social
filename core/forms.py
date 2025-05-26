from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField( required=True )

    class Meta:  # Classe qui permet de personnaliser le formulaire
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring focus:border-blue-500',
                'placeholder': field.label
            })

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']

        widgets = {
            'content' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'Quoi de neuf ?', 'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'}),
        }