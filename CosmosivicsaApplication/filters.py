import django_filters
from django_filters import *
from .models import *
STATUS_CHOICES = (
    (2021, 2021),
    (2020,2020),
    (2, 'Admin'),
)
class NewsFilter(django_filters.FilterSet):
	newsname = ModelChoiceFilter(queryset=NewsType.objects.all())
	date_created = NumberFilter(field_name='date_created', lookup_expr='year')
	class Meta:
		model = News
		fields = ''

class ProjectFilter(django_filters.FilterSet):
	marketname = ModelChoiceFilter(queryset=Market.objects.all())
	servicename = ModelChoiceFilter(queryset=Service.objects.all())
	countryname = ModelChoiceFilter(queryset=CountryName.objects.all())
	class Meta:
		model = Project
		fields = ''