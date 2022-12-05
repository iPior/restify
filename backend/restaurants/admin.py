from django.contrib import admin

from restaurants.models import Restaurant, Comment, Food, Like, Follow

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Comment)
admin.site.register(Food)
admin.site.register(Like)
admin.site.register(Follow)
