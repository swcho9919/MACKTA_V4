from django.contrib import admin
from mackta_api.models import User 
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
# Register your models here.

admin.site.register(User)
# admin.site.register(ProfileFeedItem)

# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = User

# # class CustomUserCreationForm(UserCreationForm): 
# #     class Meta(UserCreationForm.Meta):
# #         model = User
    
# #     def clean_email(self):
# #         email = self.cleaned_data['email']
# #         try:
# #             User.objects.get(email=email)
# #         except User.DoesNotExist:
# #             return email
# #         raise forms.ValidationError(self.error_messages['duplicate_email'])


# class CustomUserAdmin(UserAdmin):
#     form = CustomUserChangeForm
#     # add_form = CustomUserCreationForm
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields' : ('email', 'first_name', 'last_name', 'is_staff',)}),
    # )