from django.shortcuts import render ,redirect,get_object_or_404
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


def delete(request, id):
    if request.method == 'POST':
      post = get_object_or_404(Poster, id=id)  # Fetch the post to delete
      post.delete()  # Delete the post
      return redirect(home)  
    
    else:
      return redirect('home')


 