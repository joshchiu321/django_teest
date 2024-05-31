from django.shortcuts import render,redirect,get_object_or_404
from .forms import StationSelectForm
from .models import Comment
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from .models import Comment
from bikeStation.models import BikeStationInfo
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse

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
    return render(request, 'comments/comment_view.html', context)




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

@login_required
def add_comment(request):
    if request.method == 'POST':
        station_no = request.POST.get('station_no')
        comment_text = request.POST.get('comment')

        if station_no and comment_text:
            station = BikeStationInfo.objects.get(station_no=station_no)
            Comment.objects.create(
                user_id = request.user,
                username=request.user.username,
                station_no=station,
                create_time=timezone.now(),
                comment=comment_text
            )
            return redirect(reverse('comment_view')+ f'?station_no={station_no}')

    return redirect('comment_view')


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, comment_id=comment_id, user_id_id=request.user)

    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            comment.comment = comment_text
            comment.save()
            return redirect(reverse('comment_view') + f'?station_no={comment.station_no.station_no}')

    context = {
        'comment': comment
    }
    return render(request, 'comments/edit_comment.html', context)


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, comment_id=comment_id, user_id_id=request.user)
    station_no = comment.station_no

    if request.method == 'POST':
        comment.delete()
        return redirect(reverse('comment_view') + f'?station_no={comment.station_no.station_no}')

    context = {
        'comment': comment
    }
    return render(request, 'comments/confirm_delete_comment.html', context)