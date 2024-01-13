from django.shortcuts import render, redirect
from .forms import ContactForm
from core.gov_notify import SendEmail
from django.db.models.functions import Cast
from django.db.models import DecimalField

from .models import StaffMembers


def index(request):
    return render(request, 'layouts/index.html')

def whoweare(request):
    return render(request, 'layouts/whoweare.html')

def at(request):
    return render(request, 'layouts/at.html')

def camps(request):
    return render(request, 'layouts/camps.html')

def flying(request):
    return render(request, 'layouts/flying.html')

def shooting(request):
    return render(request, 'layouts/shooting.html')

def sport(request):
    return render(request, 'layouts/sport.html')

def education(request):
    return render(request, 'layouts/education.html')

def news(request):
    return render(request, 'layouts/news.html')

def gallery(request):
    return render(request, 'layouts/gallery.html')

def resources(request):
    return render(request, 'layouts/resources.html')

def joincadet(request):
    return render(request, 'layouts/joincadet.html')

def joinstaff(request):
    return render(request, 'layouts/joinstaff.html')

def forParents(request):
    return render(request, 'layouts/informationParents.html')

def meetStaff(request):
    staff_members = StaffMembers.objects.all().filter(active=True).annotate(position_decimal=Cast('position', output_field=DecimalField(max_digits=10, decimal_places=0))).order_by('position_decimal', 'last_name', 'first_name', 'rank')
    ctx = {"staffMembers": staff_members}
    return render(request, 'layouts/meetStaff.html', ctx)

def contactus(request):
    if request.method == 'POST':
        if request.POST.get('submit'):
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                telephone = request.POST.get('telephone')
                purpose = form.cleaned_data['purpose']
                body = request.POST.get('message')
                if purpose == '1':
                    purpose = 'Intrested in joining as a cadet'
                    email_to = ['2445@rafac.mod.gov.uk']
                if purpose == '2':
                    purpose = 'Intrested in joining as a staff volunteer'
                    email_to = ['oc.2445@rafac.mod.gov.uk', 'adj.2445@rafac.mod.gov.uk']
                if purpose == '3':
                    purpose = 'Intrested in joining as a committee volunteer'
                    email_to = ['oc.2445@rafac.mod.gov.uk', 'adj.2445@rafac.mod.gov.uk']
                if purpose == '4':
                    purpose = 'Parent of a current cadet'
                    email_to = ['2445@rafac.mod.gov.uk']
                if purpose == '5':
                    purpose = 'Financial support'
                    email_to = ['oc.2445@rafac.mod.gov.uk', 'treasurer.2445@rafac.mod.gov.uk']
                if purpose == '6':
                    purpose = 'Report issue/bug on website/'
                    email_to = ['mikolaj.adamkiewicz100@rafac.mod.gov.uk']
                if purpose == '7':
                    purpose = 'Other'
                    email_to = ['2445@rafac.mod.gov.uk']
                for i in email_to:
                    SendEmail.send_email_notification_staff(email_to=i, full_name=first_name + " " + last_name, subject=purpose, email=email, tel_num=telephone, message=body, sent_to_list = email_to)
                SendEmail.send_email_notification_user(email_to=email, full_name=first_name + " " + last_name, subject=purpose, first_name=first_name)

        return redirect('contactus')

    if request.method == 'GET':
        form = ContactForm()
    ctx = {"form": form}
    return render(request, 'layouts/contactus.html', ctx)

def comingSoon(request):
    return render(request, 'layouts/error/soon.html')



#! *************** Error messages ***************

def pageNotFound(request, exception):
    context = {"code":"404", "type":"NOT FOUND"}
    return render(request, 'layouts/error/error.html', context)

def serverError(request):
    context = {"code":"500", "type":"SERVER ERROR"}
    return render(request, 'layouts/error/error.html', context)

def permissionDenied(request, exception):
    context = {"code":"403", "type":"FORBIDDEN"}
    return render(request, 'layouts/error/error.html', context)

def badRequest(request, exception):
    context = {"code":"400", "type":"BAD REQUEST"}
    return render(request, 'layouts/error/error.html', context)