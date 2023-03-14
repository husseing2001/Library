from django.urls import path
from .views import ShelfList, ShelfDetail

urlpatterns = [
    path('', ShelfList.as_view()),
    path('<int:pk>', ShelfDetail.as_view())
]
