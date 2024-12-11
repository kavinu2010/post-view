from django.shortcuts import render ,redirect
from .models import Poster
from .forms import PostForm



# from django.http import HttpResponse
# # Create your views here.
# def home(request):
#   return HttpResponse('welcome page')
def home(request):
  posti=Poster.objects.all()
  return render(request, 'home.html', {'posti':posti})

def userpost(request):
  if request.method=='POST':
    usepos=PostForm(request.POST)
    if usepos.is_valid():
      usepos.save()
      return redirect(home)
    
  else:
    usepos=PostForm()
  return render(request,'user.html',{'usepos':usepos})


