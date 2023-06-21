from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserAuthManager(BaseUserManager):

    def create_user(self, email, first_name, second_name, third_name, fourth_name, phone_number, password=None):
        user = self.model(
            email=email,
            first_name=first_name,
            second_name=second_name,
            third_name=third_name,
            fourth_name=fourth_name,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, second_name, third_name, fourth_name, phone_number, password):
        user = self.create_user(
            email=email,
            first_name=first_name,
            second_name=second_name,
            third_name=third_name,
            fourth_name=fourth_name,
            phone_number=phone_number,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self._db)
        return user


class UserAuth(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), max_length=50, unique=True, null=True, blank=True)
    phone_number = PhoneNumberField(_('phone number'), region="EG", unique=True)
    first_name = models.CharField(_('first name'), max_length=50)
    second_name = models.CharField(_('second name'), max_length=50)
    third_name = models.CharField(_('third name'), max_length=50)
    fourth_name = models.CharField(_('fourth name'), max_length=50)

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    last_login = models.DateTimeField(_('last login'), auto_now=True)

    is_staff = models.BooleanField(_('staff'), default=False, help_text=_('Determines whether the user can log in to this administrator site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_('Specifies whether or not this user should be treated as active. Uncheck this instead of deleting the accounts.'))


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'first_name', 'second_name', 'third_name', 'fourth_name']

    objects = UserAuthManager()

    class Meta:
        verbose_name = _('user auth')
        verbose_name_plural = _('users auth')

    def __str__(self):
        return str(self.phone_number)