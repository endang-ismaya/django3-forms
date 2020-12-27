from django.shortcuts import render
from . import forms


# Create your views here.
def index(request):
    return render(request, 'app_formbasic/index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Validation Success!')
            print(f"Name: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Text: {form.cleaned_data['text']}")
        else:
            print("Form is not valid.")

        dtcontext = {'form': form}
        return render(request, 'app_formbasic/form_page.html', context=dtcontext)
    else:
        print('else')
        dtcontext = {'form': form}
        return render(request, 'app_formbasic/form_page.html', context=dtcontext)
