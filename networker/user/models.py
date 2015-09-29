from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class User(models.Model):
    """ This is the main table for User """
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    relationship_to_group = models.CharField(max_length=50)
    # profile_image = ImageField()
    primary_email = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateTimeField()
    created_dateTime = models.DateTimeField(auto_now_add=True)
    last_login_dateTime = models.DateTimeField(default=datetime.now())
    user_timezone = timezone.now()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

class Skill_Category(models.Model):
		""" This is a helper table for User_Skill """
		SKILL_CATEGORY_CHOICES = (
				(ADMINISTRATIVE, 'Administrative'),
				(CLERICAL, 'Clerical'),
				(COMMUNICATION, 'Communication'),
				(COUNSELING, 'Counseling'),
				(CREATIVE, 'Development'),
				(FINANCIAL, 'Finanicial'),
        (INTERPERSONAL, 'Interpersonal'),
        (MANAGEMENT, 'Management'),
        (PROBLEM_SOLVING, 'Problem Solving'),
        (ORGANIZATIONAL, 'Organizational'),
        (RESEARCH, 'Research')
        (TECHNICAL, 'Technical'),
        (TIME_MANAGEMENT, 'Time Management'),
        (TRAINING, 'Training'),
        (SALES, 'Sales'),
    )
    skill_category = models.CharField(max_length=50,
                                      choices=SKILL_CATEGORY_CHOICES)

class User_Skill(models.Model):
		""" This is a sub-table for the User: Skill """
		user_id = models.ForeignKey(User)
		skill_category_id = models.ForeignKey(Skill_Category)
		skill_description = models.TextField(max_length=255)

class Email_Category(models.Model):
		""" This is a helper table for User_Email """
		EMAIL_CATEGORY_CHOICES = (
				(HOME, 'Home'),
				(WORK, 'Work'),
				(OTHER, 'Other'),
    )
    email_category = models.CharField(max_length=50,
                                      choices=EMAIL_CATEGORY_CHOICES)

class User_Email(models.Model):
		""" This is a sub-table for the User: Email """
		user_id = models.ForeignKey(User)
		email_category_id = models.ForeignKey(Email_Category)
		email = models.CharField(max_length=50)

class Phone_Category(models.Model):
		""" This is a helper table for User_Phone """
		PHONE_CATEGORY_CHOICES = (
				(Mobile, 'Mobile'),
				(WORK, 'Work'),
				(HOME, 'Home'),
				(FAX, 'Fax'),
				(OTHER, 'Other'),
    )
    phone_category = models.CharField(max_length=50,
                                      choices=PHONE_CATEGORY_CHOICES)

class User_Phone(models.Model):
		""" This is a sub-table for the User: Phone """
		user_id = models.ForeignKey(User)
		phone_category_id = models.ForeignKey(Email_Category)
		country_code = models.PositiveSmallIntegerField(max_length=3)
		phone_number = models.PositiveSmallIntegerField(max_length=15)





