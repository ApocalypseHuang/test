from django import forms
from .models import Comment
# 表单
# Create your views here.   
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
