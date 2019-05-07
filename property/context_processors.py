# -*- coding: utf-8 -*-
from .models import *

def properties_processor(request):
 PropertyTypes = PropertyType.objects.all()
 PropertyPlaces = PropertyPlace.objects.all()
 PropertyFloors = PropertyFloor.objects.all()
 LatestProperties = Property.objects.all().order_by('-date')[:3]
 FeaturedProperties = Property.objects.all().order_by('-date')
 FeaturedProperties=FeaturedProperties.filter(featured=True)[:3]
 pricesList=[]
 for i in range(1, 101, 1):
     pricesList.append(i)

 return {'PropertyTypes': PropertyTypes,
     'PropertyPlaces': PropertyPlaces,
     'PropertyFloors': PropertyFloors,
     'LatestProperties': LatestProperties,
     'FeaturedProperties': FeaturedProperties,
     'pricesList': pricesList}