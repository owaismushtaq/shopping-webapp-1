from trialshop import views
from django.conf.urls import patterns,url
from django.contrib import admin
admin.autodiscover()

urlpatterns=patterns('',

	url(r'^$',views.IndexView.as_view(), name='new_arrival'),
	url(r'^category/(?P<category_id>\d+)/$',views.CategoryView.as_view(),name="category"),
	url(r'^product_detail/(?P<detail_id>\d+)/$',views.ProductDetailcView.as_view(),name="product_detail"),
	url(r'^product_cart/(?P<product_cart_id>\d+)/$',views.CartView.as_view(),name="product_cart"),
	url(r'^remove_cart/(?P<cart_remove_id>\d+)/$',views.CartRemove.as_view(),name="remove_cart"),
	#url(r'^shoes$',views.ShoesView.as_view(), name='shoes'),
)
