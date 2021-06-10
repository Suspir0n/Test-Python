from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from logging import basicConfig, info, INFO


class CompanyManager(BaseUserManager):
    basicConfig(level=INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    def _create_company(self, _email, _password, is_staff, is_superuser, **extra_fields):
        info('\033[1;34mcreating an company...\033[m')
        if not _email:
            info('\033[1;31mThe field cannot be null!\033[m')
            raise ValueError('Companys must have an email address')
        _now = timezone.now()
        _email = self.normalize_email(_email)
        _company = self.model(
            email=_email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=_now,
            date_joined=_now,
            **extra_fields
        )
        _company.set_password(_password)
        _company.save(using=self._db)
        info('\033[1;32mcreating an company with sucess...\033[m')
        return _company

    def create_company(self, _email, _password, **extra_fields):
        return self._create_company(_email, _password, True, True, **extra_fields)

    def create_superuser(self, _email, _password, **extra_fields):
        user = self._create_company(_email, _password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class Company(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CompanyManager()

    def get_absolute_url(self):
        return "/companys/%i/" % (self.pk)




