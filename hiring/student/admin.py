from django.contrib import admin

from .models import Student,certificate,exam,course,Manager,Result,submit_test,Std_Result

admin.site.register(Student)
admin.site.register(certificate)
admin.site.register(exam)
admin.site.register(course)
admin.site.register(Manager)
admin.site.register(Result)
admin.site.register(submit_test)
admin.site.register(Std_Result)
