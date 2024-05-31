<pre>
1. A database schema that is suitable for recording the data that is provided with proper relationships and normalized form.In addition, a simple user management database schema, which allows a user to leave a comment about each YouBike site. 
    Database : sqllite <br />
        user management database : django.contrib.auth.models <br />

<img src='./my_project_visualized.png' width=60%>
<pre/>

2. A script that scrapes and records this data into the database every minute. <br />
    script : <br />
    
        bikeStation/management/commands/fetch_bike_station_info.py <br />
        bikeStation/management/commands/fetch_bike_station_status.py <br />
    cmd: ( can build a cron job in django) <br />
        python manage.py fetch_bike_station_info 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json' <br />
        python manage.py fetch_bike_station_status 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json' <br />
 <br />
3. A RESTful API that provides the following functions: <br />
    a. RESTful methods for user registration, login, and logout. <br />
    
  script : <br />
    users/urls.py <br />
  path: <br />
    path('login/', login_view, name='login'), <br />
    path('register/', register_view, name='register'), <br />
    path('logout/', logout_view, name='logout'), <br />
 <br />
    
b. RESTful methods for users to add, update, delete comments about a YouBike <br />
site.
    
  script: <br />
    comments/urls.pyv
  path: <br />
      path('list_comment', comment_view, name='comment_view'), <br />
      path('add_comment/', add_comment, name='add_comment'), <br />
      path('edit/<int:comment_id>/', edit_comment, name='edit_comment'), <br />
      path('delete/<int:comment_id>/', delete_comment, name='delete_comment'), <br />

c. A GET method that returns sites sorted by sites with the most comments at the <br />
top, with pagination. <br />
  script: <br />
    comments/urls.py <br />
  path: <br />
    path('data/most-commented-stations-data/', most_commented_stations, name='most_commented_stations_data'), <br />
 <br />
 
d. A GET method that returns similar data as the json with: <br />
i. A site name search parameter that can search both english or chinese <br />
ii. An area filter parameter to filter by keywords <br />
    script: <br />
      bikeStation/urls.py <br />
    path:v
      path('search/', search_stations, name='search_stations') <br />
 <br />
e. A GET method that returns sites that have no bikes. <br />
    script: <br />
      bikeStation/urls.py <br />
    path: <br />
      path('data/stations_with_no_bikes_data/', stations_with_no_bikes, name='stations_with_no_bikes') <br />
     <br />
5. [Optional] Unit test <br />
