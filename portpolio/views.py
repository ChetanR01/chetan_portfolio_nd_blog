from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from .models import MyEducation, MyExperience, MySkill, Project,  Contact,  About
from CRblogs.models import Blog_post

# Create your views here.
def home(request):
    edu_data =MyEducation.objects.all()
    exp_data =MyExperience.objects.all()
    skills =MySkill.objects.all()
    projects = Project.objects.all()
    abouts = About.objects.all()
    # For Blog
    blogs = Blog_post.objects.filter(trending=True).order_by('-date')


    # for Submitting contact form
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact = Contact.objects.create(name=name,email=email,subject=subject,message=message)
        messages.success(request,'Your response is successfully submitted!')

        if contact: 
            # To send mail to the admin about new contact response  
            raw_data= {
                "name":name,
                "email":email,
                "subject":subject,
                "message":message,
                "regards":"Portfolio website"
            }
            html_template= "email_admin_contact.html"
            msg_for_new_user = render_to_string(html_template, context=raw_data)

            msg= EmailMessage(
                "Your have received new contact message.",
                msg_for_new_user,
                'crrathod.tech@gmail.com' ,#from 
                ['admin@crrathod.tech','crrathod.tech@gmail.com'] ,
            )

            msg.content_subtype ="html"
            msg.send()
            print("Email Sent to admin on >. admin@crrathod.tech")

            # To send mail to the client about response submitted 
            raw_data= {
                "name":name,
                "subject":subject,
                "regards":"Chetan Rathod"
            }
            html_template= "email_portfolio_contact.html"
            msg_for_new_user = render_to_string(html_template, context=raw_data)

            msg= EmailMessage(
                "Your response is submitted successfully ",
                msg_for_new_user,
                'crrathod.tech@gmail.com' ,#from 
                [f'{email}'] ,
            )

            msg.content_subtype ="html"
            msg.send()         
            print(f"Email Sent to User on >. {email}")

            return redirect("/#contact")
       


    return render(request, "home.html", {'edu_data':edu_data, 'exp_data': exp_data, 'skills':skills, "projects":projects,"abouts":abouts, "blogs":blogs} )
    # return HttpResponse("Hello Chetan")