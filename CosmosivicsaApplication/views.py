from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.core.mail import  EmailMessage
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .filters import *
import random


# Create your views here.

def index(request):
    Latest_news = News.objects.all().order_by('-id')[:5]
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    get_image = Home_Page_Images.objects.all()
    get_video = Home_Page_Videos.objects.all()
    return render(request, "CosmosivicsaApplication/index.html",{'latest_news':Latest_news,'service':get_services,'market':get_markets,'image':get_image,'video':get_video})
def firm(request):
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    our_firm = Our_Firm.objects.all()
    return render(request, "CosmosivicsaApplication/firm.html",{'service':get_services,'market':get_markets,'our_firm':our_firm})

def news(request):
    AllNews = News.objects.all()
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    newfilter = NewsFilter(request.GET, queryset=AllNews)
    allfilter = newfilter.qs
    context = {'AllNews':allfilter, 'newfilter': newfilter,'service':get_services,'market':get_markets}
    return render(request, "CosmosivicsaApplication/news.html",context)

def viewnews(request,title):
    viewnew = News.objects.get(title=title)
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    related_news = viewnew.newsname.all()
    get_related_news = News.objects.filter(newsname__in=related_news).exclude(id=viewnew.id).distinct()[:3]
    related_countries = viewnew.countryname.all()
    get_related_projects = Project.objects.filter(countryname__in=related_countries).exclude(id=viewnew.id).distinct()[:3]
    content = {'viewnew':viewnew,'related_news':get_related_news,'get_related_projects':get_related_projects,'service':get_services,'market':get_markets}
    return render(request,"CosmosivicsaApplication/viewnews.html", content)

def viewprojects(request,title):
    viewprojects = Project.objects.get(title=title)
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    related_markets = viewprojects.marketname.all()
    related_services = viewprojects.servicename.all()
    related_countries = viewprojects.countryname.all()
    get_related_projects = Project.objects.filter(servicename__in=related_services,marketname__in=related_markets).exclude(id=viewprojects.id).distinct()[:3]
    get_related_news = News.objects.filter(countryname__in=related_countries).exclude(id=viewprojects.id).distinct()[:3]
    content = {'viewprojects': viewprojects, 'related_projects':get_related_projects,'get_related_news':get_related_news,'service':get_services,'market':get_markets}
    return render(request,"CosmosivicsaApplication/viewprojects.html", content)

def values(request):
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    our_values = Our_Values.objects.all()
    return render(request, "CosmosivicsaApplication/values.html",{'service':get_services,'market':get_markets,'our_values':our_values})

def projects(request):
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    proj = Project.objects.all()
    projectfilter = ProjectFilter(request.GET, queryset=proj)
    allfilter = projectfilter.qs
    content = {'project':allfilter,'projectfilter':projectfilter,'service':get_services,'market':get_markets}
    return render(request, "CosmosivicsaApplication/projects.html",content)

def career(request):
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    return render(request, "CosmosivicsaApplication/careers.html",{'service':get_services,'market':get_markets})

def contact(request):
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    our_offices = Our_Offices.objects.all()
    project = Project.objects.all()
    return render(request, "CosmosivicsaApplication/contact.html",{'service':get_services,'market':get_markets,'our_offices':our_offices,'project':project})

def service(request):
    allservice = Service.objects.all()
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    return render(request, "CosmosivicsaApplication/service.html",{'allservice':allservice,'service':get_services,'market':get_markets})

def alljobs(request):
    if request.method=="GET":
        job = request.GET['job']
        country = request.GET['country']
        if job and country:
            alljobs = Publish_job.objects.filter(job_title__contains=job,country__contains=country)
        elif job:
            alljobs = Publish_job.objects.filter(job_title__contains=job)
        else:
            alljobs = Publish_job.objects.filter(country__contains=country)
    else:
        alljobs = Publish_job.objects.all()
    return render(request, "CosmosivicsaApplication/jobcareer.html",{'alljobs': alljobs})

def viewjobs(request,job_title):
    showjob = Publish_job.objects.filter(job_title=job_title)
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    return render(request, "CosmosivicsaApplication/viewjobs.html",{'showjob':showjob,'services':get_services,'market':get_markets})

def jobapply(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        country = request.POST['country']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        job_name = request.POST['job_name']
        job_cat = request.POST['job_cat']
        job_bus = request.POST['job_bus']
        institution = request.POST['institution']
        year = request.POST['year']
        area_of_study = request.POST['area_of_study']
        degree = request.POST['degree']
        company = request.POST['company']
        job_title = request.POST['job_title']
        start_year = request.POST['start_year']
        end_year = request.POST['start_year']
        responsibilties = request.POST['Responsibilities']
        job_details = Job_Apply(first_name=first_name,last_name=last_name,country=country,address=address,city=city,province=state,phone_number=phone_no,
                                email=email,job_name=job_name,job_cat=job_cat,job_bus=job_bus,institution_name=institution,institution_graduation_year=year,degree_name=degree,major_area=area_of_study,
                                company_name=company,job_title=job_title,start_job_year=start_year,end_job_year=end_year,responsibilties=responsibilties)
        job_details.save()
        try:
            send_mail(f'From {first_name}',f'Hi, {first_name} {last_name} Have applied for this job:\nJob Name: "{job_name}",\nJob_Category: "{job_cat}" \nBusiness Line: "{job_bus}".\nHis\Her More Details are mentioned below: \nCountry Name: "{country}", \nAddress: "{address}",\nCity: "{city}", \nState: "{state}",\nemail: "{email}", \nPhone_no: {phone_no}"',email,['talhasarwar289@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request, 'Your Application have successfully received to admin')
        return redirect('career')
    return render(request,"CosmosivicsaApplication/jobapply.html")

def viewservice(request,servicename):
    allservices = Service.objects.get(servicename=servicename)
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    rel_projects = Project.objects.filter(servicename__servicename=allservices.servicename).exclude(id=allservices.id).distinct()[:3]
    return render(request,"CosmosivicsaApplication/viewservice.html",{'allservices':allservices,'rel_projects':rel_projects,'service':get_services,'market':get_markets})

def market(request):
    allmarket = Market.objects.all()
    allmarkets = Market.objects.all()[:7]
    return render(request,"CosmosivicsaApplication/market.html",{'market':allmarkets,'market':allmarket})

def viewmarkets(request,marketname):
    all_markets = Market.objects.get(marketname=marketname)
    get_markets = Market.objects.all()[:7]
    get_services = Service.objects.all()
    rel_markets = Project.objects.filter(marketname__marketname=all_markets.marketname).exclude(id=all_markets.id).distinct()[:3]
    return render(request, "CosmosivicsaApplication/viewmarket.html",{'all_markets': all_markets,'rel_markets':rel_markets,'market':get_markets,'service':get_services})

def press_contact(request):
    if request.method=="POST":
        press_name = request.POST['form_type']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        public_company = request.POST['public_company']
        email = request.POST['email']
        project = request.POST.get('project')
        project_options = request.POST.get('project_options')
        message = request.POST['message']
        message_file = request.FILES.get('message_file')
        press_message = Press_Contact(press=press_name,first_name=first_name,last_name=last_name,company=public_company,email=email,project=project,
                                      project_options=project_options,message=message,message_file=message_file)
        press_message.save()
        if project:
            try:
                send_mail(f'From {first_name}', f'Hi, {first_name} {last_name} wants to contact with you about {press_name}, \nHis\Her More Details are mentioned below: \nCompany\Publication Name: "{public_company}", \nEmail: "{email}",\nMessage: "{message}", \nProject Name: "{project}"',email, ['talhasarwar289@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Your Application have successfully received to admin')
        else:
            try:
                send_mail(f'From {first_name}', f'Hi, {first_name} {last_name} wants to contact with you about {press_name}, \nHis\Her More Details are mentioned below: \nCompany\Publication Name: "{public_company}", \nEmail: "{email}",\nMessage: "{message}", \nProject Name: "{project_options}"',email, ['talhasarwar289@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Your Application have successfully received to admin')
    project = Project.objects.all()
    our_offices = Our_Offices.objects.all()
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    return render(request, "CosmosivicsaApplication/contact.html",{'service':get_services,'market':get_markets,'project':project,'our_offices':our_offices})

def academic_contact(request):
    if request.method=="POST":
        academic = request.POST['form_type']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        academic_intitution = request.POST['academic_intitution']
        degree = request.POST['degree']
        email = request.POST['email']
        project = request.POST.get('academicproject')
        project_options = request.POST.get('project_select_option')
        message = request.POST['message']
        message_file = request.FILES.get('message_file')
        press_message = Academic_Contact(acedemic=academic,first_name=first_name,last_name=last_name,acedemic_ins=academic_intitution,degree=degree,email=email,project=project,
                                      project_options=project_options,message=message,message_file=message_file)
        press_message.save()
        if project:
            try:
                send_mail(f'From {first_name}', f'Hi, {first_name} {last_name} wants to contact with you about {academic}, \nMore Details are mentioned below: \nCompany\institution Name: "{academic_intitution}", \nEmail: "{email}",\nMessage: "{message}", \nProject Name: "{project}"',email, ['talhasarwar289@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Your Application have successfully received to admin')
        else:
            try:
                send_mail(f'From {first_name}', f'Hi, {first_name} {last_name} wants to contact with you about {academic}, \nMore Details are mentioned below: \nCompany\institution Name: "{academic_intitution}", \nEmail: "{email}",\nMessage: "{message}", \nProject Name: "{project_options}"',email, ['talhasarwar289@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Your Application have successfully received to admin')
    project = Project.objects.all()
    our_offices = Our_Offices.objects.all()
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    return render(request, "CosmosivicsaApplication/contact.html",{'service':get_services,'market':get_markets,'project':project,'our_offices':our_offices})

def career_contact(request):
    if request.method=="POST":
        career = request.POST['form_type']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        job_title = request.POST.get('job_title')
        office_name = request.POST.get('job_location')
        url = request.POST.get('link_to_job_post')
        message = request.POST['message']
        message_file = request.FILES.get('message_file')
        press_message = Career_Contact(career=career,first_name=first_name,last_name=last_name,email=email,job_title=job_title,message=message,message_file=message_file,office_name=office_name,url=url)
        press_message.save()
        try:
                send_mail(f'From {first_name}', f'Hi, {first_name} {last_name} wants to contact with you about {career}, \nMore Details are mentioned below: \nJob Name: "{job_title}", \nEmail: "{email}",\nMessage: "{message}"',email, ['talhasarwar289@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request, 'Your Application have successfully received to admin')
    project = Project.objects.all()
    our_offices = Our_Offices.objects.all()
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    return render(request, "CosmosivicsaApplication/contact.html",{'service':get_services,'market':get_markets,'project':project,'our_offices':our_offices})

def business_contact(request):
    if request.method=="POST":
        business = request.POST['form_type']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        company = request.POST.get('company')
        message = request.POST['message']
        message_file = request.FILES.get('message_file')
        sell_product = request.POST.get('selling_product')
        press_message = Business_Contact(business=business,first_name=first_name,last_name=last_name,email=email,company=company,message=message,message_file=message_file,sell_product=sell_product)
        press_message.save()
        try:
            send_mail(f'From {first_name}', f'Hi, {first_name} {last_name} wants to contact with you about {business}, \nMore Details are mentioned below: \nCompany Name: "{company}", \nEmail: "{email}",\nMessage: "{message}"',email, ['talhasarwar289@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request, 'Your Application have successfully received to admin')
    project = Project.objects.all()
    our_offices = Our_Offices.objects.all()
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    return render(request, "CosmosivicsaApplication/contact.html",{'service':get_services,'market':get_markets,'project':project,'our_offices':our_offices})

def others_contact(request):
    if request.method=="POST":
        other = request.POST['form_type']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']
        message_file = request.FILES.get('message_file')
        subject = request.POST['subject']
        office_name = request.POST.get('job_location')
        press_message = Others_Contact(other=other,first_name=first_name,last_name=last_name,email=email,message=message,message_file=message_file,subject=subject,office_name=office_name)
        press_message.save()
        try:
            send_mail(f'From {first_name}', f'Hi, {first_name} {last_name} wants to contact with you about {other}, \nMore Details are mentioned below:  \nEmail: "{email}",\nMessage: "{message}"',email, ['talhasarwar289@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request, 'Your Application have successfully received to admin')
    project = Project.objects.all()
    our_offices = Our_Offices.objects.all()
    get_services = Service.objects.all()
    get_markets = Market.objects.all()[:7]
    return render(request, "CosmosivicsaApplication/contact.html",{'service':get_services,'market':get_markets,'project':project,'our_offices':our_offices})