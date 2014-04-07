from django.db import models
#from django.db.models import ImageField
from django.contrib import admin

class Product_Cat(models.Model):
	cat_field = models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.cat_field)

# Create your models here.
class Product(models.Model):
	product_type = models.ForeignKey(Product_Cat)
	product_name = models.CharField(max_length=200)
	product_brand = models.CharField(max_length=200)
	product_pic = models.ImageField(upload_to='img')
	product_price = models.IntegerField(default=0)
	pub_date = models.DateTimeField('date published')
	cart_value= models.BooleanField(default=False)
	
	list_display = ["product_name", "product_brand", "product_price", "pub_date", "cart_value","product_pic"]
	
	def __unicode__(self):
		return unicode(self.product_name)
	# def image_thumb(self):
	# 	return '<img src="/photostore/%s" width="100" height="100" />' % (self.photo)
	# image_thumb.allow_tags = True	
        
