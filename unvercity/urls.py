from django.urls import path
from . import views

urlpatterns = [
    path('',views.body_funk,name="tana_qismi"),
    path('student-add/',views.add_student,name="qushdik"),
    path('student_list/',views.student_list,name='listga joylash'),
    path('add-ustoz/', views.add_ustoz, name='qushdik'),
    path('ustoz_list/', views.ustoz_list, name='listga joylash'),

]