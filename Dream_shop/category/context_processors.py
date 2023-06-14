from .models import Category


def menu_links(request):
    links = Category.objects.exclude(category_name="Best Seller")
    return dict(links=links)
