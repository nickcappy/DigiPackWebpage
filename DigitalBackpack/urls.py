from django.urls import path
from . import views

urlpatterns = [
    path( '', views.landing_page, name='landing_page' ),
    path( 'student/', views.student_page, name='student_page' ),
    path( 'teacher/', views.teacher_page, name='teacher_page' ),
    path( 'ratings/', views.ratings, name='ratings'),
    path( 'student/connectivity/', views.connection_page, name='connection_timeframe_page' ),
]
