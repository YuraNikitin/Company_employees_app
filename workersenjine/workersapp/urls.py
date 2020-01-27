from django.urls import path
from .views.worker import *
from .views.department import *
from .views.alphabet import AlphabetList

urlpatterns = [
    path('', WorkerList.as_view(), name='worker_list_url'),
    path('worker/create/', WorkerCreate.as_view(), name='worker_create_url'),
    path('works/', WorkerFilter.as_view(), name='worker_filter_url'),
    path('worker/<str:slug>/', WorkerListDetail.as_view(), name='worker_detail_url'),
    path('worker/<str:slug>/update/', WorkerUpdate.as_view(), name='worker_update_url'),
    path('worker/<str:slug>/delete/', WorkerDelete.as_view(), name='worker_delete_url'),

    path('department/create/', DepartmentCreate.as_view(), name='department_create_url'),
    path('department/<str:slug>/', DepartmentDetail.as_view(), name='department_detail_url'),
    path('department/<str:slug>/update/', DepartmentUpdate.as_view(), name='department_update_url'),
    path('department/<str:slug>/delete/', DepartmentDelete.as_view(), name='department_delete_url'),


    path('alphabet/<str:group>/', AlphabetList.as_view(), name='alphabet_url'),




]