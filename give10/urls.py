from django.urls import path
from .views import index, SignUpView, ViewByUser, TipCreate, TipDetail, TiptypeCreate, TipDeleteView, TipUpdate

app_name = 'give10'

urlpatterns = [
    path('', index, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ViewByUser.as_view(), name='profile'),
    path('new_tiptype/', TiptypeCreate.as_view(), name='new_tiptype'),
    path('new_tip/', TipCreate.as_view(), name='new_tip'),
    path('tip/<int:pk>/', TipDetail.as_view(), name='tip_detail'),
    path('tip/<int:pk>/delete/', TipDeleteView.as_view(), name='tip_delete'),
    path('tip/<int:pk>/update/', TipUpdate.as_view(), name='tip_update'),
]

