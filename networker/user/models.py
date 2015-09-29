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
    email = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()
    created_dateTime = models.DateTimeField(auto_now_add=True)
    last_login_dateTime = models.DateTimeField(default=datetime.now())
    user_timezone = timezone.now()

class Skill_Category(model.Model):
	""" This is a helper table for User_Skills """
		skill = models.CharField(max_length=50)

class User_Skill(model.Model):
	""" This is a sub-table for User storing Skills """
		user_id = models.ForeignKey(User)
		skill_category_id = models.ForeignKey(Skill_Category)
		skill_description = models.TextField(max_length=255)




