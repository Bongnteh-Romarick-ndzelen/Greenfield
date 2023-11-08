from django import forms
from .models import Contact, LiveChat
from django.core.validators import RegexValidator

#Every letter to lowercase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()

#Capitalized the first letter of each word
class Capitalized(forms.CharField):
    def to_python(self, value):
        return value.title()

class ContactForm(forms.ModelForm):

    #VALIDATION
    name = Capitalized(
        label='Name',min_length=5,max_length=200,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$',
        message = "Only letters are allowed")],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name...'})
    )
    email = Lowercase(
        label='Email Address',min_length=10,max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message = "Put a valid email address"
        )],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your Email Address...'}),
        required=False
    )
    number = forms.CharField(
        label='Number',min_length=5,max_length=50,
        validators=[RegexValidator(r'[^[0-9]*$',
        message = "Only numbers are allowed!"
        )],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone Number...'})
    )
    subject = Capitalized(
        label='Subject',min_length=5,max_length=200,
        validators=[RegexValidator(r'^[a-zA-Z\s.-_]*$',
        message = "Only letters are allowed!")],
        widget=forms.TextInput(attrs={'placeholder': 'Subject....'}),
        required=False
    )
    message = forms.CharField(
        label='message',min_length=20, max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Type a Message', 'rows':4})
    )
    class Meta:
        model = Contact
        fields = "__all__"


class LiveChatForm(forms.ModelForm):
    #VALIDATION
    name = forms.CharField(
        label='Name',min_length=5,max_length=200,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$',
        message = "Only letters are allowed")],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name...'}),
        required=False
    )
    number = forms.CharField(
        label='Number',min_length=5,max_length=50,
        validators=[RegexValidator(r'[^[0-9]*$',
        message = "Only numbers are allowed!"
        )],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone Number...'})
    )
    message = forms.CharField(
        label='message',min_length=10, max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Type a Message', 'rows':3}),
        required=False
    )
    class Meta:
        model = LiveChat
        fields = "__all__"