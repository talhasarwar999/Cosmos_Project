from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# from location_field.models.spatial import LocationField
# from django.contrib.gis.geos import Point
from django.core.validators import FileExtensionValidator


# Create your models here.
class NewsType(models.Model):
    newsname = models.CharField(max_length=1000)
    def __str__(self):
        return self.newsname

class CountryName(models.Model):
    countryname = models.CharField(max_length=1000)
    def __str__(self):
        return self.countryname

class Market(models.Model):
    marketname = models.CharField(max_length=1000)
    market_images = models.ImageField(upload_to='home/images')
    main_title = models.CharField(max_length=1001)
    def __str__(self):
        return self.marketname

class MarketParagraph(models.Model):
    title = models.CharField(max_length=300,blank=True,null=True)
    paragraph = RichTextUploadingField()
    projectFK = models.ForeignKey(Market, on_delete=models.CASCADE, related_name="marketfk")

class Service(models.Model):
    servicename = models.CharField(max_length=1000)
    main_title = models.CharField(max_length=1001)
    service_images = models.ImageField(upload_to='home/images')
    def __str__(self):
        return self.servicename

class ServiceParagraph(models.Model):
    title = models.CharField(max_length=300,blank=True,null=True)
    paragraph = RichTextUploadingField()
    projectFK = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="servicefk")

class Project(models.Model):
    marketname = models.ManyToManyField(Market,blank=True) #Many key to Market
    servicename = models.ManyToManyField(Service,blank=True) #Many key to Service
    title = models.CharField(max_length=500,blank=True,null=True)
    client = models.CharField(max_length=500,blank=True,null=True)
    countryname = models.ManyToManyField(CountryName,blank=True) #Many key to CountryName
    include = models.CharField(max_length=900,blank=True,null=True)
    area = models.CharField(max_length=900,blank=True,null=True)
    cost = models.CharField(max_length=900,blank=True,null=True)
    sustainability = models.CharField(max_length=900,blank=True,null=True)
    key_highlights = models.CharField(max_length=900,blank=True,null=True)
    status = models.CharField(max_length=800,blank=True,null=True)
    desc_1 = models.CharField(max_length=3000,blank=True,null=True)
    desc_2 = models.CharField(max_length=3001,blank=True,null=True)
    # location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0)))
    location = models.CharField(max_length=1000,blank=True,null=True)
    parent_images = models.ImageField(upload_to='home/images')

class ProjectPostImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="imag") #Foreign key to Project
    images = models.ImageField(upload_to='home/images')

class ProjectParagraphAndImage(models.Model):
    title = models.CharField(max_length=300,blank=True,null=True)
    paragraph = RichTextUploadingField()
    image = models.ImageField(upload_to='home/images')
    projectFK = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="imagg") #Foreign key to Project

class News(models.Model):
    newsname = models.ManyToManyField(NewsType,blank=True) #Many key to NewsType
    countryname = models.ManyToManyField(CountryName,blank=True) #Many key to CountryName
    title = models.CharField(max_length=1000,blank=True,null=True)
    parent_image = models.ImageField(upload_to='home/images')
    date_created = models.DateField(auto_now=True)

class NewsParagraphAndImage(models.Model):
    paragraph = RichTextUploadingField()
    image = models.ImageField(upload_to='home/images')
    newsFK = models.ForeignKey(News, on_delete=models.CASCADE, related_name="imagge") #Foreign key to News

class Publish_job(models.Model):
    job_title = models.CharField(max_length=1000)
    job_category = models.CharField(max_length=1001)
    business_line = models.CharField(max_length=1002)
    requirements = RichTextUploadingField(blank=True)
    responsibiltie = RichTextUploadingField(blank=True)
    country = models.CharField(max_length=1000)
    position_status = models.CharField(max_length=1000)
    requisition_vacancy_no = models.IntegerField()
    def __str__(self):
        return self.job_title

class Job_Apply(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=300)
    province = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=200)
    job_name = models.CharField(max_length=200)
    job_cat= models.CharField(max_length=200)
    job_bus= models.CharField(max_length=200)
    institution_name = models.CharField(max_length=1000,null=True,blank=True)
    institution_graduation_year = models.CharField(max_length=1000,null=True,blank=True)
    degree_name = models.CharField(max_length=500,null=True,blank=True)
    major_area = models.CharField(max_length=5000,null=True,blank=True)
    company_name = models.CharField(max_length=1000,null=True,blank=True)
    job_title = models.CharField(max_length=100,null=True,blank=True)
    start_job_year = models.CharField(max_length=100,null=True,blank=True)
    end_job_year = models.CharField(max_length=100,null=True,blank=True)
    responsibilties = models.TextField()
    def  __str__(self):
        return self.first_name

class Home_Page_Videos(models.Model):
    video_content = models.CharField(max_length=3000,blank=True,null=True)
    videofile = models.FileField(upload_to='home/SliderVideos',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

class Home_Page_Images(models.Model):
    image = models.ImageField(upload_to='home/images')

class Our_Values(models.Model):
    video = models.FileField(upload_to='home/SliderVideos',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    name = models.CharField(max_length=100)

class Our_ValuesParagraphAndImage(models.Model):
    title = models.CharField(max_length=300)
    paragraph = RichTextUploadingField()
    image = models.ImageField(upload_to='home/images')
    valuesFK = models.ForeignKey(Our_Values, on_delete=models.CASCADE, related_name="values") #Foreign key to Our_Values


class Our_Firm(models.Model):
    video = models.FileField(upload_to='home/SliderVideos',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    name = models.CharField(max_length=100)

class Our_FirmParagraphAndImage(models.Model):
    title = models.CharField(max_length=300)
    paragraph = RichTextUploadingField()
    image = models.ImageField(upload_to='home/images')
    firmFK = models.ForeignKey(Our_Firm, on_delete=models.CASCADE, related_name="firm")#Foreign key to Our_Firm

class Our_Firm_Excecutive_Images(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    work = models.CharField(max_length=250,blank=True,null=True)
    about = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to='home/images')
    firmimageFK = models.ForeignKey(Our_Firm, on_delete=models.CASCADE, related_name="firm_images")  # Foreign key to Our_Firm

class Our_Offices(models.Model):
    image = models.ImageField(upload_to='home/images')
    countryname = models.ManyToManyField(CountryName,blank=True)
    address  = models.CharField(max_length=350)
    location  = models.URLField(max_length=1000)

class Press_Contact(models.Model):
    press = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=500,blank=True,null=True)
    email = models.CharField(max_length=500)
    project = models.CharField(max_length=1000,blank=True,null=True)
    project_options = models.CharField(max_length=1000,blank=True,null=True)
    message = models.TextField()
    message_file = models.FileField(null=True,upload_to='home/images')

class Academic_Contact(models.Model):
    acedemic = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    acedemic_ins = models.CharField(max_length=500)
    degree = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    project = models.CharField(max_length=1000,blank=True,null=True)
    project_options = models.CharField(max_length=1000,blank=True,null=True)
    message = models.TextField()
    message_file = models.FileField(upload_to='home/images',blank=True,null=True)

class Career_Contact(models.Model):
    career = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    job_title = models.CharField(max_length=1000,blank=True,null=True)
    office_name = models.CharField(max_length=1000,blank=True,null=True)
    url = models.URLField(max_length=1000,blank=True,null=True)
    message = models.TextField()
    message_file = models.FileField(null=True,upload_to='home/images')

class Business_Contact(models.Model):
    business = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=500,null=True,blank=True)
    email = models.CharField(max_length=500)
    message = models.TextField()
    message_file = models.FileField(upload_to='home/images',blank=True,null=True)
    sell_product = models.CharField(max_length=1000,null=True,blank=True)

class Others_Contact(models.Model):
    other = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    subject = models.CharField(max_length=500)
    office_name = models.CharField(max_length=1000,blank=True,null=True)
    message = models.TextField()
    message_file = models.FileField(upload_to='home/images',blank=True,null=True)