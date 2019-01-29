from django.shortcuts import render
from datetime import datetime

# Create your views here.
def video(request, tvno):
    tv_list = [
        {'name': '明天再擱來', 'tvcode': 'D3cLm-AuMU0'},
        {'name': '愛我你會死', 'tvcode': 'j7mNwY6IJmQ'},
        {'name': '浪流連', 'tvcode': '3Y0Ut5ozaKs'},
        {'name': '我跟你卡好', 'tvcode': 'iTl5_n5saQU'}
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'video.html', locals())
