# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def message_new(self, msg_dict, custom_values=None):
        _logger.info("test msg dict : %s custom values : %s" %(msg_dict,custom_values))
        try:
            body = msg_dict.get('body')
            phone = str(body).split("Téléphone :")[1].split("<br>")[0]
            contact = str(body).split("Contact :")[1].split("<br>")[0]
            note = str(body).split("Message :")[1].split("<br>")[0]
            email_from = str(body).split("Email :")[1].split("<br>")[0]
            custom_values.update(
                {'phone': phone, 'contact_name': contact, 'description': note})
            msg_dict.update({'email_from':email_from})
        except:
            pass

        return super(CrmLeadInherit, self).message_new(msg_dict, custom_values)
