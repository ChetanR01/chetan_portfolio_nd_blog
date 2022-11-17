from django.contrib import admin
from . models import MyEducation, MyExperience, MySkill, Project, Contact, About
# Register your models here.

# admin.site.register(MySkill)
admin.site.register(Project)
admin.site.register(About)


# To modify Contact view for admin
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject']
admin.site.register(Contact, ContactAdmin)

# To modify Education view for admin
class MyEducationAdmin(admin.ModelAdmin):
    list_display = ['id','name','university','date_from','date_to']
admin.site.register(MyEducation, MyEducationAdmin)

# To modify Experience view for admin
class MyExperienceAdmin(admin.ModelAdmin):
    list_display = ['id','job_title','company_name','date_from','date_to']
admin.site.register(MyExperience, MyExperienceAdmin)

# To modify Skills view for admin
class MySkillAdmin(admin.ModelAdmin):
    list_display = ['name','skill_percentage']
    list_editable = ['skill_percentage']
admin.site.register(MySkill, MySkillAdmin)

