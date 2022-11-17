import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.core.paginator import Paginator
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from portpolio.models import About
from .models import Contact, Blog_post, Comment, Tag, Category, Extended_user

# Create your views here.
def index(request):
    blogs= Blog_post.objects.all().order_by('-date')


    comments = Comment.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    # To get count of no of comments
    for blog in blogs:
        temp_val=0
        for comment in comments:
            if (comment.rel_post_id == blog.id) and (comment.verified == True):
                temp_val +=1
                blog.no_of_comments = temp_val

    
    
    return render(request, "index.html", {"blogs":blogs,"comments":comments,"tags":tags, "categories":categories})

# For Search Function
def search(request):
    blogs = Blog_post.objects.all().order_by('-date')
    comments = Comment.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    
    if request.method =="GET":
        search_for =  request.GET.get('search') 
        try:
            status = Blog_post.objects.filter(name__icontains = search_for)

            # No of comments
            for blog in status:
                temp_val=0
                for comment in comments:
                    if (comment.rel_post_id == blog.id) and (comment.verified == True):
                        temp_val +=1
                        blog.no_of_comments = temp_val

            # to show msg as no record found for search
            show_msg =True
            for rec in status:
                show_msg = False
            if show_msg:
                messages.success(request,f'No result Found! for {search_for}')
            return render(request, "search.html", {"blogs":status,"comments":comments,"tags":tags, "categories":categories})
        except:
            return render(request, "search.html",{"blogs":blogs, "comments":comments,"tags":tags, "categories":categories})
    else:
        return render(request, 'search.html',{"blogs":blogs, "comments":comments,"tags":tags, "categories":categories})



def about(request):
    abouts = About.objects.all()
    return render(request, "about.html", {"abouts":abouts})

def blog(request):
    blogs = Blog_post.objects.all().order_by('-date').distinct()

    p = Paginator(blogs, 4)
    page_no= request.GET.get('page')
    try:
        page_obj = p.get_page(page_no)
    except PageNotAnInteger:
        page_obj=p.page(1)
    except EmptyPage:
        page_obj=p.page(p.num_pages)

    comments = Comment.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    # To get count of no of comments
    for blog in page_obj:
        temp_val=0
        for comment in comments:
            if (comment.rel_post_id == blog.id) and (comment.verified == True):
                temp_val +=1
                blog.no_of_comments = temp_val

    return render(request, "blog.html",{"blogs":blogs, "page_obj":page_obj,"comments":comments,"tags":tags, "categories":categories})

def tag(request, id):
    comments = Comment.objects.all().order_by('-date')
    tags = Tag.objects.all()
    tag = get_object_or_404(Tag, id=id )
    blogs = Blog_post.objects.filter(tags=tag).order_by('-date').distinct()
    p = Paginator(blogs, 4)
    page_no= request.GET.get('page')
    try:
        page_obj = p.get_page(page_no)
    except PageNotAnInteger:
        page_obj=p.page(1)
    except EmptyPage:
        page_obj=p.page(p.num_pages)

    categories = Category.objects.all()
    # To get count of no of comments
    for blog in page_obj:
        temp_val=0
        for comment in comments:
            if (comment.rel_post_id == blog.id) and (comment.verified == True):
                temp_val +=1
                blog.no_of_comments = temp_val
    return render(request, "blog.html",{"blogs":blogs, "page_obj":page_obj, "comments":comments,"tags":tag,"tags":tags, "categories":categories})



def category(request, id):
    comments = Comment.objects.all().order_by('-date')
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=id )
    blogs = Blog_post.objects.filter(category=category).order_by('-date').distinct()
    p = Paginator(blogs, 4)
    page_no= request.GET.get('page')
    try:
        page_obj = p.get_page(page_no)
    except PageNotAnInteger:
        page_obj=p.page(1)
    except EmptyPage:
        page_obj=p.page(p.num_pages)

    tags = Tag.objects.all()
    # To get count of no of comments
    for blog in page_obj:
        temp_val=0
        for comment in comments:
            if (comment.rel_post_id == blog.id) and (comment.verified == True):
                temp_val +=1
                blog.no_of_comments = temp_val
    return render(request, "blog.html",{"blogs":blogs, "page_obj":page_obj, "comments":comments,"tags":tag,"tags":tags, "categories":categories})






def post(request, id, post_url):
    # For storing comments
    users = User.objects.all()
    if request.method =="POST":
        name = request.user.first_name +" "+ request.user.last_name
        user_id = request.user.id
        date = datetime.datetime.now() 
        rel_post_id = request.POST['post_id']
        comment_msg = request.POST['message']  

        comment = Comment.objects.create(name=name,date=date,user_id=user_id,rel_post_id=rel_post_id,comment_msg=comment_msg)
        messages.success(request,'Your Comment is submitted successfully, It\'ll be live after verified by the Admin, Thank You!')

        return redirect("/blog/post/"+rel_post_id)

    blogs= Blog_post.objects.all().order_by('-date')
    blog= Blog_post.objects.get(id=id)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    comments = Comment.objects.filter(rel_post_id=id)
    return render(request, "post-details.html",{"blog":blog,"blogs":blogs , "comments":comments,"tags":tags, "categories":categories, "users":users})

def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        check_button = request.POST.getlist('subsription')

        if "on" in check_button:
            subsription = True
        else:
            subsription= False

        contact = Contact.objects.create(name=name,email=email,subject=subject,message=message,subsription=subsription)
        messages.success(request,'Your reseponse is submitted successfully, Thank You!')

        # to send welcome email
        raw_data= {
            "name":name,
            "subject":subject,
            "regards":"Admin CRRathod Blog."
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

        # To send mail to the admin about new contact response  
        raw_data= {
            "name":name,
            "email":email,
            "subject":subject,
            "message":message,
            "regards":"CRRathod Blog."
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

        return redirect("/blog/contact")
        
    return render(request, "contact.html")

def profile(request):
    if request.method =="POST":
        predata = User.objects.get(id=request.user.id)  
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        predata.first_name = first_name
        predata.last_name = last_name
        predata.email = email

        mobile_no = request.POST['mobile_no']

        try:
            data_check =  Extended_user.objects.get(user = predata)
            print("data checker", data_check)
        except:
            data_check = False
        # if mobile no. or photo already uploaded
        if data_check:
            try:
                user_image = request.FILES['profile_image']
                data_check.user_image = user_image
                if len(mobile_no)<=12:
                    data_check.mobile_no = mobile_no
                else:
                    messages.info(request,"Please enter valid mobile number (max length 12)")
                    return redirect('/blog/profile')
            except:
                if len(mobile_no)<=12:
                    data_check.mobile_no = mobile_no
                else:
                    messages.info(request,"Please enter valid mobile number (max length 12)")
                    return redirect('/blog/profile')
            data_check.save()
        # if updating mobile no or photo for first time
        else:
            try: 
                user_image = request.FILES['profile_image']
                if len(mobile_no)<=12:
                    ext_data = Extended_user(user=predata, mobile_no = mobile_no, user_image = user_image)  
                else:
                    messages.info(request,"Please enter valid mobile number (max length 12)")
                    return redirect('/blog/profile')
            except:
                if len(mobile_no)<=12:
                    ext_data = Extended_user(user=predata, mobile_no = mobile_no) 
                else:
                    messages.info(request,"Please enter valid mobile number (max length 12)")
                    return redirect('/blog/profile')
            ext_data.save()
                   
        predata.save()   

        messages.info(request,"Your account details successfully updated")

        return redirect('/blog/profile')
    return render(request, "profile.html")

def signup(request):
    if request.method== "POST":
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_pass = request.POST['confirm_pass']
        
        if password == confirm_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is Already Used!")
                return redirect('/blog/profile/signup')
            else:
                user = User.objects.create_user(username=username,password= password, email=email, first_name=name)
                user.save()
                messages.info(request,"Your have successfully created account, Login Now!")

                # to send welcome email
                raw_data= {
                    "name":name,
                    "email":email,
                    "username":username,
                    "password":password,
                }
                html_template= "email_signup.html"
                msg_for_new_user = render_to_string(html_template, context=raw_data)

                msg= EmailMessage(
                    "Your account is created successfully ",
                    msg_for_new_user,
                    'crrathod.tech@gmail.com' ,#from 
                    [f'{email}'] ,
                )

                msg.content_subtype ="html"
                msg.send()
                               
                print(f"Email Sent to User on >. {email}")

                return redirect('/blog/profile/login')

        else:
            messages.info(request,"Password Not matching!")
            return redirect('/blog/profile/signup')

    else:
        return render(request, "signup.html")

def login(request):
    if request.method== "POST":
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/blog")
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect("/blog/profile/login")

    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/blog')