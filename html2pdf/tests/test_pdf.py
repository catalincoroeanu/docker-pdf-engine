from django.utils import timezone
from datetime import timedelta


def get_context():
    return {
        # META CONTENT
        "header": {
            "image": "https://www.cc-wdesign.com/static/img/WDesign-Logo.png",
            "text": ""
        },
        "footer": {
            "image": "",
            # text redered as html {{ footer.text|safe }}
            "text": "CC-WDesign ⋅ Wehntalerstrasse 500 ⋅ CH-8064 Zurich</br>Telefon +41 12 345 67 89 ⋅ www.cc-wdesign.com ⋅ contact@cc-wdesign.com"
        },
        "currency": "CHF",
        "locale": "de",

        # OFFER FIELDS
        "agency_address_header": "CC-WDesign · Wehntalerstrasse 500 · CH-8064 Zurich",
        "customer": {
            "company": "MissBoss & Co. AG",
            # These can be titles prefixing a person's name, e.g.: Mr, Mrs, Miss, Ms, Sir, Dr, Lady or Lord
            "contact_person_title": "Mr",
            "contact_person_name": "John Doe",
            "address": "Bahnhofstrasse 1",
            "country_code": "CH",
            "postal_code": "8001",
            "city": "Zurich",
        },
        "offer": {
            "offer_date": timezone.now(),
            "valid_until_date": timezone.now() + timedelta(days=90),
            "manager": "Catalin Coroeanu",
        },
        "public_id": "CC-2018-001",
        "public_id_text": "Invoice Number: ",
        "title": "Complete redesign www.MissBoss.ch platform",
        "customer_refference": "MissBoss.ch, the first Online Designer Outlet in Switzerland. Discover a wide array of products by the best Italian and international designers.",
        "description": "<div class='f7'>Steps To be done:</div><ul><li>Create new Mockup pages</li><li>Convert the aprouved Mockups into HTML templates</li><li>Refactor Backend Logic to the New Design</li><li>Custom Payment System</li><li>Contact Page with Functional Contact Form</li><li>Optional: Newsletter integration</li></ul></div><br>",
        "total_optional": 2000,
        "total_optional_text": "Total Optional Cost",
        "total_external":2000,
        "total_external_text": "Total External Cost",
        "total_tax": 1600,
        "is_tax_included": True,
        "total_tax_text": "VAT. [8 %]",
        "total_offer": 17000,
        "total_offer_text": "Total CHF cluding. VAT.",
        "discount_explanation": "The total VAT is included in the TOTAL amount.",
        "services_title": "Steps:",
        "services": [
            {
                "position": 1,
                "is_optional": False,
                "is_optional_text": "Optional",
                "is_external_cost": False,
                "is_external_cost_text": "External Cost",
                "has_subtotal": False,
                "has_subtotal_text": "Summary CHF",
                "total_amount": 4000,
                "discount": 0,
                "accepted": None,
                "title": "Create new Mockup pages",
                "description": ""
            },
            {
                "position": 2,
                "is_optional": False,
                "is_optional_text": "Optional",
                "is_external_cost": False,
                "is_external_cost_text": "External Cost",
                "has_subtotal": False,
                "has_subtotal_text": "Summary CHF",
                "total_amount": 6000,
                "discount": 0,
                "accepted": None,
                "title": "Convert the aprouved Mockups into HTML templates",
                "description": ""

            },
            {
                "position": 3,
                "is_optional": False,
                "is_optional_text": "Optional",
                "is_external_cost": False,
                "is_external_cost_text": "External Cost",
                "has_subtotal": False,
                "has_subtotal_text": "Summary CHF",
                "total_amount": 3000,
                "discount": 0,
                "accepted": {},
                "title": "Refactor Backend Logic to the New Design",
                "description": ""

            },
            {
                "position": 4,
                "is_optional": False,
                "is_optional_text": "Optional Cost",
                "is_external_cost": True,
                "is_external_cost_text": "External Cost",
                "has_subtotal": False,
                "has_subtotal_text": "Summary CHF",
                "total_amount": 2000,
                "discount": 0,
                "accepted": {},
                "title": "Custom Payment System",
                "description": ""
            },
            {
                "position": 5,
                "is_optional": True,
                "is_optional_text": "Optional Cost",
                "is_external_cost": False,
                "is_external_cost_text": "External Cost",
                "has_subtotal": False,
                "has_subtotal_text": "Summary CHF",
                "total_amount": 2000,
                "discount": 0,
                "accepted": {},
                "title": "Optional: Newsletter integration",
                "description": ""

            }
        ]
    }
