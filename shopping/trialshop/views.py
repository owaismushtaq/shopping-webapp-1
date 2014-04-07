from django.shortcuts import render ,get_object_or_404
from trialshop.models import Product,Product_Cat
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader
from django.http import HttpResponse,request
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'trialshop/new_arrival.html'
   
    def get(self,request,*args,**kwargs):
    	prod_cat= Product_Cat.objects.all()
    	productobj=Product.objects.order_by('-pub_date')#[:5]
    	return self.render_to_response({'productobj':productobj,'prod_cat':prod_cat})


class CategoryView(generic.TemplateView):
	template_name = 'trialshop/new_arrival.html'
	def get(self,request,*args,**kwargs):
		productobj=Product.objects.order_by('-pub_date')#[:5]
		prod_cat= Product_Cat.objects.all()
		product_search_key=Product_Cat.objects.get(id =kwargs['category_id'])
		return self.render_to_response({ 'productobj':  productobj, 'prod_cat':  prod_cat, 'product_search_key': product_search_key,
		 })

class ProductDetailcView(generic.TemplateView):
    template_name = 'trialshop/product_detail.html'
    def get(self,request,*args,**kwargs):
        productobj=Product.objects.get(id=kwargs['detail_id'])
        return self.render_to_response({  'productobj' :  productobj,
        })

class CartView(generic.TemplateView):
    template_name = 'trialshop/viewcart.html'
    def get(self,request,*args,**kwargs):
        product_id=kwargs.get('product_cart_id')
        productobj=Product.objects.order_by('-pub_date')#[:5]
        cart_obj=Product.objects.get(id = product_id)
        mesg=''
        if cart_obj.cart_value == True:
            mesg="This Product is already in Basket"
        else:    
            cart_obj.cart_value = True
            cart_obj.save()
        total=0
        for i in productobj:
            if i.cart_value:
                total=total+i.product_price
        return self.render_to_response({'productobj':productobj, 'product_id':product_id,'total':total,'mesg':mesg,
        })

class CartRemove(generic.TemplateView):
    template_name = 'trialshop/viewcart.html'
    def get(self,request,*args,**kwargs):
        product_id=kwargs.get('cart_remove_id')
        productobj=Product.objects.order_by('-pub_date')#[:5]
        cart_obj=Product.objects.get(id = product_id)
        cart_obj.cart_value = False
        cart_obj.save()
        total=0
        for i in productobj:
            if i.cart_value:
                total=total+i.product_price
        return self.render_to_response({'productobj':productobj, 'product_id':product_id,'total':total,
        })