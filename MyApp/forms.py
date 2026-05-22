from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact

        fields = ['name', 'email', 'subject', 'message']

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'w-full h-14 bg-white/5 border border-white/10 rounded-2xl pl-16 pr-5 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500',
                'placeholder': 'Enter your name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'w-full h-14 bg-white/5 border border-white/10 rounded-2xl pl-16 pr-5 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500',
                'placeholder': 'Enter your email'
            }),

            'subject': forms.TextInput(attrs={
                'class': 'w-full h-14 bg-white/5 border border-white/10 rounded-2xl pl-16 pr-5 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500',
                'placeholder': 'Enter subject'
            }),

            'message': forms.Textarea(attrs={
                'class': 'w-full h-40 bg-white/5 border border-white/10 rounded-2xl pl-16 pr-5 pt-5 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500 resize-none',
                'placeholder': 'Write your message'
            }),
        }