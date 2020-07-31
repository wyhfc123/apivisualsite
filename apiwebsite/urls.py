from django.urls import path

from apiwebsite.views import GetChartOneAPIView, UpdateChartOneAPIView, SaveChartTwoAPIView, GetChartTwoAPIView

urlpatterns=[
    path("getchartone/", GetChartOneAPIView.as_view()),
    path("updatechartone/",UpdateChartOneAPIView.as_view()),
    path("savecharttwo/",SaveChartTwoAPIView.as_view()),
    path("getcharttwo/",GetChartTwoAPIView.as_view()),



]