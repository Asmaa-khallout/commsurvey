from odoo import http, _, fields, SUPERUSER_ID
import logging
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
import binascii
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from odoo.tools import format_datetime, format_date, is_html_empty
_logger = logging.getLogger(__name__)

from odoo.addons.survey.controllers.main import Survey

class SignSurvey(http.Controller):
    @http.route(['/sign/survey/<int:answer_id>/accept'], type='json', auth="public", website=True)
    def sign_accept(self, answer_id, access_token=None, name=None, signature=None):
        _logger.info("docummmeent %s " %(answer_id))
        access_token = access_token or request.httprequest.args.get('access_token')
        try:
            #answer_sudo = CustomerPortal.with_user(SUPERUSER_ID)._document_check_access(self,'survey.user_input', answer_id, access_token=access_token)
            answer_sudo = request.env['survey.user_input'].browse(answer_id)
        except (AccessError, MissingError,Exception) as e:
            return {'error': _('Invalid Answer. %s' %(e))}

        try:
            answer_sudo.sudo().write({
                'signed_by': name,
                'signed_on': fields.Datetime.now(),
                'signature': signature,
            })
            request.env.cr.commit()
        except (TypeError, binascii.Error) as e:
            return {'error': _('Invalid signature data.')}

        return {
            'force_refresh': True,
            'redirect_url': '/survey/print/%s?answer_token=%s' % (answer_sudo.sudo().survey_id.access_token, answer_sudo.sudo().access_token),
        }


    @http.route(['/sign/survey/<int:answer_id>/refu'], auth="public", website=True)
    def sign_accept(self, answer_id, motif=None):
        try:
            answer_sudo = request.env['survey.user_input'].browse(answer_id)
        except (AccessError, MissingError,Exception) as e:
            return {'error': _('Invalid Answer. %s' %(e))}

        try:
            answer_sudo.sudo().write({
                'motif': motif,
            })
            request.env.cr.commit()
        except Exception as e:
            return {'error': _('Invalid motif data.')}

        return request.redirect('/survey/print/%s?answer_token=%s' % (answer_sudo.sudo().survey_id.access_token, answer_sudo.sudo().access_token))



