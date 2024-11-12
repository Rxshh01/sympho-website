from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
from cityplan_app.models import cityplan_reg
from threemtt.models import threemtt
## import data tables from database
from .models import Submission,iitb,non_iitb
from poster_app.models import poster_class

# Create your views here.

def home(request):
    return render(request, "home_new.html")

def main_view1(request):
    return render(request, "index.html")

def new(request):
    return render(request, "new.html")

def academic_home(request):
    return render(request,"academic.html")
#def poster_view(request):
#    return render(request,"poster.html")

def submission(request):
    return render(request, "submission.html")

def main_view(request):
    user = request.user
    is_filled_mtt=False
    is_filled_cityplan = False
    is_filled_poster=False
    submit_form=False
    if user.is_authenticated:
        email = user.email
        is_filled_cityplan = len(cityplan_reg.objects.filter(email1=email))==1
        is_filled_mtt = len(threemtt.objects.filter(email=email))==1
        is_filled_poster = len(poster_class.objects.filter(email=email))==1

    print(is_filled_cityplan)
    return render(request, "sympo_main.html",
    {
        'is_filled_cityplan':is_filled_cityplan,
        'submit_form':submit_form,
        'is_filled_mtt':is_filled_mtt,
        'is_filled_poster':is_filled_poster
    })


#   response = redirect('/paper/')
#   return render(request,"sympo_main.html")

def submitted(request):
    if request.method == "POST":
        user = request.user
        author = request.POST.get('author', '')
        email = user.email
        colgName = request.POST.get('colgName', '')
        degree = request.POST.get('degree', '')
        mobileNo = request.POST.get('mobileNo', '')
        co1 = request.POST.get('co1', '')
        mail1 = request.POST.get('mail1', '')
        co2 = request.POST.get('co2', '')
        mail2 = request.POST.get('mail2', '')
        co3 = request.POST.get('co3', '')
        mail3 = request.POST.get('mail3', '')
        field = request.POST.get('field', '')
        title = request.POST.get('title', '')
        others = request.POST.get('others', '')
        abstract = request.FILES.get('abstract', '')
        authentication = request.FILES.get('authentication', '')
        referral = request.POST.get('referral', 'NA')

        object = Submission.objects.all()
        isfill= False
        for obj in object :
            if obj.email==email:
                object = Submission.objects.get(email=email)
                object.delete()
                response = Submission(author=author, email=email, colgName=colgName,  degree=degree, mobileNo=mobileNo,
                              co1=co1, mail1=mail1, co2=co2, mail2=mail2, co3=co3, mail3=mail3, field=field, title=title, others=others, abstract=abstract, authentication=authentication, referral=referral)
                response.save()
                isfill =True
                break
        if not isfill : 
            response = Submission(author=author, email=email, colgName=colgName,  degree=degree, mobileNo=mobileNo,
                              co1=co1, mail1=mail1, co2=co2, mail2=mail2, co3=co3, mail3=mail3, field=field, title=title, others=others, abstract=abstract, authentication=authentication, referral=referral)
            response.save()
        

    return  redirect('home')

def iitb_view(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        contact = request.POST.get('contact', '')
        ldap = request.POST.get('ldap', '')
        roll = request.POST.get('roll_no', '')
        department= request.POST.get('department', '')
        final = iitb(name=name, contact=contact,ldap=ldap,roll=roll,department=department)
        # if len(iitb.objects.filter(ldap=ldap))==1:
	    #     return HttpResponse('this ldap is already registered')
        
        final.save()
    # return redirect('academic_writting')
    return render(request,'academic.html',{'filled_acad':True})

def noniitb_view(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        college= request.POST.get('college', '')
        transaction_id= request.POST.get('transaction_id', '')
        payment_screenshot= request.FILES.get('payment_screenshot', '')
        data = non_iitb(name=name,email=email,contact=contact,college=college,transaction_id=transaction_id,payment_screenshot=payment_screenshot)
        if len(non_iitb.objects.filter(email=email))==1:
            return HttpResponse("this email is already registered")
        data.save()
            
    # return redirect('academic_writting')
    return render(request,'academic.html',{'filled_acad':True})
