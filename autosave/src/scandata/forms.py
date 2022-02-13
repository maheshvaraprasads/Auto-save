from django import forms
from .models import Data
# from .models import Comment
import datetime

class DataCreationForm(forms.ModelForm):
	class Meta:
		model = Data
		exclude = ['user','updated','created']





# class CommentForm(forms.ModelForm):

# 	class Meta:
# 		model = Comment
# 		exclude = ['updated','created','request']