from django.urls import path

from showcase import views

app_name = 'showcase'

urlpatterns = [
    path('<slug:slug>/', views.ShowcaseDetailView.as_view(), name='showcase')
]
