# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class SurveySurveyInherit(models.Model):
    _inherit = 'survey.user_input'

    signature = fields.Image('Signature', help='Signature received through the portal.', copy=False, attachment=True, max_width=1024, max_height=1024)
    signed_by = fields.Char('Signed By', help='Name of the person that signed the SO.', copy=False)
    signed_on = fields.Datetime('Signed On', help='Date of the signature.', copy=False)
    state_signature = fields.Selection([
        ('signe', 'Signé'),
        ('not_signe', 'Non Signé')], string='Statut de signature', default='not_signe', compute="_get_statut",
        store=True)
    motif = fields.Text(String="Motif")

    @api.depends('signature')
    def _get_statut(self):
        for user in self:
            if user.signature:
                user.state_signature = "signe"
            else:
                user.state_signature = "not_signe"



    def _mark_done(self):
        if self.survey_id.show_signature and not self.signature:
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            mail_to = self.user_input_line_ids[2].display_name
            contact = self.user_input_line_ids[1].display_name
            message ="Bonjour %s <br/>Veuillez svp signer document cahier de charge Dk group sur l'url :<a href='%s/survey/print/%s?answer_token=%s'> Mon cahier de charge</a>" % (contact,base_url,self.sudo().survey_id.access_token, self.sudo().access_token)
            if(mail_to):
                mail_values = {
                    'subject': _('%s', "Signature cahier de charge"),
                    'body_html': message,
                    'author_id': 2,
                    'email_to': mail_to,
                    'email_from': self.env.company.email or self.env.user.email_formatted,
                }
                mail = self.env['mail.mail'].sudo().create(mail_values)
                mail.send()
            #self.write({'state':'in_progress'})
        return super(SurveySurveyInherit, self)._mark_done()


