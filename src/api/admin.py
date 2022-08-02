from django.contrib import admin
from .models import Student, Todo, Message, GroupChat
# Register your models here.
admin.site.register(Student)
admin.site.register(Todo)
admin.site.register(Message)
admin.site.register(GroupChat)