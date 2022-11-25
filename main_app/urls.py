from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('pizzas/', views.pizzas_index, name='index'),
  path('pizzas/<int:pizza_id>/', views.pizzas_detail, name='detail'),
  path('pizzas/create/', views.PizzaCreate.as_view(), name='pizzas_create'),
  path('pizzas/<int:pk>/update/', views.PizzaUpdate.as_view(), name='pizzas_update'),
  path('pizzas/<int:pk>/delete/', views.PizzaDelete.as_view(), name='pizzas_delete'),
  path('pizzas/<int:pizza_id>/assoc_topping/<int:topping_id>/', views.assoc_topping, name='assoc_topping'),
  path('pizzas/<int:pizza_id>/unassoc_topping/<int:topping_id>/', views.unassoc_topping, name='unassoc_topping'),
  path('toppings/', views.ToppingList.as_view(), name='toppings_index'),
  path('toppings/<int:pk>/', views.ToppingDetail.as_view(), name='toppings_detail'),
  path('toppings/create/', views.ToppingCreate.as_view(), name='toppings_create'),
  path('toppings/<int:pk>/update/', views.ToppingUpdate.as_view(), name='toppings_update'),
  path('toppings/<int:pk>/delete/', views.ToppingDelete.as_view(), name='toppings_delete'),
]
