from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titel','image_file','main_Tag']

class FilterForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titel']

        def __init__(self, *args, **kwargs):
            super(FilterForm, self).__init__(*args, **kwargs)
            self.fields['titel'].blank = True
