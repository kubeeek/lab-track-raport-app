from django.shortcuts import redirect
from django.urls import path

from . import views

urlpatterns = [
    path('', lambda request: redirect('test_sample_create', permanent=True)),

    # ex: /test-sample/create/
    path('test-sample/create', views.TestSampleCreateView.as_view(), name="testsample_create"),
    path('test-sample/', views.TestSampleListView.as_view(), name="testsample_list"),
    path('test-sample/<int:pk>/', views.TestSampleDetailView.as_view(), name="testsample_detail"),
    path('test-sample/<int:pk>/update', views.TestSampleUpdateView.as_view(), name="testsample_update"),
    path('test-sample/<int:pk>/delete', views.TestSampleDeleteView.as_view(), name="testsample_delete"),

    path('test-sample/<int:pk>/test-label/add', views.TestLabelCreateView.as_view(), name="add_related_testlabel"),

    path('test-sample/export', views.TestSampleExportFormView.as_view(), name="testsample_export"),
    path('test-sample/export/download', views.TestSampleExportView.as_view(), name="testsample_export_download"),

    # ex: /test-label/1/
    path('test-label/<int:pk>/', views.TestLabelDetailView.as_view(), name="testlabel_detail"),
    path('test-label/<int:pk>/update', views.TestLabelUpdateView.as_view(), name="testlabel_update"),
    path('test-label/<int:pk>/delete', views.TestLabelDeleteView.as_view(), name="testlabel_delete"),

    path('test-label/export', views.TestLabelExportFormView.as_view(), name="testlabel_export"),
    path('test-sample/export/download', views.TestSampleExportView.as_view(), name="testlabel_export_download"),

    # path('test-label/add', views.TestLabelCreateView.as_view())
]
