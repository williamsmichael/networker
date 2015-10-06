from django.contrib import admin
from .models import NetworkerUser, SkillCategory, UserSkill, AddressCategory, UserAddress, EmailCategory, UserEmail, PhoneCategory, UserPhone, SocialMediaCategory, UserSocialMedia, JobCategory, UserJob, EducationCategory, UserEducation

# Register your models here.
admin.site.register(NetworkerUser)
admin.site.register(SkillCategory)
admin.site.register(UserSkill)
admin.site.register(AddressCategory)
admin.site.register(UserAddress)
admin.site.register(EmailCategory)
admin.site.register(UserEmail)
admin.site.register(PhoneCategory)
admin.site.register(UserPhone)
admin.site.register(SocialMediaCategory)
admin.site.register(UserSocialMedia)
admin.site.register(JobCategory)
admin.site.register(UserJob)
admin.site.register(EducationCategory)
admin.site.register(UserEducation)


