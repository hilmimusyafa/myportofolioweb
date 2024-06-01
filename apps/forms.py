from django import forms
from django.db import models

class ContactForm(forms.Form):
    name = forms.CharField(label='Name :',widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    email = forms.EmailField(label='Email :',widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    title = forms.CharField(label='Message Title :',widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}))
    message = forms.CharField(label='Message :',widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control'}))
