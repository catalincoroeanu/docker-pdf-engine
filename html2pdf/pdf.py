# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils import translation


class PDF(object):
    """
    PDF class adds method `to_pdf`, and `valid_fonts` to the Views.
    In order to be able to do that it needs the `request` object inside it.
    This gives us a more flexibility:
        - can be accessed from any View;
        - can be extended later on to other document types,
            template types, features or CSS style;
    It is essential to use This class together with the other django class based view
    """

    @staticmethod
    def to_pdf(
            request,
            html_template=None,
            options=None,
            content_data=None,
            style_overwrites=None):
        # Check for `options` dictionary and replace the values with some default ones
        content_data['filename'] = options.get("filename", "Sample Title")
        content_data['lang'] = options.get('language', "en")
        content_data['font'] = options.get('font', "Proxima")
        # If style_overwrites is None it will defaults to the basic CSS
        content_data['style_overwrites'] = style_overwrites

        # Manually Overwrites the Language and Formats to a certain Country
        translation.activate(content_data['lang'])

        html = render_to_string(html_template, content_data)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="{}.pdf"'.format(content_data['filename'])
        HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)
        return response
