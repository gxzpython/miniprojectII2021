from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse

from .models import Group,Event,People

from .forms import RegisterForm
# Create your views here.
def homepage(request):
    template = loader.get_template('society/homepage.html')
    return HttpResponse(template.render({},request))

def register(request):
    if request.method =='POST':
        register_form=RegisterForm(request.POST,request.FILES)
        if register_form.is_valid():
            register_form.save()
        context={
            "form": register_form,
            "img_obj":register_form.instance
        }
        return render(request,'society/register.html',context)
    else:
        register_form=RegisterForm()
        return render(request,'society/register.html',{'form':register_form})

def group(request):
	group=Group.objects.all()
	template = loader.get_template('society/group.html')
	
	context = {
		'group':group,
	}
	return HttpResponse(template.render(context,request))

def event(request):
    event=Event.objects.all()
    event_count = Event.objects.count()
    template = loader.get_template('society/event.html')
    context = {
		'event':event,
        'number':event_count,
	}
    return HttpResponse(template.render(context,request))


def people(request):
	people=People.objects.all()
	template = loader.get_template('society/people.html')
	context = {
		'people':people,
	}
	return HttpResponse(template.render(context,request))

def group_detail(request,group_id):
    group_detailview= Group.objects.get(id=group_id)
    template=loader.get_template('society/group_detail.html')
    creator=People.objects.all()
    context={
        'group_detailview':group_detailview,
        'creator':creator

    }
    return HttpResponse(template.render(context,request))

def event_detail(request,event_id):
    event_detailview= Event.objects.get(id=event_id)
    template=loader.get_template('society/event_detail.html')

    context={
        'event_detailview':event_detailview,
    }
    return HttpResponse(template.render(context,request))


def people_detail(request,people_id):
	people_detailview= People.objects.get(id=people_id)
	template=loader.get_template('society/people_detail.html')
	context={
		'people_detailview':people_detailview
	}
	return HttpResponse(template.render(context,request))

