from django.urls import path
from django.http.response import HttpResponse

def test(request):
    return HttpResponse("HELLO!")

urlpatterns = [
    path("test", test)
]