from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import fields
from django.forms import widgets
from my_app.models import PostToProject,ProjectComment
from django import forms


class UserCRForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserCRForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['style']='color:white;width:800;font-size:16px;'
        self.fields['email'].widget.attrs['style']='color:white;width:800;font-size:16px;'
        self.fields['password1'].widget.attrs['style']='color:white;width:800;font-size:16px;'
        self.fields['password2'].widget.attrs['style']='color:white;width:800;font-size:16px;'
        

class PostForm(forms.ModelForm):

    class Meta:
        model=PostToProject
        fields=('author','title','text','author_img')

        widgets={
            'title':forms.TextInput(attrs={'class':'title'}),
            'text':forms.Textarea(attrs={'style':'color:rgba(0,0,0,.9)'}),
        }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model=ProjectComment
        fields=('text',)

        widgets={
            'text':forms.Textarea(attrs={'class':'commentinput text'}),
            'text':forms.Textarea(attrs={'style':'padding-left:15px;background-color:rgba(0,0,0,.1);color:rgba(0,0,0,.95)'}),
        }
   
