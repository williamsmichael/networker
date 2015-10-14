# from django.test import TestCase
# from django.utils import timezone

# from .models import NetworkerGroup


# class NetworkerGroupModelTests(TestCase):
# 	""" create a group and test if it is less than current time """
# 	def setUp(self):
# 		self.group = Group.objects.create(
# 			name = "Makers"
# 			id = 1
# 		)

# 	def test_group_creation(self):
# 		networker_group = NetworkerGroup.objects.create(
# 			group_extension = 1,
# 			group_organizer = 1,
# 			group_description = "Makers since 1978",
# 			welcome_message = "Welcome to our new space!",
# 			group_image = "static/images/avatar_group.png",
# 			website = ""

# 		)
# 		now = timezone.now()
# 		self.assertLess(networker_group.created_dateTime, now)
