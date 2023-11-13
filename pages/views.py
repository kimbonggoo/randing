from django.shortcuts import render, redirect
from .models import Data
from .forms import DataForm

# Create your views here.
def userdata(request):
    print(request.POST)
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:index')
    else:
        form = DataForm()

    return render(request, 'pages/index.html', {
        'form': form,
    })