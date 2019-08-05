from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, ):
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email), 
            first_name=first_name,
            last_name=last_name,)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email, first_name, last_name, password
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('Email Address'),
        max_length=255,
        unique=True
    )
    first_name = models.CharField(
        verbose_name=_('First Name'),
        max_length=30
    )
    last_name = models.CharField(
        verbose_name=_('Last Name'),
        max_length=30
    )
    is_active = models.BooleanField(
        verbose_name=_('Is Active'),
        default=True
    )
    is_staff = models.BooleanField(
        default=False
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date Joined'),
        default=timezone.now
    )
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def get_full_name(self):
        """retreive full name of user"""
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        """retreive short name of user"""
        return self.first_name

    def __str__(self):
        """return string representation of our user"""
        return self.first_name

class Crawling(models.Model):
    pass

# class Traindata7(models.Model):
#     trantype = models.TextField(db_column='TranType', blank=True, null=True)  # Field name made lowercase.
#     waytype = models.TextField(db_column='WayType', blank=True, null=True)  # Field name made lowercase.
#     trainnum = models.IntegerField(db_column='TrainNum', blank=True, null=True)  # Field name made lowercase.
#     traintype = models.TextField(db_column='TrainType', blank=True, null=True)  # Field name made lowercase.
#     depcity = models.TextField(db_column='DepCity', blank=True, null=True)  # Field name made lowercase.
#     arrcity = models.TextField(db_column='ArrCity', blank=True, null=True)  # Field name made lowercase.
#     deptime = models.TextField(db_column='DepTime', blank=True, null=True)  # Field name made lowercase.
#     arrtime = models.TextField(db_column='ArrTime', blank=True, null=True)  # Field name made lowercase.
#     month = models.IntegerField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
#     day = models.IntegerField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    
#     class Meta:
#         managed = False
#         db_table = 'TrainData7'

class Traindata7(models.Model):
    trantype = models.TextField(db_column='TranType', blank=True, null=True)  # Field name made lowercase.
    waytype = models.TextField(db_column='WayType', blank=True, null=True)  # Field name made lowercase.
    trainnum = models.IntegerField(db_column='TrainNum', blank=True, null=True)  # Field name made lowercase.
    traintype = models.TextField(db_column='TrainType', blank=True, null=True)  # Field name made lowercase.
    depcity = models.TextField(db_column='DepCity', blank=True, null=True)  # Field name made lowercase.
    arrcity = models.TextField(db_column='ArrCity', blank=True, null=True)  # Field name made lowercase.
    deptime = models.TextField(db_column='DepTime', blank=True, null=True)  # Field name made lowercase.
    arrtime = models.TextField(db_column='ArrTime', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'TrainData7'