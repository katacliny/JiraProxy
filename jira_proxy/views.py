from django.shortcuts import render
from django.http import HttpResponse
from urllib import parse
from django.views.decorators.csrf import csrf_exempt

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
    
    
    return HttpResponse("OK")

