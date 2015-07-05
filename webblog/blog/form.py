# -*- coding:utf-8 -*-
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name')
    subject = forms.CharField(label='Subject', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'iconic user', 'placeholder': 'Hi friend, how may I call you ?'})
        self.fields['subject'].widget.attrs.update({'class' : 'iconic quote-alt', 'placeholder': 'What would you like to talk about?'})
        self.fields['email'].widget.attrs.update({'class' : 'iconic mail-alt', 'placeholder': 'Please enter your email ...'})
        self.fields['message'].widget.attrs.update({'class' : 'iconic comment', 'placeholder': 'Please enter message  ...'})

    def clean_email(self):
        email = self.cleaned_data['email']
        num = len(list(email))
        if num < 10:
            raise forms.ValidationError('Not enough word!!')

        return email