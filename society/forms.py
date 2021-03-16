from django import forms
from .models import People

class RegisterForm(forms.ModelForm):
	"""Form for the people model"""
	class Meta:
		model=People
		fields =('about_me','image','fav_movies','first_name','last_name','username')
# class People(models.Model):
#     about_me = models.CharField(max_length=100)
#     photo_image = models.ImageField(upload_to='images',null=True)
#     fav_movies = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100,unique=True)

#     def __str__(self):
#         return self.username