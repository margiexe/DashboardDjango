from django.urls import  path
from . import views

urlpatterns = [
    path('',views.index,name="services"),
    path('add-service',views.add_service,name="add-services"),
    path('edit-service/<int:id>',views.edit_service,name="edit-service"),
    path('service-delete/<int:id>',views.service_delete,name="service-delete"),
    path('reports-plots',views.reports_plots,name="reports-plots"),
    path('stats',views.stats_view,name="stats")
]