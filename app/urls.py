from django.urls import path
from app.infrastructure.api.views import ItemList, ListDetails

urlpatterns = [
    path("items/", ItemList.as_view(), name="items"),
    path("lists/<int:id>/", ListDetails.as_view(), name="lists"),
]
