# from django import forms
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.utils.translation import ugettext_lazy as _

# from .models import User, UserManager

# class UserCreationForm(forms.ModelForm):
#     email = forms.EmailField(
#         label=_('Email'),
#         required=True,
#         widget=forms.EmailInput(
#             attrs={
#                 'class' : 'form-control',
#                 'placeholder' : _('Email Address'),
#                 'required' : 'True',
#             }
#         )
#     )
#     first_name = forms.CharField(
#         label=_('First Name'),
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 'class' : 'form-control',
#                 'placeholder' : _('First Name'),
#                 'required' : 'True',
#             }
#         )
#     )
#     last_name = forms.CharField(
#         label=_('Last Name'),
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 'class' : 'form-control',
#                 'placeholder' : _('Last Name'),
#                 'required' : 'True',
#             }
#         )
#     )
#     password1 = forms.CharField(
#         label=_('Password'),
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Password'),
#                 'required': 'True',
#             }
#         )
#     )
#     password2 = forms.CharField(
#         label=_('Password confirmation'),
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Password confirmation'),
#                 'required': 'True',
#             }
#         )
#     )
#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']
#         user.save()
