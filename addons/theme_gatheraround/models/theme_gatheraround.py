from odoo import api, models


class ThemeGatherAround(models.AbstractModel):
    _inherit = 'theme.utils'

    @api.model
    def _reset_default_config(self):

        self.disable_view('theme_gatheraround.template_ga_header_1')
        self.disable_view('theme_gatheraround.template_ga_header_2')
        self.disable_view('theme_gatheraround.template_ga_header_3')
        self.disable_view('theme_gatheraround.template_ga_header_4')

        super(ThemeGatherAround, self)._reset_default_config()
