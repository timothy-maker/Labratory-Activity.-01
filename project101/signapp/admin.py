
from django.contrib import admin
from .models import SignUpRegistration

@admin.register(SignUpRegistration)
class SignUpRegistrationAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'gender', 'date_registered')
    search_fields = ('username', 'email', 'first_name', 'last_name')
