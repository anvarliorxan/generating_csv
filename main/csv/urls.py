from django.urls import path, include
from . import views

app_name = 'csv'

urlpatterns = [
    path('csv-list', views.csvList, name='cvs-list'),
    path('add-csv-data', views.addCsvData, name='add-csv-data'),
    path('delete-csv-data/<str:id>/', views.deleteCsvData, name='delete-csv-data'),
    path('edit-csv-data/<str:id>/', views.editCsvData, name='edit-csv-data'),
    path('edit-csv-data/<str:id>/', views.editCsvData, name='edit-csv-data'),
    path('generate-data-csv/<str:id>/', views.generateDataToCsv, name='generate-data-csv'),

]
