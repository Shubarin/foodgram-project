import pdfkit
from django.template.loader import get_template


def generate_pdf(template_name, context):
    """
    Generate a PDF file from Django template.
    """
    pdf_options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    html = get_template(template_name).render(context)
    return pdfkit.from_string(html, False, options=pdf_options)
