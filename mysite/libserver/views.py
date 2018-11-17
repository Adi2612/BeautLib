from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def test(request):
	return render(request , 'libserver/index.html' , { })

def myfriend(request, p_n):
	# image_data = open("images/Adi2612.jpeg", "rb").read()
	return HttpResponse("image_data", content_type="text")