from django.shortcuts import render, redirect

from .forms import GovernmentRegister


def gov_add(request):
    form=GovernmentRegister()
    if request.method == 'POST':
        form=GovenmentRegister(request.post)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'register.html',{'form':form})
