from . import views
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    path('mechanics/', views.mechanic, name='mechanics'),
    path('mechanics/<int:mechanic_id><str:mechanic_name>', views.mechanic_info, name='mechanic_info'),
    path('months', views.months, name='months'),
    path('months/<int:month_id><str:month_name>', views.month_info, name='month_info'),
    path('timetable/', views.timetable, name='time_table'),
    path('create_timetable/', views.create_timetable, name='create_timetable'),
    path('add_mechanic/', views.add_mechanic, name='add_mechanic'),
    path('mod_mechanic/<int:mechanic_id>', views.modify_mechanic, name='mod_mechanic'),
    path('choose_month/', views.choose_month, name='choose_month'),
    path('mod_timetable/<int:timetable_id>', views.modify_timetable, name='mod_timetable'),


]

