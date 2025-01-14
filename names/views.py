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
    response = render(request, 'names/index.html', context)
    names = []  # Clear the names list after rendering
    request.session.flush()  # Clear the session after rendering
    return response

def random_name(request):
    names = request.session.get('names', [])
    if names:
        selected_name = random.choice(names)
    else:
        selected_name = None
    request.session.flush()  # Clear the session after rendering
    return render(request, 'names/random_name.html', {'selected_name': selected_name})
