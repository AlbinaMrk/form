from django.shortcuts import render
from .forms import MyForm

def page1(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = MyForm()
    context = {
        'form': form,

    }
    return render(request,'base.html',context)