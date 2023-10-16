from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

# Create your models here.

class UserManager(BaseUserManager):
    
    def create_user(self, username, email, password=None):
        
        if username is None:
            raise TypeError("Users should have a username")
        
        if email is None:
            raise TypeError("Users should have an email")
        
        user=self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        