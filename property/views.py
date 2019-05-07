from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

#from .serializers import PropertySerializer
#from rest_framework import viewsets

from .models import *
#from .permissions import IsOwnerOrReadOnly

#from .forms import ContactForm
# Create your views here.
def index(request):
    kind = request.GET.get('kind', '')
    place = request.GET.get('place', '')
    #floor = request.GET.get('floor', '')
    floor1 = request.GET.get('floor1', '')
    floor2 = request.GET.get('floor2', '')
    area1 = request.GET.get('area1', '')
    area2 = request.GET.get('area2', '')
    price1 = request.GET.get('price1', '')
    price2 = request.GET.get('price2', '')
    sale = request.GET.get('sale', '')
    fitted = request.GET.get('fitted', '')
    furnished = request.GET.get('furnished', '')
    featured = request.GET.get('featured', '')

    print ("==============================================")
    print (kind)

    query = Property.objects.all().order_by('id')
    if kind != '':
        if kind != '-1':
            query=query.filter(type=kind)
        if place != '-1':
            query=query.filter(place=place)
        #if floor != '-1':
        #    query=query.filter(floor=floor)

        if area1 !='':
            query=query.filter(area__gte=area1)

        if area2!='':
            query=query.filter(area__lte=area2)

        if floor1 !='':
            query=query.filter(floor__gte=floor1)

        if floor2!='':
            query=query.filter(floor__lte=floor2)

        if price1 !='':
            if sale == '1':
                p1=int(price1)*int(1000000)
                query=query.filter(price__gte=p1)
            if sale == '2':
                p1=int(price1)*int(1000)
                query=query.filter(price__gte=p1)
            #query=query.filter(price__gte=price1, price__lte=price2)

        if price2!='':
            if sale == '1':
                p2=int(price2)*int(1000000)
                query=query.filter(price__lte=p2)
            if sale == '2':
                p2=int(price2)*int(1000)
                query=query.filter(price__lte=p2)

        if sale == '1':
            query=query.filter(forSale=True)
        else:
            query=query.filter(forSale=False)

        if fitted == '1':
            query=query.filter(fitted=True)

        if furnished == '1':
            query=query.filter(furnished=True)

    if featured =='1':
        query=query.filter(featured=True)

    query=query.filter(display=True)

    query=query.order_by('-date')
    context_instance=RequestContext(request)
    if kind!='-1' and kind!='':
        context_instance['kind']=PropertyType.objects.get(id=kind)
    else:
        context_instance['kind']='-1'

    if place!='-1' and place!='':
        context_instance['place']=PropertyPlace.objects.get(id=place)
    else:
        context_instance['place']='-1'

    #if floor!='-1' and floor!='':
    #    context_instance['floor']=PropertyFloor.objects.get(id=floor)
    #else:
    #    context_instance['floor']='-1'


    context_instance['area1']=area1
    context_instance['area2']=area2
    context_instance['price1']=price1
    context_instance['price2']=price2

    context_instance['floor1']=floor1
    context_instance['floor2']=floor2

    context_instance['sale']=sale
    context_instance['fitted']=fitted
    context_instance['furnished']=furnished
    context_instance['featured']=featured

    context_instance['search_results']=query

    return render_to_response('propertyhome.html',context_instance)
#    return render_to_response('propertyhome.html',RequestContext(request))

def featuredproperties(request):
    query = Property.objects.all().order_by('-date')
    query=query.filter(featured=True)

    query=query.filter(display=True)
    context_instance=RequestContext(request)
    context_instance['search_results']=query
    return render_to_response('propertyhome.html',context_instance)

def propertyDetails(request):
    pid = request.GET.get('id', '')
    query = Property.objects.get(id=pid)
    context_instance=RequestContext(request)
    context_instance['item']=query
    #query2 = Seller.objects.get(id=query.seller)
    return render_to_response('propertyDetails.html',context_instance)

def requests(request):
    query = Contact.objects.all().order_by('-date')
    query=query.filter(type='request')
    query=query.filter(checked=True)
    query=query.filter(display=True)

    context_instance=RequestContext(request)
    #context_instance['search_results']=query

    # view only 10 requests per page
    pagenum = request.GET.get('pagenum', '')
    if pagenum=='':
        pagenum=1

    startingindex=(int(pagenum)-1)*int(10)
    if startingindex > (int(query.count())-1):
        startingindex=0

    endingindex=startingindex+9

    if endingindex > (int(query.count())-1):
        endingindex=int(query.count())-1

    pp=int(query.count())/(int(10))
    numOfPages=int(pp)+1

    context_instance['startingindex']=startingindex
    context_instance['endingindex']=endingindex

    context_instance['search_results']=query[startingindex:(endingindex+1)]
    context_instance['pagenum']=int(pagenum)
    context_instance['numOfPages']=reversed(range((numOfPages+1)))
    context_instance['maxPages']=numOfPages
    context_instance['nextPage']=int(pagenum)+1
    context_instance['previousPage']=int(pagenum)+1

    return render_to_response('requests.html',context_instance)

def contactus(request):
    pid = request.GET.get('id', '')
    req = request.GET.get('request', '')
    context_instance=RequestContext(request)
    context_instance['req']=req
    if pid!='' and req!='1':
        query = Property.objects.get(id=pid)
        context_instance['item']=query

    if pid!='' and req=='1':
        query = Contact.objects.get(id=pid)
        context_instance['item']=query

    na = request.GET.get('name', '')
    em = request.GET.get('email', '')
    ph = request.GET.get('phone', '')
    su = request.GET.get('subject', '')
    me = request.GET.get('message', '')



    context_instance['result']=-1
    if na!='':
        con = Contact(name=na,type='contact',phone=ph,email=em,subject=su,message=me)
        try:
            con.full_clean()
            con.save()
            context_instance['result']=1
        except:
            context_instance['result']=0
            context_instance['message']="خطأ في البيانات"



    return render_to_response('contactus.html',context_instance)

def offer(request):
    pid = request.GET.get('id', '')
    context_instance=RequestContext(request)

    na = request.GET.get('name', '')
    em = request.GET.get('email', '')
    ph = request.GET.get('phone', '')
    su = 'Offer a property'
    me = request.GET.get('message', '')

    context_instance['result']=-1
    if na!='':
        con = Contact(name=na,type='offer',phone=ph,email=em,subject=su,message=me)
        try:
            con.full_clean()
            con.save()
            context_instance['result']=1
        except:
            context_instance['result']=0
            context_instance['message']="خطأ في البيانات"



    return render_to_response('offer.html',context_instance)

def request(request):
    pid = request.GET.get('id', '')
    context_instance=RequestContext(request)

    na = request.GET.get('name', '')
    em = request.GET.get('email', '')
    ph = request.GET.get('phone', '')
    su = 'Request a property'
    me = request.GET.get('message', '')



    context_instance['result']=-1
    if na!='':
        con = Contact(name=na,type='request',phone=ph,email=em,subject=su,message=me)
        try:
            con.full_clean()
            con.save()
            context_instance['result']=1
        except:
            context_instance['result']=0
            context_instance['message']="خطأ في البيانات"



    return render_to_response('request.html',context_instance)

def home(request):
    title='Welcome'
    
    form = ContactForm(request.POST or None)
    context={
        "title":title,
        "form":form
        }
    if form.is_valid():
        #form.save()
        instance=form.save(commit=False)
        if not instance.phone:
            instance.phone="000000"

        for key in form.cleaned_data:
            print (key)
            print (":")
            print (form.cleaned_data.get(key))

        instance.save()
        print (instance.email)
        #print (instance.timestamp)
        context={
            "title":"Thank You",
            }


    return render(request,"propertyhome.html",context)
