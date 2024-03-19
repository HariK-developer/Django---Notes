from django.urls import path
from .views import NoteDetail,NoteList


urlpatterns = [
    path("notes/", NoteList.as_view(), name="note"),
    path("notes/<int:pk>/", NoteDetail.as_view(), name="note_detail"),
]
