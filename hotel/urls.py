from django.urls import path 
from hotel import views 

app_name = "hotel"

urlpatterns = [
    path("", views.index, name="index"),
    
    path("policy/", views.policy, name="policy"),
    path("tandc/", views.tandc, name="tandc"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("rooms/", views.rooms, name="rooms"),
    path("rooms/<slug:slug>/", views.room_details, name="room_details"),
    path("blogs/", views.blogs, name="blogs"),
    path("blog/<slug:slug>", views.blog_details, name="blog_details"),
    path("detail/<slug:slug>/", views.hotel_detail, name="detail"),
    path("detail/<slug:slug>/room-type/<slug:rt_slug>/", views.room_type_detail, name="room_type_detail"),
    path("selected_rooms/", views.selected_rooms, name="selected_rooms"),
    path("checkout/<booking_id>/", views.checkout, name="checkout"),
    path("invoice/<booking_id>/", views.invoice, name="invoice"),
    path("update_room_status/", views.update_room_status, name="update_room_status"),
    
    
    # Payment API
    path('api/checkout-session/<booking_id>/', views.create_checkout_session, name='api_checkout_session'),
    path('success/<booking_id>/', views.payment_success, name='success'),
    path('failed/<booking_id>/', views.payment_failed, name='failed'),
]