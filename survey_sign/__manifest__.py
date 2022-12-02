# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name' : "sign in servey form",
    'version' : "16.0.0.0",
    'description' : """
        
        

     """,
    'author' : "Asmaa Khallout",
    'website'  : "https://dkgroup.fr",
    'depends': ['survey','portal'],
    # 'external_dependencies': {
    #     'python': ['zxcvbn'],
    # },
    'data'     : ['views/survey_survey_views_inherit.xml',
                  'views/survey_inherit_template.xml',
                  'views/survey_template_frontend.xml',
                  'views/survey_user_input_views_inherit.xml',
                  ],
    'qweb': [
        'static/src/xml/survey_templates.xml',
    ],
    "assets": {'web.assets_frontend': ["/survey_sign/static/src/css/survey.css"]},
    'installable' : True,
    'application' :  True,
}
