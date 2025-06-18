{
    'name': "My ZPL Label Report",
    'version': "1.0",
    'summary': "Report template for ZPL label printing",
    'category': 'Reporting',
    'author': "AyaDelRey",
    'license': 'AGPL-3',
    'depends': [
        'base_report_to_label_printer',
        'base_report_to_printer',
    ],
    'data': [
        'views/report_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
