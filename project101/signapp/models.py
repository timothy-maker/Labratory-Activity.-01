
from django.db import models
from django.core.exceptions import ValidationError

class SignUpRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_registered = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=12, default="")

    def clean(self):
        # Ensure all required fields are filled
        required_fields = [
            'first_name', 'last_name', 'email', 'username', 'password', 'confirm_password', 'date_of_birth'
        ]
        for field in required_fields:
            if not getattr(self, field):
                raise ValidationError({field: f"{field} is required."})

        # Passwords must match
        if self.password != self.confirm_password:
            raise ValidationError("Password and Confirm Password do not match.")

    def save(self, *args, **kwargs):
        # Call clean() before saving
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
