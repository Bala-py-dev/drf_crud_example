from django.urls import path
from student.views import StudentDetailListCreate, StudentDetailRetrieve

urlpatterns = [
 path('student-details/', StudentDetailListCreate.as_view(), name='student-details'),
 path('student-details/<int:id>', StudentDetailRetrieve.as_view(), name='student-detail'),  
]