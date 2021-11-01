from django.urls import path
from .views import FoodCreate, top_view, list_view, count_minus, Food_Delete, login_view, logout_view, SignUpView
urlpatterns = [
    path('create/', FoodCreate.as_view(), name='create'),
    path('list/', list_view, name='list'),
    path('delete/<int:pk>', Food_Delete.as_view(), name='delete'),
    path('minus/<int:pk>', count_minus, name='minus'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', top_view, name='top'),

]