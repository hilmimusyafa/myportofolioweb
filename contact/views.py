from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Simpan data ke database
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']

            contact = Contact.objects.create(
                name = name,
                email = email,
                title = title,
                message = message
            )

            # Kirim email pemberitahuan (opsional)
            # ...

            return render(request, 'contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
