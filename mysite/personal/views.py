from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'personal/Sample/index.html')

def contact (request):
    return render(request, 'personal/Sample/basic.html', {'content': ['If you would like to contact me, please call me','sesantakuro29@gmail.com']} )
