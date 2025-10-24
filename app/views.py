from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully, Feedback will be returned through filled Email Account')
            return redirect('index')
    form = ContactForm()  
    context = {
        'form':form,
    }
    return render(request, 'app/index.html', context)