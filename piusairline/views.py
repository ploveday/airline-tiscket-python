from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import forms as airlineForm, models as airlineModel
# from django.core import serializers
from django.contrib.auth.decorators import login_required,permission_required

def index(request):
    return render(request, "piusairline/index.html")

@login_required
def booking(request):
    bookinf = {}
    thisTicketInfo = {}
    if request.method == 'POST':
        # booknow = airlineModel.Sales
        deDate = request.POST['deDate']
        bookinf['buyerID'] = request.user.id
        bookinf['ticketID'] = request.POST['deDate']
        bookinf['paymentType'] = request.POST['mpayment']
        thisTicketInfo = airlineModel.Tickets.objects.filter(id=deDate).values()
        
    aTickets = airlineModel.Tickets.objects.filter(status=1)#.all()
    # form = UserCreationForm()
    context = {
        'bookinf':bookinf,
        'tickets':aTickets,
        'ticketinf':thisTicketInfo
    }
    
    return render(request, 'piusairline/booking.html', context)

def save_bookng(request):
    bookstu = 0
    bookmsg = ""
    if request.method == 'POST':
        tbook = airlineModel.Sales()
        try:
            tbook.buyerID = request.POST['buyerID']
            tbook.ticketID = request.POST['ticketID']
            tbook.paymentType = request.POST['paymentType']
            tbook.save()
            bookstu = 1
        except Exception as ex:
            bookmsg = ex
            bookstu = 0
        else:
            bookstu = 1
        context = {
            'bookstu':bookstu,
            'bookmsg':bookmsg
        }
        return render(request, 'piusairline/booking.html', context)

def newUser(request):
    # tot_users = len(User.objects.all())+1
    if request.method == 'POST':
        form = airlineForm.RegForm(request.POST)
        detail_form = airlineForm.DetailsForm(request.POST, instance=airlineModel.Usersdetails())
        if form.is_valid() and detail_form.is_valid():            
            usernames = request.POST['username']
            passwords = request.POST['password1']
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            email = request.POST['email']
            new_user = User.objects.create_user(username=usernames,password=passwords,last_name=lname,first_name=fname,email=email)
            new_user.save()
            # user_form = form.save()
            new_detail_form = detail_form.save(commit=False)
            new_detail_form.user = new_user
            new_detail_form.save()
            # if form.has_error:
            #     regError = form._errors
            #     return render(request, 'piusairline/register.html', {'form':form, 'err':regError})
            return redirect('index')
        # invalid form data with error
        else:            
            context = {
                'form':form, 
                'err':form._errors,
                'dform':detail_form
                }
            return render(request, 'piusairline/register.html', context)
    else:
        form = airlineForm.RegForm()
        detail_form = airlineForm.DetailsForm()
        context ={
            'form':form,
            'dform':detail_form
        }
        return render(request, 'piusairline/register.html', context)

def flights(request):
    # allusers = User.objects.get(id=3)
    allusers = User.objects.all()
    totUsr = len(allusers)
    # print(f'Total Registerd Users in Pius Airline is{totUsr}')
    return render(request, 'piusairline/flights.html', { 'flights':allusers, 'totUsr':totUsr })

@login_required
def userprofile(request):
    return render(request, "piusairline/userprofile.html")

@login_required
def actinfo(request):
    myinfo = airlineModel.Usersdetails.objects.get(user_id=request.user.id)
    # cuser = User.objects.get_by_natural_key    
    # print(f"TESTIN DJANGO MODELS {myinfo}")
    context={
        'myinfo':myinfo,
    }
    return render(request, "piusairline/view.html", context)

# @login_required
# @permission_required('User.is_superuser', login_url='/illegal/', raise_exception=False)
def newTicket(request):
    if not request.user.is_superuser:
        notauth = "You do not have the required previledge to access this section<br> If this is an error, try logout and re-login"
        return render(request,"piusairline/index.html",{'none':notauth})
    newTicketStatus = ""
    mtype = 1# This is to determin the type of message to give the user
    if request.method == 'POST':
        form = airlineForm.CreateTicketForm(request.POST)               
        if form.is_valid():   
            thisTicket = form.save(commit=False) #Get form data But not save in DB
            thisTicket.status = 1
            thisTicket.ticketAuthor = request.user.id
            thisTicket.destinationState = request.POST['destinationState']
            thisTicket.destinationCountry = request.POST['destinationCountry']
            thisTicket.departureCountry = request.POST['departureCountry']
            thisTicket.departureState = request.POST['departureState'] 
            thisTicket.destinationAirport = request.POST['destinationAirport'] 
            thisTicket.departureAirport = request.POST['departureAirport'] 
            try:
                thisTicket.save()#Now Commit to DB after adding Extra Values                
            except Exception as ex:
                print('SAVING ERROR: '+ex)
                newTicketStatus = ex
                mtype = 3
            else:
                mtype = 2
                newTicketStatus = "New Ticket was saved successfully"
        else:
            mtype = 3
            newTicketStatus = form.errors

    form = airlineForm.CreateTicketForm
    context={
        'form':form,
        'msg':mtype,
        'emsg':newTicketStatus
    }
    return render(request, "piusairline/creatticket.html", context)

@login_required
def vewTicket(request, pk=None):    
    if not request.user.is_superuser:
        notauth = "You do not have the required previledge to access this section<br> If this is an error, try logout and re-login"
        return render(request,"piusairline/index.html",{'none':notauth})
    aticket = None
    if pk:
      aticket = airlineModel.Tickets.objects.get(pk=pk)

    context = {
        'tickets':airlineModel.Tickets.objects.all(),
        'tdetail':aticket
    }
    return render(request,"piusairline/seetickets.html",context)


