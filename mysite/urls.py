"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import main.views as main_views
import user.views as user_views
import guestbook.views as guest_book_views
import board.views as board_views

urlpatterns = [
# 메인 화면
    path('', main_views.index),
#관리자 화면
    path('admin/', admin.site.urls),
# 사용자 관련 기능
    # 사용자 회원가입 화면
    path('user/joinform/', user_views.joinform),
    # 사용자 회원가입 TX
    path('user/join', user_views.join),
    # 회원가입 완료
    path('user/joinsuccess/', user_views.joinsuccess),
    # 로그인
    path('user/loginform/', user_views.loginform),
    # 로그인 TX
    path('user/login', user_views.login),
    # 로그아웃
    path('user/logout', user_views.logout),

# 방명록 관련 기능
    # 방명록 리스트
    path('guestbook/', guest_book_views.index),
    # 방명록 추가 TX
    path('guestbook/add', guest_book_views.add),
    # 방명록 삭제화면
    path('guestbook/deleteform', guest_book_views.deleteform),
    # 방명록 삭제 TX
    path('guestbook/delete', guest_book_views.delete),

# 게시판
    # 게시판 리스트 출력
    path('board/', board_views.index),
    # 게시판 등록화면
    path('board/writeform', board_views.writeform),
    path('board/write', board_views.write),
    # 게시판 detail
    path('board/view', board_views.view),
    path('board/modifyform', board_views.modifyform),
    path('board/modify', board_views.modify),
    path('board/delete', board_views.delete)
]
