from django.urls import path
from .views import (Payment,
Index,
ProjectDetail,
About, 
DepartmentListView, 
ProjectList,  
Hirewriter,
Contact,
Success,)



urlpatterns = [
path('payment/', Payment.as_view(), name='paymentpage'),
path('', Index.as_view(), name='index'),
path('<int:pk>/', ProjectDetail.as_view(), name='content'),
path('about/', About.as_view(), name='about'),
path('department-list', DepartmentListView.as_view(), name='listDepartment'),
path('list-of-project/', ProjectList.as_view(), name='projectlist'),
path('hire-writer', Hirewriter.as_view(), name='hirewwriter'),
path('contact_us', Contact.as_view(), name='contact_us'),
path('thanks', Success.as_view(),name='thanks')

]
