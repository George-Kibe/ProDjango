# from django.conf import settings
# import logging
from django.contrib import admin
from django.urls import path

# print(settings.DEBUG)
# print(settings.SECRET_KEY)
# logger = logging.getLogger(__name__)
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warn message")
# print("Done Logging")

urlpatterns = [
    path("admin/", admin.site.urls),
]
