from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import SerializedArticle
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def article_list(request):
    if (request.method == 'GET'):
        articles = Article.objects.all()
        serializer = SerializedArticle(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif (request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = SerializedArticle(data=data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.error, status=400)


def index(request):
    return HttpResponse("this is the page")
