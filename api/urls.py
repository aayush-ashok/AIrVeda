from django.urls import path,include
from . import views

urlpatterns = [
    # path('devices/',views.DeviceList,name='List Devices'),
    path('devices/',views.DeviceReq,name='API to Create Device / to List all Devices'),
    path('devices/<int:uid>',views.DeleteOrRetrive,name="API to Delete device / retrieve device"),
    path('devices/<int:uid>/readings/<str:parameter>/',views.date_filter,name = 'API to Return reading for a device'),
    path('devices-graph/',views.Visualization,name='API for Plotting Graph'),
]