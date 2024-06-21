{
    "name": "Interest Calculator",
    "version": "1.0",
    "sequence": -100,
    "summary": "Module to calculate simple and compound interest",
    "description": """
        This module calculates simple and compound interest based on user input.
    """,
    "category": "Finance",
    "license": "AGPL-3",
    "website": "https://www.amicurehealth.in",
    "author": "Amicure Health",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/view_interest_calculation_form.xml",
        # "views/report_template.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
