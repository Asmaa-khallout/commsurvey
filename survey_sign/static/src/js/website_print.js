/* Copyright (c) 2018-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
odoo.define('survey_sign.website_print', function (require) {
	'use strict';

	var publicWidget = require('web.public.widget');
	publicWidget.registry.websiteCoupon = publicWidget.Widget.extend({
		selector: '.o_survey_print ',
		events: {
			'change .print_checkbox': '_onChangeConfirm',
		},
		_onChangeConfirm: function (ev) {
			console.log("cliiiick checkbox");
		},
	});
});