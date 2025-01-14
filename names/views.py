from django.shortcuts import render, redirect
import random

names = []

def index(request):
    global names
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            names.append(name)
        return redirect('index')
    context = {'names': names}
    return render(request, 'names/index.html', context)

def random_name(request):
    global names
    if names:
        selected_name = random.choice(names)
    else:
        selected_name = None
    names = []  # Clear the names list after rendering
    return render(request, 'names/random_name.html', {'selected_name': selected_name})
