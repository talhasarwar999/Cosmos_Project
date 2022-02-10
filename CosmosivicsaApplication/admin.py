from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(NewsType)
admin.site.register(CountryName)
admin.site.register(Publish_job)
admin.site.register(Job_Apply)
admin.site.register(Home_Page_Videos)
admin.site.register(Home_Page_Images)
admin.site.register(Our_Offices)
admin.site.register(Press_Contact)
admin.site.register(Academic_Contact)
admin.site.register(Career_Contact)
admin.site.register(Business_Contact)
admin.site.register(Others_Contact)

class ProjectPostImageInline(admin.TabularInline):
    model = ProjectPostImage
class ProjectParagraphAndImageInline(admin.TabularInline):
    model = ProjectParagraphAndImage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectPostImageInline,ProjectParagraphAndImageInline
    ]

class NewsParagraphAndImageInline(admin.TabularInline):
    model = NewsParagraphAndImage
@admin.register(News)
class NewsInlineAdmin(admin.ModelAdmin):
    inlines = [
        NewsParagraphAndImageInline
    ]

class ServiceParagraphInline(admin.TabularInline):
    model = ServiceParagraph
@admin.register(Service)
class ServiceInlineAdmin(admin.ModelAdmin):
    inlines = [
        ServiceParagraphInline
    ]


class MarketParagraphInline(admin.TabularInline):
    model = MarketParagraph
@admin.register(Market)
class MarketInlineAdmin(admin.ModelAdmin):
    inlines = [
        MarketParagraphInline
]

class Our_ValuesParagraphAndImageInline(admin.TabularInline):
    model = Our_ValuesParagraphAndImage
@admin.register(Our_Values)
class Our_ValuesInlineAdmin(admin.ModelAdmin):
    inlines = [
        Our_ValuesParagraphAndImageInline
]

class Our_FirmParagraphAndImageInline(admin.TabularInline):
    model = Our_FirmParagraphAndImage
class Our_Firm_Excecutive_ImagesInline(admin.TabularInline):
    model = Our_Firm_Excecutive_Images
@admin.register(Our_Firm)
class Our_FirmInlineAdmin(admin.ModelAdmin):
    inlines = [
        Our_FirmParagraphAndImageInline,Our_Firm_Excecutive_ImagesInline
]
