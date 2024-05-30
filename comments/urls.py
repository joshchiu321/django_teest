from django.urls import path
from .views import comment_view,sorted_stations_view,most_commented_stations,most_commented_stations_page


urlpatterns = [
    path('list_comment', comment_view, name='comment_view'),
    path('paginator', sorted_stations_view, name='sorted_stations_view'),
    path('most-commented-stations/', most_commented_stations_page, name='most_commented_stations_page'),
    path('most-commented-stations-data/', most_commented_stations, name='most_commented_stations_data'),
]
