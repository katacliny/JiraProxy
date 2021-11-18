from django.shortcuts import render
from django.http import HttpResponse
from urllib import parse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def proxy_view(request):
    print(request)
    # print(dir(request))
    print(request.body)
    # print(request.content_params)
    # print(request.get_full_path())
    # print(request.get_raw_uri())
    parsed = parse.urlsplit(request.get_full_path())
    print(parse.parse_qs(parsed.query))
    url = 'http://51.75.147.46:1337/jira'
    body = request.body
    requests.post(url, data = body)
    
    
    return HttpResponse("OK")

