from django.urls import path
from .import views


urlpatterns=[

    path('reg',views.reg_agency),
    path('log',views.login_agency),
    path('vehicle',views.vehicle),
    path('card',views.card_vehicle),
    path('',views.home),
    path('profile',views.agency_profile),
    path('list',views.vehicles_list),
    path('update <str:u_id>',views.update_list,name='update1')
]