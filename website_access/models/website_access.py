# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WebsiteWordPress(models.Model):
    _name = 'website.access'
    _description = "Website Access"
    _rec_name = "name"

    name = fields.Char("Name",required=True)
    url_access_front = fields.Char("Url Website Front ",required=True)
    url_access_admin = fields.Char("Url website Admin",required=True)
    token_access = fields.Char("Access Token")


    def redirect_to_website_front(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': self.url_access_front,
        }


    def redirect_to_website_admin(self):
        url = self.url_access_admin
        if(self.token_access):
            url= "%s?%s" %(url,self.token_access)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url,
        }