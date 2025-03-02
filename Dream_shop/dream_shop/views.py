from django.shortcuts import render
from store.models import Product, Category


def home(request):
	"""
		Renders the home page with featured products and category links.

		Tries to retrieve the best seller category first. If it doesn't exist,
		displays the latest available products instead.
		Also retrieves category links for women and men, as well as accessory categories.

		Returns:
			A rendered home page template with the featured products and category links.
	"""
	try:
		# Essaie de récupérer les produits "Best seller"
		category = Category.objects.get(category_online="Best seller")
		products = Product.objects.filter(is_available=True, category=category)[:3]
	except Category.DoesNotExist:
		# Si la catégorie n'existe pas, affiche les derniers produits ajoutés
		products = Product.objects.filter(is_available=True).order_by('-created_date')[:3]

	women_links = Category.objects.filter(product_type='B')
	men_links = Category.objects.filter(product_type='A')
	
	women_acc = Category.objects.filter(product_type='X')
	men_acc = Category.objects.filter(product_type='Y')

	context = {
			'products': products,
			'women_links': women_links,
			'women_acc': women_acc,
			'men_links': men_links,
			'men_acc': men_acc,
	}

	return render(request, 'home.html', context)
