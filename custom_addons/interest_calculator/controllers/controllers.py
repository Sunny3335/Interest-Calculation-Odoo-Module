from odoo import http
from odoo.http import request

class InterestCalculationController(http.Controller):

    @http.route('/interest_calculation/calculate', auth='public', website=True, csrf=False)
    def calculate_interest(self, **kw):
        # Example implementation of calculating interest
        principal_amount = float(kw.get('principal_amount', 0))
        interest_rate = float(kw.get('interest_rate', 0))
        time_period = int(kw.get('time_period', 0))
        interest_type = kw.get('interest_type', 'simple')

        # Perform interest calculation based on input parameters
        if interest_type == 'simple':
            simple_interest = (principal_amount * interest_rate * time_period) / 100
            compound_interest = 0.0
        elif interest_type == 'compound':
            compound_interest = principal_amount * ((1 + interest_rate / 100) ** time_period) - principal_amount
            simple_interest = 0.0
        else:
            simple_interest = 0.0
            compound_interest = 0.0

        # Return a JSON response with the calculated interests
        return request.make_response({
            'simple_interest': simple_interest,
            'compound_interest': compound_interest
        })

