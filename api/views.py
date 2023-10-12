from django.http import HttpRequest, HttpResponse
import json


def test_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        pass
    
    if request.method == 'POST':

        body = request.body.decode()
        data = json.loads(body)
        print(data)
        print(type(data))

    return HttpResponse("ok")
