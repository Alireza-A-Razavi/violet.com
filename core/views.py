from django.shortcuts import render, redirect, reverse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from .models import Item, Category, MainCategory, ContactTicket


# def index_view(request):
# 	items = Item.objects.all()

#     return render(request, 'index.html', {})


class Index(View):
	
	def get(self, request, *args, **kwargs):
		items = Item.objects.all()
		categories = Category.objects.all()
		main_categories = MainCategory.objects.all()

		context = {
			'categories' : categories,
			'items' : items,
			'main_categories' : main_categories,
		}
		return render(request, 'index.html', context)

	# def post(self, request, *args, **kwargs):
	# 	email = request.POST.get['sub-email']
		

class ProductDetailView(View):

	def get(self,  slug, request, *args, **kwargs):
		item = Item.objects.get(slug=slug)

		context = {
			'product' : item,
		}

		return render(request, 'product.html', context)

	# def post(self, request, *args, **kwargs):
		# comment



class ContactView(View):

	def get(self, request, *args, **kwargs):
		try:
			tickets = ContactTicket.objects.filter(user=request.user)

		except ObjectDoesNotExist:
			tickets = None

		context = {
			'tickets' : tickets,
		}
		return render(request, 'contact.html', context)

	def post(self, request, *args, **kwargs):
		first_name = request.POST.get('first_name', "")
		last_name = request.POST.get('last_name', "")
		email = request.POST.get('email', "")
		subject = request.POST.get('subject', "")
		message = request.POST.get('message', "")

		ticket = ContactTicket.objects.create(
				first_name=first_name,
				last_name=last_name,
				email=email,
				subject=subject,
				message=message,
			)
		if request.user.is_authenticated():
			user=request.user
			ticket.user = user
		return redirect('core:index')
		

# class Products(View):
# 	def get(self, request, *args, **kwargs):



# def categories_view(request):

#     return render(request, 'categories.html', {})

# def check_out_view(request):

#     return render(request, 'check-out.html', {})

# def contact_view(request):

#     return render(request, 'contact.html', {})

# def product_page_view(request):

#     return render(request, 'product-page.html', {})

# def cart_view(request):

#     return render(request, 'shopping-cart.html', {})
