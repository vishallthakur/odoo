
from odoo import models, fields, api

class WebsiteAdvanceSearch(models.Model):
    _inherit = "website"
    
    advance_search_ids = fields.One2many(
        string='Advance Search',
        comodel_name='advance.search',
        inverse_name='website_id',
    )
    
    search_in = fields.Selection(
        string='Search In',
        selection=[('product', 'Product'), ('variant', 'Variant'), ('both', 'Both (Product/Variant)')],
    )

    def _search_get_details(self, search_type, order, options):
        result = super()._search_get_details(search_type, order, options)

        if options.get('autocomplete_search_in', False):
            for res in result.copy():
                if res.get('model', False) and res.get('model', False) == 'product.template' and options.get('autocomplete_search_in', '') == "variant":
                    result.remove(res)
                    continue

            if search_type in ['products', 'products_only', 'all'] and options.get('autocomplete_search_in', False) in ['variant', 'both']:
                result.append(self.env['product.product']._search_get_detail(self, order, options))

        return result