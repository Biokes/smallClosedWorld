from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = [
    ('USER', 'USER'),
    ('ADMIN', 'ADMIN'),
]


class User(AbstractUser):
    id = models.AutoField(primary_key=True,default=0)
    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(max_length=16, validators=[RegexValidator(
        regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,16}$',
        message="Password must be between 5 and 16 characters long and contain at least one letter and one number."
    )]
    )
    isVerified = models.BooleanField(default=False)
    username = models.CharField(max_length=254, unique=False)
    profile_picture_url = models.CharField(max_length=254, blank=True, null=False)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], default='Female')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return f'email : {self.email} , username: {self.username}, gender: {self.gender}'
