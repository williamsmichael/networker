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
    profile_image = ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
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
	    (RESEARCH, 'Research'),
	    (TECHNICAL, 'Technical'),
	    (TIME_MANAGEMENT, 'Time Management'),
	    (TRAINING, 'Training'),
	    (SALES, 'Sales'),
    )
    skill_category = models.CharField(max_length=20, choices=SKILL_CATEGORY_CHOICES)

class User_Skill(models.Model):
	""" This is a sub-table for the User: Skill """
	user_id = models.ForeignKey(User)
	skill_category_id = models.ForeignKey(Skill_Category)
	skill_description = models.TextField(max_length=255, blank=True)

class Address_Category(models.Model):
	""" This is a helper table for User_Address + User_Email """
	ADDRESS_CATEGORY_CHOICES = (
		(HOME, 'Home'),
		(WORK, 'Work'),
		(OTHER, 'Other'),
    )
    address_category = models.CharField(max_length=10, choices=ADDRESS_CATEGORY_CHOICES)

class User_Address(models.Model):
	""" This is a sub-table for the User: Address """
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

class User_Email(models.Model):
	""" This is a sub-table for the User: Email """
	user_id = models.ForeignKey(User)
	email_category_id = models.ForeignKey(Address_Category)
	email = models.CharField(max_length=50, blank=True)

class Phone_Category(models.Model):
	""" This is a helper table for User_Phone """
	PHONE_CATEGORY_CHOICES = (
		(MOBILE, 'Mobile'),
		(WORK, 'Work'),
		(HOME, 'Home'),
		(FAX, 'Fax'),
		(OTHER, 'Other'),
    )
    phone_category = models.CharField(max_length=10, choices=PHONE_CATEGORY_CHOICES)

class User_Phone(models.Model):
	""" This is a sub-table for the User: Phone """
	user_id = models.ForeignKey(User)
	phone_category_id = models.ForeignKey(Phone_Category)
	country_code = models.PositiveSmallIntegerField(max_length=3, blank=True)
	phone_number = models.PositiveSmallIntegerField(max_length=15, blank=True)

class Social_Media_Category(models.Model):
	""" This is a helper table for User_Social_Media """
	SOCIAL_MEDIA_CATEGORY_CHOICES = (
		(FACEBOOK, 'Facebook'),
		(FOURSQUARE, 'Foursquare'),
		(INSTAGRAM, 'Instagram'),
		(KIK_MESSENGER, 'Kik Messenger'),
		(LINKEDIN, 'LinkedIn'),
		(OOVOO, 'ooVoo'),
		(PINTEREST, 'Pinterest'),
		(SKYPE, 'Skype'),
		(TUMBLR, 'Tumblr'),
		(TWITTER, 'Twitter'),
		(VINE, 'Vine'),
		(WHATSAPP, 'Whatsapp'),
    )
    social_media_category = models.CharField(max_length=20, choices=SOCIAL_MEDIA_CATEGORY_CHOICES)

class User_Social_Media(models.Model):
	""" This is a sub-table for the User: Social Media """
	user_id = models.ForeignKey(User)
	social_media_category_id = models.ForeignKey(Social_Media_Category)
	social_media_url = models.URLField(blank=True)

class Job_Category(models.Model):
	""" This is a helper table for User_Job """
	JOB_CATEGORY_CHOICES = (
		(ACCOUNTING, 'Accounting'),
		(ACCOUNTING_CLERICAL, 'Administrative/Clerical')
		(ARTS_ENTERTAINMENT_MEDIA, 'Arts/Entertainment/Media'),
		(AGRICULTURE_FORESTRY_FISHING, 'Agriculture/Forestry/Fishing'),
		(AUTOMOTIVE, 'Automotive'),
		(BIOTECHNOLOGY, 'Biotechnology'),
		(BUSINESS, 'Business'),
		(COMPUTERS, 'Computers'),
		(CONSTRUCTION, 'Construction'),
		(CONSULTING, 'Consulting')
		(CUSTOMER_SERVICE, 'Customer Service'),
		(EDUCATION, 'Education'),
		(ENGINEERING, 'Engineering'),
		(EXECUTIVE, 'Executive'),
		(FACILITIES, 'Facilities'),
		(FINANCIAL_SERVICES, 'Financial Services'),
		(GOVERNMENT, 'Government'),
		(HEALTHCARE, 'Healthcare'),
		(HOSPITALITY, 'Hospitality'),
		(HUMAN_RESOURCES, 'Human Resources'),
		(INFORMATION_TECHNOLOGY, 'Information Technology'),
		(INSURANCE, 'Insurance'),
		(LAW_ENFORCEMENT_FIRE_SECURITY, 'Law Enforcement/Fire/Security'),
		(LEGAL, 'Legal'),
		(MANUFACTURING_PRODUCTION, 'Manufacturing/Production'),
		(MARKETING, 'Marketing'),
		(MEDIA, 'Media'),
		(REAL_ESTATE, 'Real Estate'),
		(RESTAURANT_FOOD_SERVICES, 'Restaurant/Food Services'),
		(RETAIL_WHOLESALE, 'Retail/Wholesale'),
		(SALES, 'Sales'),
		(SCIENCE_RESEARCH, 'Science/Research'),
		(TELECOMMUNICATIONS, 'Telecommunications'),
		(TECHNOLOGY, 'Techology')
		(TRANSPORTATION, 'Transportation/Warehouse'),
		(OTHER, 'Other'),
    )
    job_category = models.CharField(max_length=50, choices=JOB_CATEGORY_CHOICES)

class User_Job(models.Model):
	""" This is a sub-table for the User: Job """
	user_id = models.ForeignKey(User)
	job_category_id = models.ForeignKey(Job_Category)
	job_description = models.TextField(max_length=255, blank=True)
	company_name = models.CharField(max_length=50, blank=True)
	company_state_province = models.CharField(max_length=50, blank=True)
	company_country = models.CharField(max_length=50, blank=True)
	company_year_started = models.DateField(blank=True)
	company_year_ended = models.DateField(blank=True)

class Education_Category(models.Model):
	""" This is a helper table for User_Education """
	Education_CATEGORY_CHOICES = (
		(K12, 'K-12'),
		(HIGHSCHOOL, 'High School Diploma'),
		(SOME_COLLEGE, 'Some College, non-degree'),
		(POSTSECONDARY, 'Postsecondary, non-degree'),
		(ASSOCIATES, 'Associates Degree')
		(BACHELORS, 'Bachelors Degree'),
		(GRADUATE, 'Graduate Degree'),
		(DOCTORAL, 'Doctoral Degree'),
		(CERTIFICATE, 'Certificate'),
		(LICENSE, 'License'),
		(PROFESSIONAL_DEVELOPMENT, 'Professional Development')
    )
    education_category = models.CharField(max_length=50, choices=EDUCATION_CATEGORY_CHOICES)

class User_Education(models.Model):
	""" This is a sub-table for the User: Education """
	user_id = models.ForeignKey(User)
	education_category_id = models.ForeignKey(Education_Category)
	education_description = models.TextField(max_length=255, blank=True)
	school_name = models.CharField(max_length=255, blank=True)
	graduation_status = models.BooleanField(default=False)
	school_year_started = models.DateField(blank=True)
	school_year_ended = models.DateField(blank=True)












