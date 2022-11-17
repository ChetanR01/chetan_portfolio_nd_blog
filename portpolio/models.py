from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from cloudinary.models import CloudinaryField
# Create your models here.

# For MyEducation details 
class MyEducation(models.Model):
    name = models.CharField(max_length=200)
    university = models.CharField(max_length=100)
    date_from = models.DateField()
    date_to = models.DateField()
    
    description = models.TextField()

    def __str__(self):
        return self.name 

# For MyExperience details 
class MyExperience(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    date_from = models.DateField()
    date_to = models.DateField()
    
    description = models.TextField()

    def __str__(self):
        return self.job_title


# For MySkill details 
class MySkill(models.Model):
    name = models.CharField(max_length=100)
    PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]
    skill_percentage = models.DecimalField(max_digits=3,decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR)

    def __str__(self):
        return self.name


# For Project details 
class Project(models.Model):
    name = models.CharField(max_length=30)
    project_img = CloudinaryField('project_img')
    # project_img = models.ImageField(upload_to='project_img')
    desc = models.CharField(max_length=100)
    code_link = models.CharField(max_length=200)
    view_link = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


# For Contact form
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=300)
    message=models.TextField()

    def __str__(self):
        return "Message from: "+self.name


# For About form
class About(models.Model):
    intro=models.CharField(max_length=500)
    image = CloudinaryField('img')
    # image = models.ImageField(upload_to='img')
    degree=models.CharField(max_length=100)
    experience=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    Mobile_no=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    # resume = CloudinaryField('doc')
    resume=models.CharField(max_length=300)
    other=models.CharField(max_length=100)

    def __str__(self):
        return "For About"