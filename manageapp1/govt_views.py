from django.contrib import messages
from django.shortcuts import render, redirect
from .filters import PlaceFilter, ComplaintsFilter
from .models import Complaints, Appointment, AppointmentSchedule, Uploads


def govt_home(request):
    return render(request, 'govbase.html')


def cmp_gov(request):
    n = Complaints.objects.all()
    complaintsFilter = ComplaintsFilter(request.GET, queryset=n)
    n=complaintsFilter.qs
    context = {
        'complaints': n,
        'complaintsFilter': complaintsFilter,
    }
    return render(request, 'govt_cmp_view1.html', context)


def reply_complaint(request, id):
    complaint = Complaints.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaint.reply = r
        complaint.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('cmp_gov')
    return render(request, 'gov_cmp_reply.html', {'complaint': complaint})


def appointment_admin(request):
    p = Appointment.objects.all()
    placeFilter = PlaceFilter(request.GET, queryset=p)
    p = placeFilter.qs
    context = {
        'appointment': p,
        'placeFilter': placeFilter,
    }
    return render(request, 'govt_appointment.html', context)


def approve_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_admin')


def reject_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_admin')


def certificate(request, id):
    uploads = Uploads.objects.get(id=id)
    if request.method == 'POST':
        c = request.POST.get("reply")
        uploads.reply = c
        uploads.save()
        messages.info(request,'certificate/document is send to user')
        return redirect('cmp_gov')
    return render(request,'gov_certificate_issue.html', {'uploads':uploads})
