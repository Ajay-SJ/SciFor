from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.conf import settings
from subscription.forms import SubscribeForm

# Create your views here.
def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Django Email Send Demo'
            message = 'Sending Email through Gmail'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('subscribe')
    return render(request, 'home.html', {'form': form})
