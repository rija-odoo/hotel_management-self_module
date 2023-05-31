{
    'name': "Hotel_Management",
    'version': '1.0',
    'depends': ['base'],
    'author': "Ritik Jariya",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/hotel_model_facility_views.xml',
        'views/hotel_model_offer.xml',
        'views/hotel_model_type.xml',
        'views/hotel_model_view.xml',
        'views/hotel_menus.xml',
    ],
    # data files containing optionally loaded demonstration data

    "demo": [
        "demo/hotel_demo.xml",
    ],


    'application': True,
}