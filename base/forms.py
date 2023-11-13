from django import forms
from .models import Contact, LiveChat, Comment
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
        widget=forms.TextInput(attrs={
                                        'placeholder': 'Enter your name...',
                                        'style': 'margin-top: auto, margin-bottom: auto,padding:0',
                                        }
                                )
    )
    email = Lowercase(
        label='Email Address',min_length=10,max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message = "Put a valid email address"
        )],
        widget=forms.TextInput(attrs={
                                        'placeholder': 'Enter your Email Address...',
                                        'style': 'margin-top: auto, margin-bottom: auto,padding:0',
                                    }
                                ),
        required=False
    )
    number = forms.CharField(
        label='Number',min_length=5,max_length=50,
        validators=[RegexValidator(r'[^[0-9]*$',
        message = "Only numbers are allowed!"
        )],
        widget=forms.TextInput(attrs={
                                        'placeholder': 'Enter your phone Number...',
                                        'style': 'margin-top: auto, margin-bottom: auto,padding:0',
                                        }
                                )
    )
    subject = Capitalized(
        label='Subject',min_length=5,max_length=200,
        validators=[RegexValidator(r'^[a-zA-Z\s.-_]*$',
        message = "Only letters are allowed!")],
        widget=forms.TextInput(attrs={
                                        'placeholder': 'Subject....',
                                        'style': 'margin-top: auto, margin-bottom: auto,padding:0',
                                        }
                                ),
        required=False
    )
    message = forms.CharField(
        label='message',min_length=20, max_length=1000,
        widget=forms.Textarea(attrs={
                                        'placeholder': 'Type a Message',
                                        'style': 'margin-top: auto, margin-bottom: auto,padding:0',
                                        'rows':4
                                    }
                            )
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
        label='Comment',min_length=20, max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Type a Message', 'rows':4})
    )
    class Meta:
        model = LiveChat
        fields = "__all__"

class CommentForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',min_length=5,max_length=200,
        validators=[RegexValidator(r'^[a-zA-Z\s]*$',
        message = "Only letters are allowed")],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name...', 'style':'background-color:#B4E8DAEF', 'color':'#000','margin-top':1,'margin-bottom':1})
    )
    email = forms.CharField(
        label='Email Address',min_length=10,max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message = "Put a valid email address"
        )],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your Email Address...','style':'background-color:#B4E8DAEF', 'color':'#000','margin-top':1,'margin-bottom':1}),
        required=False
    )
    comment = forms.CharField(
        label='Comment',min_length=20, max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Type a Comment', 'rows':4,'style':'background-color:#B4E8DAEF', 'color':'#000','margin-top':1,'margin-bottom':1 })
    )
    class Meta:
        model = Comment
        exclude = ['situations', 'send_date']
