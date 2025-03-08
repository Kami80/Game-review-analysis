from django.urls import path
from .views import index_func, export_to_csv, upload_csv, export_games_to_csv, game_list

urlpatterns = [
    path('', index_func, name='homepage'),
    path('export-csv/', export_to_csv, name='export_csv'),  # Add this line
    path("upload-csv/", upload_csv, name="upload_csv"),
    path('export-games/', export_games_to_csv, name='export_games'),
    path('games/', game_list, name='game_list'),
    ]