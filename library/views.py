
from django.shortcuts import render,redirect
from .forms import LibraryForm
from .models import Library
# Create your views here.
def books_list(request):
    book=Library.objects.all()
    return render(request,'library/books_list.html',{'book':book})

def books_form(request,id=0):
    if request.method=='GET':
        if id==0:
            form=LibraryForm()
        else:
            book=Library.objects.get(pk=id)
            form=LibraryForm(instance=book)
        return render(request,'library/books_form.html',{'form':form})
    else:
        if id==0:
            form=LibraryForm(request.POST)
        else:
            book=Library.objects.get(pk=id)
            form=LibraryForm(request.POST,instance=book)
              
        if form.is_valid():
            form.save()
        return redirect('/library/list')
def books_delete(request,id):
    book=Library.objects.get(pk=id)
    book.delete()
    return redirect('/library/list')