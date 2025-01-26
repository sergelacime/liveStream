from django.urls import path
from . import views

urlpatterns = [
    path('', views.folder_list, name='folder_list'),
    
    # Page pour afficher les vidéos d'un dossier spécifique
    path('folder/<int:folder_id>/', views.video_list_by_folder, name='video_list_by_folder'),
    
    # Page pour afficher une vidéo spécifique (optionnel, selon ton implémentation)
    path('video/<int:video_id>/', views.video_player, name='video_player'),
    path('api/videos/', views.video_list_api, name='video_list_api'),
]
