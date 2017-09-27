from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    # Regular Django Views


    # API views
    url(r'^api/offer/$', views.OfferList.as_view()),
    url(r'^api/offer/(?P<pk>[0-9]+)/$', views.OfferDetail.as_view()),
    url(r'^api/transaction/$', views.TrasactionList.as_view()),
url(r'^api/lasttransaction/$', views.LastTransaction.as_view()),
    url(r'^api/transaction/(?P<pk>[0-9]+)/$', views.TransactionDetail.as_view()),
    url(r'^api/wallet/$', views.WalletList.as_view()),
url(r'^api/redeem/$', views.Redeem.as_view()),
    url(r'^api/wallet/(?P<pk>[0-9]+)/$', views.WalletDetail.as_view()),
    url(r'^api/card/$', views.CardList.as_view()),
    url(r'^api/card/(?P<pk>[0-9]+)/$', views.CardDetail.as_view()),
                  url(r'^api/profile/$', views.ProfileList.as_view()),
url(r'^api/shopcart/$', views.ShopCartList.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
