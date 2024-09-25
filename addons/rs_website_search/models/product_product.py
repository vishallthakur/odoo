
from odoo import models, fields, _, api
from odoo.exceptions import ValidationError
from odoo.addons.http_routing.models.ir_http import slug, unslug


class ProductProductAdvanceSearch(models.Model):
    _inherit = [
        "product.product",
        'website.searchable.mixin',
    ]
    _name = "product.product"

    @api.model
    def _search_get_detail(self, website, order, options):
        with_image = options['displayImage']
        with_description = options['displayDescription']
        with_category = options['displayExtraLink']
        with_price = options['displayDetail']        
        domains = [website.sale_product_domain()]
        category = options.get('category')
        tags = options.get('tags')
        min_price = options.get('min_price')
        max_price = options.get('max_price')
        attrib_values = options.get('attrib_values')
        if category:
            domains.append([('public_categ_ids', 'child_of', unslug(category)[1])])
        if tags:
            domains.append([('all_product_tag_ids', 'in', tags)])
        if min_price:
            domains.append([('list_price', '>=', min_price)])
        if max_price:
            domains.append([('list_price', '<=', max_price)])
        if attrib_values:
            attrib = None
            ids = []
            for value in attrib_values:
                if not attrib:
                    attrib = value[0]
                    ids.append(value[1])
                elif value[0] == attrib:
                    ids.append(value[1])
                else:
                    domains.append([('attribute_line_ids.value_ids', 'in', ids)])
                    attrib = value[0]
                    ids = [value[1]]
            if attrib:
                domains.append([('attribute_line_ids.value_ids', 'in', ids)])

        search_fields = ['name', 'default_code', 'product_template_attribute_value_ids.name',]
        fetch_fields = ['id', 'name', 'website_url']
        mapping = {
            'name': {'name': 'name', 'type': 'text', 'match': True},
            'default_code': {'name': 'default_code', 'type': 'text', 'match': True},
            'website_url': {'name': 'website_url', 'type': 'text', 'truncate': False},
        }



        # sql_query = """ SELECT array_agg(id) 
        #     FROM advance_search 
        #     WHERE featured_product_type in ('new', 'featured', 'rated') 
        #     AND tabs_product_type IS NULL 
        #     AND is_active = 'true' 
        #     LIMIT 1;"""

        # self.env.cr.execute(sql_query)
        # search_fields_id = self.env.cr.fetchone()[0] or []
        active_advance_search = self.env['advance.search'].search([('website_id', '=', website.id), ('model_id.model', '=', self._name), ('is_active', '=', True)])
        

        for field in active_advance_search.field_ids:
            field_name = field.name if not field.relation else field.name + ".name"
            if field_name not in search_fields:
                search_fields.append(field_name)

            if not mapping.get(field_name, False):
                mapping.update({
                    field_name: {'name': field_name, 'type': 'text', 'match': True}
                })

        if with_image:
            mapping['image_url'] = {'name': 'image_url', 'type': 'html'}
        if with_description:
            search_fields.append('description')
            fetch_fields.append('description')
            search_fields.append('description_sale')
            fetch_fields.append('description_sale')
            mapping['description'] = {'name': 'description_sale', 'type': 'text', 'match': True}
        if with_price:
            mapping['detail'] = {'name': 'price', 'type': 'html', 'display_currency': options['display_currency']}
            mapping['detail_strike'] = {'name': 'list_price', 'type': 'html', 'display_currency': options['display_currency']}
        if with_category:
            mapping['extra_link'] = {'name': 'category', 'type': 'html'}        
        return {
            'model': 'product.product',
            'base_domain': domains,
            'search_fields': search_fields,
            'fetch_fields': fetch_fields,
            'mapping': mapping,
            'icon': 'fa-shopping-cart',
        }


    def _search_render_results(self, fetch_fields, mapping, icon, limit):
        with_image = 'image_url' in mapping
        with_category = 'extra_link' in mapping
        with_price = 'detail' in mapping
        with_default_code = 'default_code' in mapping
        with_attribute_values = 'product_template_attribute_value_ids.name' in mapping
        results_data = super()._search_render_results(fetch_fields, mapping, icon, limit)
        current_website = self.env['website'].get_current_website()
        for product, data in zip(self, results_data):
            if with_price:
                categ_ids = product.public_categ_ids.filtered(lambda c: not c.website_id or c.website_id == current_website)
                combination_info = product._get_combination_info_variant()
                monetary_options = {'display_currency': mapping['detail']['display_currency']}
                data['price'] = self.env['ir.qweb.field.monetary'].value_to_html(combination_info['price'], monetary_options)
                if combination_info['has_discounted_price']:
                    data['list_price'] = self.env['ir.qweb.field.monetary'].value_to_html(combination_info['list_price'], monetary_options)
            if with_image:
                data['image_url'] = '/web/image/product.product/%s/image_128' % data['id']

            if with_category and product.public_categ_ids:
                data['category'] = self.env['ir.ui.view'].sudo()._render_template(
                    "website_sale.product_category_extra_link",
                    {'categories': categ_ids, 'slug': slug}
                )
            if with_default_code and product.default_code:
                data['default_code'] = product.default_code
            if with_attribute_values and product.product_template_attribute_value_ids:
                data['product_template_attribute_value_ids.name'] = ', '.join(product.product_template_attribute_value_ids.mapped('name'))

        return results_data    
    
    