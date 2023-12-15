from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here


class Usermanage(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError(" you make sure have an email")
        if not username:
            raise ValueError(" you make sure have an username")
        user=self.model(email=self.normalize_email(email),
                        last_name=last_name,first_name=first_name,username=username
                        
                        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,username,email,password=None):
       user=self.create_user(email=self.normalize_email(email),
                        last_name=last_name,first_name=first_name,username=username)
       user.set_password(password)
       user.save(using=self._db)
       user.is_admin=True
       user.is_staff=True
       user.is_active=True
       user.is_superuser=True
       return user
       
        
class User(AbstractBaseUser):
    VENDOR =1
    COSTUMER=2
    ROLE=((VENDOR ,"Resturant"),(COSTUMER,"Costumer"))
    last_name=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    role=models.PositiveSmallIntegerField(choices=ROLE,blank=True,null=True)
    #required field
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = Usermanage()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_role(self):
        if self.role == 1:
            user_role = 'Vendor'
        elif self.role == 2:
            user_role = 'Customer'
        return user_role
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    # def full_address(self):
    #     return f'{self.address_line_1}, {self.address_line_2}'

    def __str__(self):
        return self.user.email
    