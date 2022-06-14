from django.urls import path

from showcase import views

urlpatterns = [
    path('<slug:slug>/', views.ShowcaseDetailView.as_view(), name='showcase')
]
