from odoo import models, api

class InterestCalculationReport(models.AbstractModel):
    _name = 'report.interest_calculation.report_interest_calculation'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['interest.calculation'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'interest.calculation',
            'docs': docs,
        }
