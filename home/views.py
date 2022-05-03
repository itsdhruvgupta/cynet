from home.models import event,winners, banner
from django.shortcuts import redirect, render , HttpResponse
import datetime

# Create your views here.
def index(request):
    event_data = event.objects.all()
    banner_data = banner.objects.all()
    
    date = event.objects.values('date_time')

    timeNow = datetime.datetime.now()


    dict = {'event_data':event_data, 'banner_data':banner_data}
    
    return render(request,'esport.html',dict)

def winners_page(request):
    winner_data = winners.objects.all()
    dict = {'winner_data':winner_data}
    return render(request,'winners.html',dict)


def event_registration(request):
   
    id = int(request.GET['id'])

    event_data = event.objects.filter(id=id)
    print(event_data)

    dict = {'event_data':event_data}
    return render(request,'event_registration.html',dict)

