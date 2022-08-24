from diango.urls import path

urlpatterns = [
    path('hello_view/', django_api.views.HelloApiView.as_view());
]
