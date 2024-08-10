

from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website_sale.controllers.delivery import WebsiteSaleDelivery
from odoo.exceptions import AccessError, MissingError, UserError
from odoo.addons.website.controllers.main import Website
from odoo.http import request


class WebsiteAdvanceSearch(Website):
    
    @http.route()
    def autocomplete(self, search_type=None, term=None, order=None, limit=5, max_nb_chars=999, options={},**kwargs):
        website = request.env['website'].get_current_website()
        
        if website.search_in:
            options.update({
                'autocomplete_search_in': website.search_in,
        })
            
        return super().autocomplete(search_type, term, order, limit, max_nb_chars, options, **kwargs)