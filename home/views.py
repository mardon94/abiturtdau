from django.shortcuts import render, HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect

# Create your views here.
from home.models import Setting, Qabul, QabulForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = QabulForm(request.POST, request.FILES)
        if form.is_valid():
            data = Qabul()
            data.direction_of_study = form.cleaned_data['direction_of_study']
            data.name = form.cleaned_data['name']
            data.date_birth = form.cleaned_data['date_birth']
            data.place_birth = form.cleaned_data['place_birth']
            data.address = form.cleaned_data['address']
            data.phone = form.cleaned_data['phone']
            data.pasport = form.cleaned_data['pasport']
            data.study = form.cleaned_data['study']
            data.year = form.cleaned_data['year']
            data.diplom = form.cleaned_data['diplom']
            data.pasport_photo = form.cleaned_data['pasport_photo']
            data.diplom_photo = form.cleaned_data['diplom_photo']
            data.photo3x4 = form.cleaned_data['photo3x4']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
        #messages.success(request, 'Sizning xabaringiz qabul qilindi')
        return HttpResponseRedirect('/qabul')
    form = QabulForm
    setting = Setting.objects.get()
    context = {
        'form': form,
        'setting': setting,
    }

    return render(request, 'index.html', context)


def qabul_list(request):
    qabuls = Qabul.objects.all().order_by('-id')
    setting = Setting.objects.get()
    context = {
        'qabuls': qabuls,
        'setting': setting,
    }
    return render(request, 'qabul_list.html', context)
