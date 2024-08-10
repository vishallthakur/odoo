
from odoo import models, fields

class ResConfigSettingsAdvanceSearch(models.TransientModel):
    _inherit = 'res.config.settings'

    search_in = fields.Selection(
        string='Search In',
        selection=[('product', 'Product'), ('variant', 'Variant'), ('both', 'Both (Product/Variant)')],
        related='website_id.search_in',
        readonly=False,
    )    