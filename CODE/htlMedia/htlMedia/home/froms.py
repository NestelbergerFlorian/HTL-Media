from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titel','image_file','main_Tag']

class FilterForm(forms.Form):
    titel = forms.CharField(max_length=200,required=False)
    order_by = forms.ChoiceField(choices=(
        (1,"älteste"),(2,"jüngste")
    ))