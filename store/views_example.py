from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views import View


def index(request):
    # if request.method == "GET":
    #     text = "This is a GET request."
    # elif request.method == "POST":
    #     text = "This is a POST Request."

    logged_in = request.user.is_authenticated
    if logged_in:
        text = (f'Welcome to our store, {request.user}')
    return HttpResponse(text)


def test_view(request):
    response = HttpResponse()
    if request.user.is_authenticated:
        response.write(f"Welcome, {request.user}")
    else:
        response.write("Please log in.")
    return response

@require_http_methods(["PUT", "GET"])
def browse(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/store/test')
    else:
        return HttpResponse('Hello.')
    


class SimpleClassBasedView(View):
    http_method_names = ["DELETE", "GET"]

    def get(self, request):
        text = "This is a GET request."
        if request.user.is_authenticated:
            text = f"Welcome to Class Based Views, {request.user}"
        return HttpResponse(text)
    
    def post(self, request):
        text = "This is a POST request"
        return HttpResponse(text)