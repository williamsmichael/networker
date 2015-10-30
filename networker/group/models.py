from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from forum.models import Forum


# helper function for uploading files to group name path
def upload_to(instance, filename):
    return 'images/{}/{}'.format(instance.name, filename)
    

class NetworkerGroup(models.Model):
	""" Main table for Group """
	organizer = models.ForeignKey(User)
	forum = models.OneToOneField(Forum)

	name = models.CharField(max_length=255, blank=True)	
	description = models.TextField(blank=True)
	welcome_message = models.TextField(blank=True)
	profile_image = models.ImageField(upload_to=upload_to, blank=True, null=True)
	website = models.URLField(blank=True)
	created_dateTime = models.DateTimeField(auto_now_add=True, auto_now=False)

	class Meta:
		ordering = ['id',]
		
	def __str__(self):
		return self.name


# ----------------------------------------------------------------------unused
# class GroupUser(models.Model):
# 	""" Relationship table for message system and user """
# 	group_id = models.ForeignKey(NetworkerGroup)
# 	user_id = models.ForeignKey(User)

# 	last_message_dateTime = models.DateTimeField(auto_now_add=False, auto_now=True)


# class MessageSystemTopic(models.Model):
# 	""" Topic table for message system """
# 	group_id = models.ForeignKey(NetworkerGroup)
# 	originator_id = models.ForeignKey(GroupUser)
# 	topic_name = models.CharField(max_length=255)
# 	topic_description = models.TextField()
# 	created_dateTime = models.DateTimeField(auto_now_add=True, auto_now=False)


# class MessageSystemTopicTag(models.Model):
# 	""" Topic Tag table for the message system """
# 	message_system_topic_tag_id = models.ForeignKey(MessageSystemTopic)
# 	tag = models.CharField(max_length=255, blank=True)


# class MessageSystemMessage(models.Model):
# 	""" Message table for the message system """
# 	message_system_topic_id = models.ForeignKey(MessageSystemTopic)
# 	group_user_id = models.ForeignKey(GroupUser)
# 	message = models.TextField()
# 	created_dateTime = models.DateTimeField(auto_now_add=True, auto_now=False)



