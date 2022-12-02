# -*- coding: utf-8 -*-

from odoo import models, fields, api




class SurveySurveyInherit(models.Model):
    _inherit = 'survey.survey'
    show_signature = fields.Boolean('Show Signature',default=False)



    def get_portal_url(self, suffix=None, report_type=None, download=None, query_string=None, anchor=None):
        """
            Get a portal url for this model, including access_token.
            The associated route must handle the flags for them to have any effect.
            - suffix: string to append to the url, before the query string
            - report_type: report_type query string, often one of: html, pdf, text
            - download: set the download query string to true
            - query_string: additional query string
            - anchor: string to append after the anchor #
        """
        self.ensure_one()
        url = '%s?access_token=%s%s%s%s' % (
            suffix if suffix else '',
            '&report_type=%s' % report_type if report_type else '',
            '&download=true' if download else '',
            query_string if query_string else '',
            '#%s' % anchor if anchor else ''
        )
        return url
