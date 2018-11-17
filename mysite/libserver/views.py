from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from libserver.models import Product
from django.core import serializers


# Create your views here.
def test(request):
	add_ = Product.objects.order_by('created_date')
	data = list(Product.objects.values())
	return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})
	# return HttpResponse(add_, content_type="text")	
	# qs_json = serializers.serialize('json', add_)
	# # # return HttpResponse(qs_json, content_type='application/json')
	# return JsonResponse({'posts' : qs_json})

def myfriend(request, p_n):
	# image_data = open("images/Adi2612.jpeg", "rb").read()
	return HttpResponse("image_data", content_type="text")
