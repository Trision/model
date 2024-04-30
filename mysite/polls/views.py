from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import Template
import json
# Create your views here.

def index(request):
    return HttpResponse("Hello, Wolrd. You're at index page")

def webhook_view(request):
    if request.method:
        # Get the webhook data from the request body
        data = json.loads(request.body.decode('utf-8'))
        # Process the webhook data (e.g. save it to a database)
        print(data)
        return HttpResponse('Webhook received!', status=200)
    else:
        return HttpResponse('Invalid request method', status=405)