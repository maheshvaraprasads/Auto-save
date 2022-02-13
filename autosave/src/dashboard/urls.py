from django.urls import path
from .import views


app_name = 'dashboard'

urlpatterns = [
    path('welcome/',views.dashboard,name='dashboard'),

   
    #---work-on-edit-view------#
    path('data/apply/',views.data_creation,name='createdata'),
    
    path('datas/view/table/',views.view_my_data_table,name='staffdatatable'),
    # BIRTHDAY ROUTE
   



]
