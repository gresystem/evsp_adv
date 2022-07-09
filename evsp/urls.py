from django.contrib import admin
from django.urls import path, include
from evuser.views import (
    index, search, EvuserUpdateView,
    EvuserList, logout, EvuserDetail, EvuserCreateView, EvuserDeleteView
    )
from charginginfo.views import (
    CharginginfoList, CharginginfoCreateView, CharginginfoDetail,
    CharginginfoUpdateView
    )   
from cardinfo.views import (
    CardinfoList, CardinfoCreateView, CardinfoDeleteView, CardinfoUpdateView,
    CardinfoDetail
    )
from evcharger.views import (
    EvchargerList, EvchargerDetail, EvchargerUpdateView, 
    EvchargerCreateView, EvchargerDeleteView
    )
from board.views import boards_list2, boards_detail, board_write
from msglog.views import MsglogList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('update/<int:pk>/', EvuserUpdateView.as_view(), name='update'),
    path('evuser/', EvuserList.as_view()),
    path('evuser/<int:pk>/delete/', EvuserDeleteView.as_view()),
    path('evuser/<int:pk>/', EvuserDetail.as_view()),
    path('evuser/register/', EvuserCreateView.as_view()),
    path('evuser/search/', search),
    path('charginginfo/', CharginginfoList.as_view()),
    path('charginginfo/<int:pk>/', CharginginfoDetail.as_view()),
    path('charginginfo/register/', CharginginfoCreateView.as_view()),
    path('charginginfoupdate/<int:pk>/', CharginginfoUpdateView.as_view(), name='charginginfoupdate'),
    path('cardinfo/', CardinfoList.as_view()),
    path('cardinfo/<int:pk>/', CardinfoDetail.as_view()),
    path('cardinfo/register/', CardinfoCreateView.as_view()),
    path('cardinfo/<int:pk>/delete/', CardinfoDeleteView.as_view()),
    path('cardupdate/<int:pk>/', CardinfoUpdateView.as_view(), name='cardupdate'),
    path('evcharger/', EvchargerList.as_view()),
    path('evcharger/<int:pk>/delete/', EvchargerDeleteView.as_view()),
    path('evcharger/<int:pk>/', EvchargerDetail.as_view()),
    path('evcharger/register/', EvchargerCreateView.as_view()),
    path('cpupdate/<int:pk>/', EvchargerUpdateView.as_view(), name='cpupdate'),
    path('msgloginfo/', MsglogList.as_view()),
    path('logout/', logout),
]
urlpatterns += [
    path('board/', boards_list2, name="boards_list2"),
    path('board/write/', board_write, name="board_write"),
    path('board/<int:board_id>/', boards_detail, name="boards_detail"),

    path('api/', include('api.urls')),
    path('msglog/', include('msglog.urls')),
]

