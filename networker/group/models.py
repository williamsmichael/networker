from django.db import models
from datetime import datetime
from user.models import NetworkerUser

class NetworkerGroup(models.Model):
	""" Main table for Group """
	group_organizer = models.ForeignKey(NetworkerUser)
	group_name = models.CharField(max_length=255)
	group_description = models.TextField(max_length=255, blank=True)
	created_dateTime = models.DateTimeField(auto_now_add=True)

class GroupUser(models.Model):
	""" Relationship table for message system and user """
	group_id = models.ForeignKey(NetworkerGroup)
	user_id = models.ForeignKey(NetworkerUser)
	last_message_dateTime = models.DateTimeField(auto_now=True)

class MessageSystemTopic(models.Model):
	""" Topic table for message system """
	group_id = models.ForeignKey(NetworkerGroup)
	originator_id = models.ForeignKey(GroupUser)
	topic_name = models.CharField(max_length=255)
	topic_description = models.TextField()
	created_dateTime = models.DateTimeField(auto_now_add=True)

class MessageSystemTopicTag(models.Model):
	""" Topic Tag table for the message system """
	message_system_topic_tag_id = models.ForeignKey(MessageSystemTopic)
	tag = models.CharField(max_length=25, blank=True)

class MessageSystemMessage(models.Model):
	""" Message table for the message system """
	message_system_topic_id = models.ForeignKey(MessageSystemTopic)
	group_user_id = models.ForeignKey(GroupUser)
	message = models.TextField()
	created_dateTime = models.DateTimeField(auto_now_add=True)



