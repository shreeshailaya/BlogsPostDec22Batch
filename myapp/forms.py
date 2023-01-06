from django import forms
from myapp.models import Blog
 
 
# creating a form
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'tags', 'publisher', 'no_lines', 'img']