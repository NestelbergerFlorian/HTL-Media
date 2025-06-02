from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titel','image_file','Description','main_Tag']

class FilterForm(forms.Form):
    titel = forms.CharField(max_length=200,required=False)
    titel.widget.attrs.update({'class': 'w-[100%] text-2xl input shadow-none focus:ring-0'})
    titel.widget.attrs.update({'placeholder': 'Search'})
    order_by = forms.ChoiceField(choices=(
        (1,"älteste"),(2,"jüngste"),(3,"meiste Aufrufe"),(4,"meiste Likes"),(5,"von Dir")
    ))