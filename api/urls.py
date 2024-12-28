from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from .views import ( 
        ArticleView, ArticleDetailView, ArticleCreateView, 
        ArticleUpdateView, ArticleDeleteView
        )

urlpatterns = [
        path('', ArticleView.as_view(), name="listpost"),
        path('article/<slug:slug>/', ArticleDetailView.as_view(), name="detailpost"),
        path('create/', ArticleCreateView.as_view(), name="createpost"),
        path('update/<pk>/', ArticleUpdateView.as_view(), name="updatepost"),
        path('delete/<pk>/', ArticleDeleteView.as_view(), name="deletepost"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)