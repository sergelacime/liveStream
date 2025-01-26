import os
from django.core.management.base import BaseCommand
from player.models import Folder, Video

class Command(BaseCommand):
    help = 'Importe les vidéos dans la base de données depuis les dossiers existants'

    def handle(self, *args, **kwargs):
        # Chemin de base où sont stockés les dossiers vidéos
        base_path = './media/'  # Remplacez par le chemin réel

        # Parcours tous les dossiers dans le chemin de base
        for folder_name in os.listdir(base_path):
            folder_path = os.path.join(base_path, folder_name)

            if os.path.isdir(folder_path):
                # Crée un dossier dans la base de données
                folder, created = Folder.objects.get_or_create(
                    name=folder_name,
                    path=folder_path
                )

                # Parcours tous les fichiers dans ce dossier
                for file_name in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file_name)
                    file_path2 = os.path.join(folder_name, file_name)

                    # Si c'est un fichier vidéo (ici on assume mp4, mkv comme exemple)
                    if os.path.isfile(file_path) and file_name.lower().endswith(('.mp4', '.mkv', '.avi')):
                        # Crée une entrée vidéo dans la base de données
                        video, created = Video.objects.get_or_create(
                            title=file_name,
                            folder=folder,
                            file=file_path2  # Enregistrez le chemin du fichier
                        )
                        if created:
                            self.stdout.write(self.style.SUCCESS(f'Vidéo ajoutée: {file_name} dans {folder_name}'))
                        else:
                            self.stdout.write(self.style.SUCCESS(f'Vidéo déjà existante: {file_name} dans {folder_name}'))
