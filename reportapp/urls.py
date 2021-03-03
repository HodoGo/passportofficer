from django.urls import path

from reportapp import views

app_name = 'reportapp'

urlpatterns = [
    path('',views.people_list,name='people_list'),
    path('export_word/',views.export_word,name='export_word'),
    path('export_excel/',views.export_excel,name='export_excel'),
]
