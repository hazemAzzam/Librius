from django.urls import path, include
from rest_framework import routers
from database import api

router = routers.DefaultRouter()
router.register("Authors", api.AuthorAPI)
router.register("Books", api.BookAPI)
router.register("Members", api.MemberAPI)
router.register("Memberships", api.MembershipAPI)


urlpatterns = [
    path('', include(router.urls)),
]