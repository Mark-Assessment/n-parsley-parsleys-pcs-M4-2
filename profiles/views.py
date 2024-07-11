from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserDefaults
from .forms import UserDefaultsForm
from checkout.models import Order

@login_required
def profile(request):
    user_defaults, created = UserDefaults.objects.get_or_create(user=request.user)
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    if request.method == 'POST':
        form = UserDefaultsForm(request.POST, instance=user_defaults)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserDefaultsForm(instance=user_defaults)
    
    return render(request, 'profiles/profile.html', {'form': form, 'orders': orders})