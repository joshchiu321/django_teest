from django.shortcuts import render
from .forms import StationSelectForm
from .models import Comment
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from .models import Comment
from bikeStation.models import BikeStationInfo
from django.db.models import Count


def comment_view(request):
    stations = BikeStationInfo.objects.all()
    selected_station = request.GET.get('station_no')
    comments = None

    if selected_station:
        comments = Comment.objects.filter(station_no=selected_station).order_by('-create_time')

    context = {
        'stations': stations,
        'comments': comments,
        'selected_station': selected_station,
    }
    return render(request, 'home.html', context)


def sorted_stations_view(request):
    stations = BikeStationInfo.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')
    paginator = Paginator(stations, 10)  # Show 10 stations per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'home.html', context)


def most_commented_stations(request):
    sorted_stations = BikeStationInfo.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')
    paginator = Paginator(sorted_stations, 10)  # Show 10 stations per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    stations_data = [
        {
            "station_no": station.station_no,
            "station_name": station.station_name,
            "comment_count": station.comment_count,
        }
        for station in page_obj
    ]

    data = {
        "stations": stations_data,
        "page": page_obj.number,
        "pages": paginator.num_pages,
    }
    return JsonResponse(data)


def most_commented_stations_page(request):
    return render(request, 'comments/most_commented_stations.html')
