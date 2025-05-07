from django.shortcuts import render, redirect
from .models import Info

def index(request):
    return render(request, 'index.html')

def user_info_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        country = request.POST.get('country')

        # Example: basic manual validation
        if name and email and age and gender and country:
            # Optional: check for unique email
            if not Info.objects.filter(email=email).exists():
                Info.objects.create(
                    name=name,
                    email=email,
                    age=age,
                    gender=gender,
                    country=country
                )
                return render(request, 'success.html', {'user_name': name})
            else:
                error = "This email is already registered."
                return render(request, 'index.html', {'error': error})
        else:
            error = "Please fill all fields correctly."
            return render(request, 'index.html', {'error': error})

    return render(request, 'index.html')
