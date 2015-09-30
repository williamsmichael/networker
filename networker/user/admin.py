from django.contrib import admin
from .models import NetworkerUser
from .models import SkillCategory
from .models import UserSkill
from .models import AddressCategory
from .models import UserAddress
from .models import EmailCategory
from .models import UserEmail
from .models import PhoneCategory
from .models import UserPhone
from .models import SocialMediaCategory
from .models import UserSocialMedia
from .models import JobCategory
from .models import UserJob
from .models import EducationCategory
from .models import UserEducation

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


