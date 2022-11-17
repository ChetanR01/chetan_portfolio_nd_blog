from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail, EmailMessage

# for rich text
from ckeditor.fields import RichTextField


# for cloudinary
from cloudinary.models import CloudinaryField

# For tags
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

# for category
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
        
class Blog_post(models.Model):
    
    name= models.CharField(max_length=100)
    # compute field 
    post_url= models.CharField(max_length=120, default="URL will be gererated after saving record")
   
    def get_post_url(self):
        url_str = ""
        strip_name = self.name.strip().lower() # to avoid blank space at start and end
        for char in strip_name:
            if char == " ":
                url_str += "-"
            else:
                url_str += char
        return url_str

    def send_sub_mail(self,email):
        # to send welcome email
        raw_data= {
            "id":self.id,
            "title":self.name,
            "date":self.date,
            "category":self.category,
            "upload_by":self.upload_by,
            "post_img":self.post_img,
            "short_content":self.short_content,
            "post_url":self.post_url,
        }
        html_template= "news_letter_template.html"
        msg_for_news_letter = render_to_string(html_template, context=raw_data)

        msg= EmailMessage(
            "New Blog is uploaded on CRRathod Blog.",
            msg_for_news_letter,
            'crrathod.tech@gmail.com' ,#from 
            [f'{email}'] ,
        )

        msg.content_subtype ="html"
        msg.send()
        print("Subsription Email Sent to >>",email)

    def save(self, *args, **kwargs):
        # send email to subscribers
        self.post_url = self.get_post_url()
        super(Blog_post, self).save(*args, **kwargs)
        # self.send_sub_mail("chetan7744rathod@gmail.com")
        if self.notify_users == True:
            users = User.objects.all()
            for user in users:
                self.send_sub_mail(user.email)


    date= models.DateField()
    post_img = CloudinaryField('img')
    # post_img = models.ImageField(upload_to='img')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    tags = models.ManyToManyField(to=Tag, related_name="post_tags", blank=True)
    short_content = models.CharField(max_length=200)
    main_content = RichTextField(blank=True, null=True)
    # main_content = models.TextField()
    keywords = models.TextField()
    trending = models.BooleanField(default=False)
    no_of_comments = models.IntegerField()

    upload_by = models.CharField(max_length=20)
    upload_by_link = models.CharField(max_length=200)

    notify_users = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

# For Comments
class Comment(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.IntegerField()
    date= models.DateField()
    comment_msg = models.CharField(max_length=400)
    rel_post_id = models.IntegerField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return "Comment by: "+self.name


# For contact form 
class Contact(models.Model):
    name = models.CharField( max_length=100)
    email = models.EmailField( )
    subject = models.CharField( max_length=300)
    message = models.TextField( )
    subsription = models.BooleanField( default=True)

    def __str__(self):
        return "Message from: "+ self.name


# Extend user model and add mobile_no and images
class Extended_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=12)
    user_image = CloudinaryField('profile_img')
    # user_image = models.ImageField(upload_to='profile_img', default="/assets/assets/images/profile_photo.jpg")

    def __str__(self):
        return self.user.first_name