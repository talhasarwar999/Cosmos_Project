from django.urls import path
from . import views


urlpatterns = [
      path('',views.index, name="index"),
      path('firm/',views.firm, name="firm"),
      path('news/',views.news, name="news"),
      path('viewnews/<str:title>',views.viewnews, name="viewnews"),
      path('values/',views.values, name="values"),
      path('projects/',views.projects, name="projects"),
      path('career/',views.career, name="career"),
      path('contact/',views.contact, name="contact"),
      path('viewprojects/<str:title>',views.viewprojects, name="viewprojects"),
      path('career/jobs/',views.alljobs, name="careerjob"),
      path('careers/jobs/<str:job_title>',views.viewjobs, name="careers"),
      path('jobapply/',views.jobapply, name="jobapply"),
      path('service/',views.service, name="service"),
      path('viewservice/<str:servicename>',views.viewservice, name="viewservice"),
      path('market/',views.market, name="market"),
      path('viewmarkets/<str:marketname>',views.viewmarkets, name="viewmarkets"),
      path('press_contact/',views.press_contact, name="press_contact"),
      path('academic_contact/',views.academic_contact, name="academic_contact"),
      path('career_contact/',views.career_contact, name="career_contact"),
      path('business_contact/',views.business_contact, name="business_contact"),
      path('others_contact/',views.others_contact, name="others_contact"),
]