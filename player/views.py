from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Folder, Video

def folder_list(request):
    """Affiche la liste des dossiers de vidéos."""
    folders = Folder.objects.all()
    return render(request, 'player/folder_list.html', {'folders': folders})

from django.core.paginator import Paginator

def video_list_by_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    videos = folder.videos.all()
    
    # Pagination
    paginator = Paginator(videos, 9)  # 9 vidéos par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'player/video_list_by_folder.html', {'folder': folder, 'page_obj': page_obj})

def video_list_api(request):
    videos = Video.objects.all()
    data = [{"id": video.id, "title": video.title, "file": video.file.url} for video in videos]
    return JsonResponse(data, safe=False)

def video_list(request):
    """Affiche une liste de vidéos disponibles."""
    videos = Video.objects.all()
    return render(request, 'player/video_list.html', {'videos': videos})

def video_player(request, video_id):
    """Affiche le lecteur vidéo pour une vidéo spécifique."""
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'player/video_player.html', {'video': video})
