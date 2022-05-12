from django.db import models
from django.utils import timezone

class Civil_stat(models.Model):
    status_name = models.CharField(max_length=255, blank=False)
    status_description = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.status_name

class Gender(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Segment(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.title

class Country_region(models.Model):
    region_id = models.IntegerField(primary_key=True)
    region_name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.region_name

class Country_state(models.Model):
    region = models.ForeignKey(Country_region, on_delete=models.CASCADE)
    state_code = models.IntegerField(blank=False, unique=True)
    state_name = models.CharField(max_length=255, blank=False)
    acronym = models.CharField(max_length=255, blank=False, primary_key=True)

    def __str__(self):
        return self.acronym

class Country_city(models.Model):
    state = models.ForeignKey(Country_state, on_delete=models.CASCADE)
    city_code = models.IntegerField(blank=False, unique=True)
    city_name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.city_name

class Common_user(models.Model):
    user_name = models.CharField(max_length=255, blank=False)
    date_creation = models.DateTimeField(default=timezone.now)
    user_email = models.EmailField(max_length=255, blank=False, unique=True)
    user_password = models.CharField(max_length=255, blank=False)
    user_phone = models.CharField(max_length=255, blank=False)
    user_city = models.ForeignKey(Country_city, on_delete=models.CASCADE)
    user_address = models.CharField(max_length=255, blank=False)
    user_photo = models.CharField(max_length=255, blank=True)
    user_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_name

class User_cnpj(models.Model):
    common_user = models.ForeignKey(Common_user, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=255, blank=False, unique=True)
    fancy_name = models.CharField(max_length=255, blank=False)
    corporate_name = models.CharField(max_length=255, blank=False)
    segments = models.ForeignKey(Segment, on_delete=models.CASCADE, related_name='companySegments')

    def __str__(self):
        return self.fancy_name

class User_cpf(models.Model):
    common_user = models.ForeignKey(Common_user, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=255, blank=False, unique=True)
    name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=False, default=timezone.now)
    profession = models.CharField(max_length=255, blank=True)
    civil_status = models.ForeignKey(Civil_stat, on_delete=models.CASCADE, related_name='civilStatUser')

    def __str__(self):
        return self.name

class User_cpf_interest(models.Model):
    user_cpf = models.ForeignKey(User_cpf, on_delete=models.CASCADE, related_name='usersInterests')
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, related_name='segmentsInterests')

    def __unicode__(self):
        return self.user_cpf.name + self.segment.title