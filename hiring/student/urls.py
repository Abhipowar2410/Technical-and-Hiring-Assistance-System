from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.front),
    path('sign_in',views.sign_in),
    path('registration_student',views.registration_student),
    path('registration_save', views.registration_save),
    path('dashboard',views.dashboard),
    path('edit_profile', views.edit_profile),
    path('student_signup',views.student_signup),
    path('add_certificate',views.add_certificate),
    path('certificate_save',views.certificate_save),
    path('update_data',views.update_data),
    path('student_logout',views.student_logout),
    path('student_profile',views.student_profile),
    path('add_cookie',views.add_cookie),
    path('quiz/<int:course_id>/<str:level>/',views.quiz),
     path('results/', views.results, name='results'),  # Adding a results view for displaying student results
    path('course_list',views.course_list),
    path('search/', views.search_courses),


    #####################################


    path('hr_login', views.hr_login, name='hr_login'),
    path('hr_registration_save', views.hr_registration_save, name='hr_registration_save'),
    path('hr_signupcheck', views.hr_signupcheck),
    path('HR_dashboard', views.HR_dashboard),
    path('hr_logout', views.hr_logout),
    path('HR_edit_profile', views.HR_edit_profile),
    path('HR_update_data', views.HR_update_data),
    path('HR_profile', views.HR_profile),
    path('student-profile/<int:student_id>/', views.std_profile_for_hr, name='std_profile_for_hr'),
    path('search_students/',views.search_students, name='search_students'),
    path('hr_registration/',views.hr_registration),

    ###########################################################

    path('about', views.about),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
