from django.db import models
from datetime import datetime
from django.utils import timezone

class User(models.Model):
    """ Main table for User """
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    relationship_to_group = models.CharField(max_length=50)
    profile_image = ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    primary_email = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateTimeField()
    created_dateTime = models.DateTimeField(auto_now_add=True)
    last_login_dateTime = models.DateTimeField(default=datetime.now())
    user_timezone = timezone.now()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

class Skill_Category(models.Model):
	""" Helper table for User_Skill """
    skill_category = models.CharField(max_length=20)

class User_Skill(models.Model):
	""" Sub-table for the User: Skill """
	user_id = models.ForeignKey(User)
	skill_category_id = models.ForeignKey(Skill_Category)
	skill_description = models.TextField(max_length=255, blank=True)

class Address_Category(models.Model):
	""" Helper table for User_Address """
    address_category = models.CharField(max_length=10)

class User_Address(models.Model):
	""" Sub-table for the User: Address """
	user_id = models.ForeignKey(User)
	address_category_id = models.ForeignKey(Address_Category)
	street_address_1 = models.CharField(max_length=50)
	street_address_2 = models.CharField(max_length=50)
	city_town = models.CharField(max_length=50)
	state_province = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	postal_code = models.CharField(max_length=25)
	latitude_api = models.CharField(max_length=25)
	longitude_api = models.CharField(max_length=25)

class Email_Category(models.Model):
	""" Helper table for User_Email """
    email_category = models.CharField(max_length=10)

class User_Email(models.Model):
	""" Sub-table for the User: Email """
	user_id = models.ForeignKey(User)
	email_category_id = models.ForeignKey(Address_Category)
	email = models.CharField(max_length=50, blank=True)

class Phone_Category(models.Model):
	""" Helper table for User_Phone """
    phone_category = models.CharField(max_length=10)

class User_Phone(models.Model):
	""" Sub-table for the User: Phone """
	user_id = models.ForeignKey(User)
	phone_category_id = models.ForeignKey(Phone_Category)
	country_code = models.PositiveSmallIntegerField(max_length=3, blank=True)
	phone_number = models.PositiveSmallIntegerField(max_length=15, blank=True)

class Social_Media_Category(models.Model):
	""" Helper table for User_Social_Media """
	social_media_category = models.CharField(max_length=50)

class User_Social_Media(models.Model):
	""" Sub-table for the User: Social Media """
	user_id = models.ForeignKey(User)
	social_media_category_id = models.ForeignKey(Social_Media_Category)
	social_media_url = models.URLField(blank=True)

class Job_Category(models.Model):
	""" Helper table for User_Job """
	job_category = models.CharField(max_length=50)

class User_Job(models.Model):
	""" Sub-table for the User: Job """
	user_id = models.ForeignKey(User)
	job_category_id = models.ForeignKey(Job_Category)
	job_description = models.TextField(max_length=255, blank=True)
	company_name = models.CharField(max_length=50, blank=True)
	company_state_province = models.CharField(max_length=50, blank=True)
	company_country = models.CharField(max_length=50, blank=True)
	company_year_started = models.DateField(blank=True)
	company_year_ended = models.DateField(blank=True)

class Education_Category(models.Model):
	""" Helper table for User_Education """
	education_category = models.CharField(max_length=50)

class User_Education(models.Model):
	""" Sub-table for the User: Education """
	user_id = models.ForeignKey(User)
	education_category_id = models.ForeignKey(Education_Category)
	education_description = models.TextField(max_length=255, blank=True)
	school_name = models.CharField(max_length=255, blank=True)
	graduation_status = models.BooleanField(default=False)
	school_year_started = models.DateField(blank=True)
	school_year_ended = models.DateField(blank=True)












