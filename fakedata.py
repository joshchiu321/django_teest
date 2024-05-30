import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vext_demo.settings')
django.setup()

# Now you can import Django models and utilities
from django.contrib.auth.models import User

import random
from django.contrib.auth.models import User
from faker import Faker
from bikeStation.models import BikeStationInfo
from comments.models import Comment
from django.utils import timezone
from datetime import timedelta

fake = Faker()

# def generate_random_users(num_users):
#     for _ in range(num_users):
#         username = fake.user_name()
#         email = fake.email()
#         password = fake.password()
#
#         # Ensure unique username
#         while User.objects.filter(username=username).exists():
#             username = fake.user_name()
#
#         # Create the user
#         User.objects.create_user(username=username, email=email, password=password)
#
# # Call the function to generate, for example, 100 random users
# generate_random_users(100)
#

def generate_random_comments(num_comments):
    users = User.objects.all()
    bike_stations = BikeStationInfo.objects.all()

    for _ in range(num_comments):
        user = random.choice(users)
        username = fake.user_name()
        station = random.choice(bike_stations)
        create_time = timezone.now() - timedelta(days=random.randint(0, 365))  # Random date within the past year
        comment_text = fake.text()

        Comment.objects.create(
            user_id = user,
            username= username,
            station_no=station,
            create_time=create_time,
            comment=comment_text
        )



# Call the function to generate, for example, 100 random comments
generate_random_comments(100)