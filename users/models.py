#from typing_extensions import Required
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(
        self,
        username,
        first_name,
        last_name,
        email,
        employee_id,
        employment_date,
        address,
        department,
        job_description,
        password=None,
    ):
        # if first_name is None:
        #raise TypeError("Users must have first names")
        if username is None:
            raise TypeError("Users must have a Username")
        # if last_name is None:
            #raise TypeError("Users must have last names")
        if email is None:
            raise TypeError("Users must have Email")
        # if employee_id is None:
            #raise TypeError("Users must have Employee_id")
        # if employment_date is None:
            #raise TypeError("Users must have Employment Date")
        # if address is None:
            #raise TypeError("Users must have an Address")
        # if department is None:
            #raise TypeError("Users must have Department")
        # if job_description is None:
            #raise TypeError("Users must have job description")

        user = self.model(first_name=first_name,
                          username=username,
                          last_name=last_name,
                          email=self.normalize_email(email),
                          employee_id=employee_id,
                          employment_date=employment_date,
                          address=address,
                          department=department,
                          job_description=job_description
                          )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        username,
        email,
        password=None,
        first_name=None,
        last_name=None,
        employee_id=None,
        employment_date=None,
        address=None,
        department=None,
        job_description=None,

    ):
        if password is None:
            raise ("Password Cannot be Empty")
        print(email)
        # if username is None:
        #raise ("Username cannot be Empty")
        # if email is None:
        #raise ("Username cannot be Email")
        user = self.create_user(
            username,
            first_name,
            last_name,
            email,
            employee_id,
            employment_date,
            address,
            department,
            job_description,
            password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=20, unique=True, db_index=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(unique=True, db_index=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    employment_date = models.DateField(null=True)
    department = models.CharField(max_length=30, null=True, blank=True)
    job_description = models.CharField(max_length=30, null=True, blank=True)
    employee_id = models.IntegerField(null=True, blank=True)
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = UserManager()

    def __str__(self):
        return self.email
