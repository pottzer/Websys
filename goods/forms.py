from django.forms import ModelForm, Textarea
from goods.models import Goods, Comment

class GoodForm(ModelForm):
	class Meta:
		model = Goods
		fields	= ['id_good', 'name', 'price', 'image', 'stock', 'description', 'expired']
		widgets = {'description': Textarea()}

class EditProductForm(ModelForm): 
	class Meta: 
		model = Goods
		fields = ['name', 'price', 'image', 'stock', 'description', 'expired']
		widgets = {'description': Textarea()}

class PostComment(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment_text']
		widgets = {'comment_text': Textarea()}
