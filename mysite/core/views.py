from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from .forms import PdfForm
from .models import Pdfs


class Home(TemplateView):
    template_name = 'home.html'


# Create your views here.
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def pdf_list(request):
    pdfs = Pdfs.objects.all()

    return render(request, 'pdf_list.html', {'pdfs': pdfs})


def pdf_upload(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/pdf")
    else:
        form = PdfForm()
    return render(request, 'upload_pdf.html', {'form': form})
