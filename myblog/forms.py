from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','body','header_image')

		widgets = {
		'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Введите название статьи'}),
		'body': forms.Textarea(attrs={'class':'form-control'}),
		'header_image': forms.ClearableFileInput(attrs={'class':'custom-file'})
		}