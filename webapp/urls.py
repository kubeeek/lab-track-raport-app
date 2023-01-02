from django.shortcuts import redirect
from django.urls import path

from . import views

urlpatterns = [
    path('', lambda request: redirect('testsample_add', permanent=True)),

    # ex: /test-sample/add/
    path('test-sample/add', views.TestSampleCreateView.as_view(), name="testsample_add"),
    path('test-sample/', views.TestSampleListView.as_view(), name="testsample_list"),
    path('test-sample/<int:pk>/', views.TestSampleDetailView.as_view(), name="testsample_detail"),
    path('test-sample/<int:pk>/test-label/add', views.TestLabelCreateView.as_view(), name="add_related_testlabel"),

    path('test-sample/export', views.TestSampleExportView.as_view(), name="testsample_export"),
    # ex: /test-label/1/

    # path('test-label/add', views.TestLabelCreateView.as_view())
]
