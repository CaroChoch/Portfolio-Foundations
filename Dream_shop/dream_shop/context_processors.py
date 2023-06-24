from category.models import Category


def category_links(request):
    women_links = Category.objects.filter(product_type='B')
    men_links = Category.objects.filter(product_type='A')
    women_acc = Category.objects.filter(product_type='X')
    men_acc = Category.objects.filter(product_type='Y')
    men_links_all = Category.objects.filter(gender='H')
    women_links_all = Category.objects.filter(gender='F')

    return {
        'women_links': women_links,
        'women_acc': women_acc,
        'men_links': men_links,
        'men_acc': men_acc,
        'men_links_all': men_links_all,
        'women_links_all': women_links_all,
    }
