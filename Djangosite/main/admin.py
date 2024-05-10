from django.contrib import admin
from .models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullName', 'about', 'post', 'photo')
    list_display_links=('id', 'fullName')
    search_fields = ('fullName', 'about')

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'projName', 'description', 'link', 'preson')
    list_display_links=('id', 'projName')
    search_fields = ('projName', 'description')

class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id','skiName', 'preson')
    list_display_links=('id', 'skiName')
    search_fields = ('id', 'skiName')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'comName', 'post', 'dateStart', 'dateEnd','preson')
    list_display_links=('id', 'comName')
    search_fields = ('comName', 'post')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'eduName', 'eduDepartment', 'eduQualification', 'dateStart', 'dateEnd','preson')
    list_display_links=('id', 'eduName')
    search_fields = ('eduName', 'eduDepartment')

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Person, PersonAdmin)