from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View


class TestView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        
        return JsonResponse(
            data={
                "message": "ok"
            },
            status=201
        )

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

