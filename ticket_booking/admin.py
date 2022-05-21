from django.contrib import admin
from ticket_booking.models import RequistOtpAuth,BookSeat,UserSavedMessages


# Register your models here.
admin.site.register(RequistOtpAuth)
admin.site.register(BookSeat)
admin.site.register(UserSavedMessages)