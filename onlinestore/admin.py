from django.contrib import admin
from .models import Category, Product ,Order,Wishlist,Comments,Follow,Profile
# Register your models here.
class ProductModel(admin.ModelAdmin):
    list_display=['id','name','price','category']

class OrderModel(admin.ModelAdmin):
    list_display=['id','name','price','user']

class WishModel(admin.ModelAdmin):
    list_display=['id','user','product']

class CommentModel(admin.ModelAdmin):
    list_display=['id','user','product']    

class ProfileModel(admin.ModelAdmin):
    list_display=['id','user','userid']    

admin.site.register(Category)
admin.site.register(Product,ProductModel)
admin.site.register(Order,OrderModel)
admin.site.register(Wishlist,WishModel)
admin.site.register(Comments,CommentModel)
admin.site.register(Follow)
admin.site.register(Profile,ProfileModel)
