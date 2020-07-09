from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from twilio.rest import Client 
from .models import mainform
# Create your views here.
def index(request):
    return render(request,'home.html')
def tester(request):
    return render(request,'home.html')
def log(request):
    return render(request, 'login.html')
def reg(request):
    return render(request,'register.html')
def login(request):
    v4=request.POST["user_namee"]
    v5=request.POST["passs"]
    user=authenticate(username=v4,password=v5)
    if user is not None:
        P = mainform.objects.all()
        content={'P':P,'user':v4}
        return render(request,'main.html',content)
    else:
        return render(request,'login.html')
def registerr(request):
    v1=request.POST["user_name"]
    v2=request.POST["pass"]
    v3=request.POST["email"]
    v4=request.POST["phone"]
    user=User.objects.create_user(username= v1,email= v3,password= v2)
    user.save();
    
 
    account_sid = 'ACbcea9c59574a613760875bfa4835cb79' 
    auth_token = 'f26200c759bab151cb91bbacfeedd29d' 
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create( 
                              from_='+15104220161',  
                              body='   user:   '+ v1 +'  You have successfully completed joining our CodeVipers community and this will make your job life a lot easier. If you are preparing for the interviews this is a great chance to overcome the tension and make your goal possible in the eleventh hour.  ',      
                              to='+918688951346' 
                          ) 
 
    print(message.sid)
    return render(request,'home.html')
def info(request):
    
    P=mainform.objects.all()
    content={'P':P,'user':"avnmht"}
    return render(request,'main.html',content)
def mainformer(request):
    v1=request.POST.get("U",False)
    try:
        u=mainform.objects.get(Username=str(v1))
    except mainform.DoesNotExist:
        u = None
    if u is None:
        v12=request.POST["fullnamer"]
        v2=request.POST["ingamenamer"]
        v3=request.POST["regionr"]
        v4=request.POST["phonenumber1r"]
        v5=request.POST["characteridr"]
        v6=request.POST["kperdr"]
        v7=request.POST["yourtierr"]
        v8=request.POST["gameserverr"]
        if v8=="ASIA" or v8=="N.A" or v8=="S.A": 
            v9=request.POST["winpermatchesr"]
            v10=request.POST["tpporfpp"]
            v11=request.POST["insquadr"]
            v2=v2.lower()
            v3=v3.lower()
            v4=v4.lower()
            v5=v5.lower()
            v6=v6.lower()
            v7=v7.lower()
            v8=v8.lower()
            v9=v9.lower()
            v10=v10.lower()
            v11=v11.lower()
            kk= mainform.objects.create(Username=v1,fullname=v12,ingamename=v2,region=v3,phone=v4,characterid=v5,kperd=v6,yourtier=v7,gameserver=v8,winpermatches=v9,tpporfpp=v10,insquad=v11)
            P = mainform.objects.all()
            content={'P':P,"user":v1}

            return render(request,'main.html',content)
        else:
            P = mainform.objects.all()
            content={'P':P,"user":v1}

            return render(request,'main.html',content)
    else:
        v=request.POST["fullnamer"]
        v2=request.POST["ingamenamer"]
        v3=request.POST["regionr"]
        v4=request.POST["phonenumber1r"]
        v5=request.POST["characteridr"]
        v6=request.POST["kperdr"]
        v7=request.POST["yourtierr"]

        v8=request.POST["gameserverr"]
        if v8=="ASIA" or v8=="N.A" or v8=="S.A": 
            v9=request.POST["winpermatchesr"]
            v10=request.POST["tpporfpp"]
            v11=request.POST["insquadr"]
            v2=v2.lower()
            v3=v3.lower()
            v4=v4.lower()
            v5=v5.lower()
            v6=v6.lower()
            v7=v7.lower()
            v8=v8.lower()
            v9=v9.lower()
            v10=v10.lower()
            v11=v11.lower()        
            u.Username=v1
            u.fullname=v
            u.ingamename=v2
            u.region=v3
            u.phone=v4
            u.characterid=v5
            u.kperd=v6
            u.yourtier=v7
            u.gameserver=v8
            u.winpermatches=v9
            u.tpporfpp=v10
            u.insquad=v11
            u.save()
            P = mainform.objects.all()
            content={'P':P,"user":v1}

            return render(request,'main.html',content)
        else:
            P = mainform.objects.all()
            content={'P':P,"user":v1}
            return render(request,'main.html',content)
def createformer(request):
    v1=request.POST.get("Uname",False)
    content={"uname":v1}
    return render(request,'mainform.html',content)
def theirformer(request):
    v1=request.POST.get('n', False)
    forms=mainform.objects.get(fullname=v1)
    content={'forms':forms}
    return render(request,'theirform.html',content)
def regioner(request):
    v1=request.POST["regionr"]
    v1=v1.lower()
    try:
        final=mainform.objects.filter(region=v1)

    except:
        final=None

    if(final==None or len(final)==0):
        booler=False
    else:
        booler=True
        
    content={"final":final,"booler":booler}
    return render(request,"regions.html",content)
def characterer(request):
    v1=request.POST["characterr"]
    v1=v1.lower()
    try:
        final=mainform.objects.filter(characterid=v1)
    except:
        final=None

    if(final==None or len(final)==0):
        booler=False
    else:
        booler=True
    content={"final":final,"booler":booler}
    return render(request,"characters.html",content)
def tierer(request):
    v1=request.POST["tierr"]
    v1=v1.lower()
    try:
        final=mainform.objects.filter(yourtier=v1)
    except:
        final=None
    if (final==None or len(final)==0):
        booler=False
    else:
        booler=True
    content={"final":final,"booler":booler}
    return render(request,"tiers.html",content)
def ingamenameer(request):
    v1=request.POST["ingamer"]
    v1=v1.lower()
    try:
        final=mainform.objects.filter(ingamename=v1)
    except:
        final=None
    if (final==None or len(final)==0):
        booler=False
    else:
        booler=True
    content={"final":final,"booler":booler}
    return render(request,"ingamenames.html",content)
def kperder(request):
    final=mainform.objects.order_by('-kperd')
    content={"final":final}
    return render(request,"kperds.html",content)