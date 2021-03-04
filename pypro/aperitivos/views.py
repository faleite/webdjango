from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 519223445},
        'instalacao-windows': {'titulo': 'Instalação Windows', 'vimeo_id': 519574905},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
