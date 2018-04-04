from django.conf.urls import url

from .views import (
    Index,
    PDFTester,
    HTMLTester
)

urlpatterns = [
    url(r'^pdf/', PDFTester.as_view(), name='PDFTester'),
    url(r'^html/', HTMLTester.as_view(), name='HTMLTester'),
    url(r'^$', Index.as_view(), name='index')
]
