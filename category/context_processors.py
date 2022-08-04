#that way, will let us use that function in any template
from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)