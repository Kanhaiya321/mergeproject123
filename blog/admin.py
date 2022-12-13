from django.contrib import admin
from .models import Post
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Category

admin.site.register(Post)

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     # model = CustomUser
#     list_display = ["email", "username",]

admin.site.register(User)
admin.site.register(Category)