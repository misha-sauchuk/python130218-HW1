from django.conf.urls import url
from . import views

urlpatterns = [
    url('mechanic', views.mechanic, name='mechanics'),
url('months', views.months, name='month'),
url('timetable', views.timetable, name='time_table'),


]
#
# path('', views.list_view, name='nums_list'),
# path('create/<int:number>', views.create_view, name='nums_create'),
# path('update/<int:number_id>/<int:value>', views.update_view, name='nums_update'),
# path('delete/<int:number_id>', views.delete_view, name='nums_delete'),
# path('books/add', views.Books, name='nums_delete'),