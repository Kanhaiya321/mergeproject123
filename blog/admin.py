from django.contrib import admin
from .models import Post, User , Tags, Category , Comment
from django.contrib.auth.admin import UserAdmin

admin.site.register(Post)

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     # model = CustomUser
#     list_display = ["email", "username",]

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Comment)