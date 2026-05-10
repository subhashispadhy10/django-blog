from . models import category
from assignment.models import Social

def get_category(request):
    categories=category.objects.all()
    return dict(categories=categories)

def get_social(request):
    social=Social.objects.all()
    return dict(social=social)