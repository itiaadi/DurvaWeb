from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *;
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def index(request):
    return render(request,'base/index.html')

def home(request):
    return render(request,'base/home.html')


def about(request):
    return render(request,'base/about.html')

def studio(request):

    category = request.GET.get('category')

    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()

    video = Video.objects.all()
    context = {'categories': categories,'photos':photos,'video':video}
    return render(request,'base/studio.html',context)


def blog(request):
    return render(request,'base/blog.html')

def contact(request):
    return render(request,'base/contact.html')


def photo(request,pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'base/photos.html',{'photo':photo})

def design(request):
    category = request.GET.get('category')

    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'photos':photos}
    return render(request,'base/design.html',context)

def video(request):
    video = Video.objects.all()

    context = {'video':video}
    return render(request,'base/motion.html',context)


def designd(request):
    des = DoodleDesign.objects.all()
    context = {'des': des}
    return render(request, 'base/doodledesign.html', context)



def bite(request):
    bit = DoodleBites.objects.all()
    context = {'bit': bit}
    return render(request, 'base/bites.html', context)


def sendEmail(request):

    if request.method == 'POST':

        template = render_to_string('base/email_template.html',{
            'name':request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        
        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['durwa123@gmail.com']
        )
        
        email.fail_silently=False
        email.send()
    return render(request, 'base/email_sent.html')