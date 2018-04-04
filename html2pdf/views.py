from django.views.generic import View, TemplateView
from django.shortcuts import render_to_response
from django.http import HttpResponse
from html2pdf.pdf import PDF
from html2pdf.tests.test_pdf import get_context
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils import translation


@method_decorator(csrf_exempt, name='dispatch')
class PDFTester(View, PDF):
    http_method_names = ['post', 'get']

    """
    WARNING
    If you don't use the Inheritance from the PDF class to generate
    the PDF Document and try to access just the method `to_pdf` directly
    it won't work even if you give it the same and exact parameters.
    The reason specified in Django documentation: The `request` looses its context
    because this method has to return a full and valid HTTPResponse.
    """

    def post(self, request):
        """
        This View is able to make use of 4 GET parameters:
            lang=[en, de, de-ch] # default=en
            doc_type=[campaign, project] # default=campaign
            font=[Proxima, Lato, Roboto, Saira_Semi_Condensed] # default=Proxima
            filename=Sample Name Document # default="Sample Title"
        """

        # set defaults for GET parameters
        doc_type = 'invoice'
        lang = "en"
        font = "Proxima"
        filename = "Sample Title"

        # replace GET parameters if it is the case
        if request.GET:
            doc_type = request.GET.get('doc_type', doc_type)
            lang = request.GET.get('lang', lang)
            font = request.GET.get('font', font)
            filename = request.GET.get('filename', filename)

        # decide which template to use based on doc_type GET parameter
        if doc_type == 'invoice':
            context = get_context()
            html_template = 'html2pdf/invoice.html'
        else:
            context = get_context()
            html_template = 'html2pdf/invoice.html'

        # prepare the `options` Dictionary
        options = {
            "language": lang,
            "font": font,
            "filename": filename
        }

        if request.POST:
            data = request.POST
        else:
            data = {}

        if data:
            for key, value in data.items():
                for context_key, context_value in context.items():
                    if key == context_key:
                        context[context_key] = value

        # get the Style To overwrite the Default CSS
        style_overwrites = "body { background-color: transparent;}"

        # Make use of `to_pdf` method because of its inheritance from PDF class
        response = self.to_pdf(
            request=request,
            html_template=html_template,
            options=options,
            style_overwrites=style_overwrites,
            content_data=context)
        return response

    def get(self, request):
        """
        This View is able to make use of 4 GET parameters:
            lang=[en, de, de-ch] # default=en
            doc_type=[campaign, project] # default=campaign
            font=[Proxima, Lato, Roboto, Saira_Semi_Condensed] # default=Proxima
            filename=Sample Name Document # default="Sample Title"
        """

        # set defaults for GET parameters
        doc_type = 'invoice'
        lang = "en"
        font = "Proxima"
        filename = "Sample Title"

        # replace GET parameters if it is the case
        if request.GET:
            doc_type = request.GET.get('doc_type', doc_type)
            lang = request.GET.get('lang', lang)
            font = request.GET.get('font', font)
            filename = request.GET.get('filename', filename)

        # decide which template to use based on doc_type GET parameter
        if doc_type == 'invoice':
            context = get_context()
            html_template = 'html2pdf/invoice.html'
        else:
            context = get_context()
            html_template = 'html2pdf/invoice.html'

        # prepare the `options` Dictionary
        options = {
            "language": lang,
            "font": font,
            "filename": filename
        }

        # get the Style To overwrite the Default CSS
        style_overwrites = "body { background-color: transparent;}"

        # Make use of `to_pdf` method because of its inheritance from PDF class
        response = self.to_pdf(
            request=request,
            html_template=html_template,
            options=options,
            style_overwrites=style_overwrites,
            content_data=context)
        return response


# Only to speed development of the HTML with Gulp and BrowserSync
@method_decorator(csrf_exempt, name='dispatch')
class HTMLTester(View, PDF):
    """
    WARNING
    If you don't use the Inheritance from the PDF class to generate
    the PDF Document and try to access just the method `to_pdf` directly
    it won't work even if you give it the same and exact parameters.
    The reason specified in Django documentation: The `request` looses its context
    because this method has to return a full and valid HTTPResponse.
    """

    # Delete the method you don't want it from here
    http_method_names = ['post', 'get']

    def post(self, request):
        # set defaults for GET parameters
        doc_type = 'invoice'
        lang = "en"
        font = "Saira_Semi_Condensed"
        filename = "Sample Title"

        # replace GET parameters if it is the case
        if request.GET:
            doc_type = request.GET.get('doc_type', doc_type)
            lang = request.GET.get('lang', lang)
            font = request.GET.get('font', font)
            filename = request.GET.get('filename', filename)

        # decide which template to use based on doc_type GET parameter
        if doc_type == 'invoice':
            context = get_context()
            html_template = 'html2pdf/invoice.html'
        else:
            context = get_context()
            html_template = 'html2pdf/invoice.html'
        if request.POST:
            data = request.POST
        else:
            data = {}

        if data:
            for key, value in data.items():
                for context_key, context_value in context.items():
                    if key == context_key:
                        context[context_key] = value
        # get the Style To overwrite the Default CSS
        style_overwrites = "body { background-color: blue;}"

        # prepare the `options` Dictionary
        options = {
            "language": lang,
            "font": font,
            "filename": filename
        }

        # Manually Overwrites the Language and Formats to a certain Country
        translation.activate(options['language'])
        response = render_to_response(html_template, context)
        return response

    def get(self, request):
        # set defaults for GET parameters
        doc_type = 'invoice'
        lang = "en"
        font = "Saira_Semi_Condensed"
        filename = "Sample Title"

        # replace GET parameters if it is the case
        if request.GET:
            doc_type = request.GET.get('doc_type', doc_type)
            lang = request.GET.get('lang', lang)
            font = request.GET.get('font', font)
            filename = request.GET.get('filename', filename)

        # decide which template to use based on doc_type GET parameter
        if doc_type == 'invoice':
            context = get_context()
            html_template = 'html2pdf/invoice.html'
        else:
            context = get_context()
            html_template = 'html2pdf/invoice.html'

        # get the Style To overwrite the Default CSS
        style_overwrites = "body { background-color: blue;}"

        # prepare the `options` Dictionary
        options = {
            "language": lang,
            "font": font,
            "filename": filename
        }

        # Manually Overwrites the Language and Formats to a certain Country
        translation.activate(options['language'])
        response = render_to_response(html_template, context)
        return response


class Index(TemplateView):
    template_name = 'index.html'


def health(requests):
    return HttpResponse('ok')
