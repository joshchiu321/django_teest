from django.urls import path
from .views import comment_view,most_commented_stations,most_commented_stations_page,add_comment,edit_comment,delete_comment


urlpatterns = [
    path('list_comment', comment_view, name='comment_view'),

    path('most-commented-stations/', most_commented_stations_page, name='most_commented_stations_page'),
    path('data/most-commented-stations-data/', most_commented_stations, name='most_commented_stations_data'),
    path('add_comment/', add_comment, name='add_comment'),
    path('edit/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('delete/<int:comment_id>/', delete_comment, name='delete_comment'),
]
