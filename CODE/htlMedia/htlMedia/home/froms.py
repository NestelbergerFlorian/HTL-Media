from django import forms
from .models import Post
from django.forms import ClearableFileInput

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titel','image_file','Description','main_Tag']
        widgets = {
            'titel': forms.TextInput(attrs={'placeholder':'Title *','class': 'text-base-content text-xl w-[100%] my-4 border-b-2 border-base-200 opacity-50 focus:border-b-2 focus:border-primary focus:opacity-100 focus:outline-none focus:shadow-lg focus:shadow-secondary'}),
            'Description': forms.Textarea(attrs={'rows':'2','placeholder':'Description *','class': 'text-base-content text-xl w-[100%] my-4 border-b-2 border-base-200 opacity-50 focus:border-b-2 focus:border-primary focus:opacity-100 focus:outline-none focus:shadow-lg focus:shadow-secondary'}),
            'image_file': ClearableFileInput(attrs={'class': 'w-[100%] opacity-0 aspect-square bg-accent pointer-events-auto relative'}),
        }


class FilterForm(forms.Form):
    titel = forms.CharField(max_length=200,required=False)
    titel.widget.attrs.update({'class': 'w-[100%] text-2xl input shadow-none focus:ring-0'})
    titel.widget.attrs.update({'placeholder': 'Search'})
    order_by = forms.ChoiceField(choices=(
        (1,"älteste"),(2,"jüngste"),(3,"meiste Aufrufe"),(4,"meiste Likes"),(5,"von Dir")
    ))