/* Copyright (c) 2018-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
odoo.define('survey_sign.website_print', function (require) {
	'use strict';

	var publicWidget = require('web.public.widget');
	publicWidget.registry.websiteCoupon = publicWidget.Widget.extend({
		selector: '.o_survey_print ',
		events: {
			'change .print_checkbox': '_onChangeConfirm',
			'click .btn_sign': '_onClickSign',
			'click .btn_rufu': '_onClickRefu',
		},
		_onChangeConfirm: function (ev) {
		if(ev.target.checked){
		$('.btn_sign').removeClass( "disabled");
		}
		else{
		$('.btn_sign').addClass( "disabled")
		}
		},
		_onClickSign: function (ev) {
		if($('#confirm_print').prop('checked')){
		$('#open_signature_modal').modal('toggle');
		}
		},
		_onClickRefu: function (ev) {
		if(!$('#confirm_print').prop('checked')){
		$('#refu_signature_modal').modal('toggle');
		}
		},
	});
});