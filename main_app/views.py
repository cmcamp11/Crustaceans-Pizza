from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pizza, Topping

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pizzas_index(request):
  pizzas = Pizza.objects.all()
  return render(request, 'pizzas/index.html', {
    'pizzas': pizzas
  })

def pizzas_detail(request, pizza_id):
  pizza = Pizza.objects.get(id=pizza_id)
  id_list = pizza.toppings.all().values_list('id')
  toppings_pizza_doesnt_have = Topping.objects.exclude(id__in=id_list)
  return render(
    request,
    'pizzas/detail.html',
    {
      'pizza': pizza,
      'toppings': toppings_pizza_doesnt_have
    }
  )

class PizzaCreate(CreateView):
  model = Pizza
  fields = [ 'name','description','qty' ]
  
class PizzaUpdate(UpdateView):
  model = Pizza
  fields = [ 'name', 'description', 'qty']

class PizzaDelete(DeleteView):
  model = Pizza
  success_url = '/pizzas/'

def assoc_topping(request, pizza_id, topping_id):
  pizza = Pizza.objects.get(id=pizza_id)
  pizza.toppings.add(topping_id)
  return redirect('detail', pizza_id=pizza_id)

def unassoc_topping(request, pizza_id, topping_id):
  Pizza.objects.get(id=pizza_id).toppings.remove(topping_id)
  return redirect('detail', pizza_id=pizza_id)

class ToppingList(ListView):
  model = Topping

class ToppingDetail(DetailView):
  model = Topping

class ToppingCreate(CreateView):
  model = Topping
  fields = '__all__'

class ToppingUpdate(UpdateView):
  model = Topping
  fields = ['name', 'qty']

class ToppingDelete(DeleteView):
  model = Topping
  success_url = '/toppings/'