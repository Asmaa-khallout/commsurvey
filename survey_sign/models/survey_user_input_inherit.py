# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class SurveySurveyInherit(models.Model):
    _inherit = 'survey.user_input'

    signature = fields.Image('Signature', help='Signature received through the portal.', copy=False, attachment=True, max_width=1024, max_height=1024)
    signed_by = fields.Char('Signed By', help='Name of the person that signed the SO.', copy=False)
    signed_on = fields.Datetime('Signed On', help='Date of the signature.', copy=False)
    state_signature = fields.Selection([('progress','En cours'),
        ('signe', 'Validé'),
        ('not_signe', 'Refusé')], string='Statut de signature', default='progress')
    motif = fields.Text(String="Motif")
    contact = fields.Char("Contact",compute="_get_data")
    email = fields.Char("Email",compute="_get_data")

    def _get_data(self):
        for record in self:
            record.email = record.user_input_line_ids[2].display_name
            record.contact = record.user_input_line_ids[1].display_name


    # @api.depends('signature','motif')
    # def _get_statut(self):
    #     for user in self:
    #         if user.signature:
    #             user.state_signature = "signe"
    #         elif user.motif:
    #             user.state_signature = "not_signe"
    #         else:
    #             user.state_signature = "progress"

    def relancer_user(self):
        for user in self:
            user.state_signature = 'progress'
            user_mail_template = self.env.ref('survey_sign.mail_template_for_resign',
                                                  raise_if_not_found=False)
            if user_mail_template:
                user_mail_template.sudo().send_mail(self.id, force_send=True)



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


