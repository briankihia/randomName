from django.shortcuts import render, redirect
import random

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            if 'names' not in request.session:
                request.session['names'] = []
            request.session['names'].append(name)
            request.session.modified = True
        return redirect('index')
    
    names = request.session.get('names', [])
    return render(request, 'names/index.html', {'names': names})

def random_name(request):
    names = request.session.get('names', [])
    if names:
        selected_name = random.choice(names)
    else:
        selected_name = None
    return render(request, 'names/random_name.html', {'selected_name': selected_name})
