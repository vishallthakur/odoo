
from odoo import models, fields, api


class AdvanceSearch(models.Model):
    _name = 'advance.search'
    _description = 'Advance Search'

    website_id = fields.Many2one(
        string='Website',
        comodel_name='website',
        ondelete='cascade',
    )
    
    sequence = fields.Integer(
        string='Sequence',
    )
    
    model_id = fields.Many2one(
        string='Model',
        comodel_name='ir.model',
        required=True,
        domain="[('model', 'in', ['product.template', 'product.product', 'product.public.category'])]",
        ondelete='cascade',
    )
    
    field_ids = fields.Many2many(
        string='Field',
        comodel_name='ir.model.fields',
        required=True,
        ondelete='cascade',
    )
    
    is_active = fields.Boolean(
        string='Is Active',
    )

    def write(self, vals):
        if vals.get('is_active', False):
            active_advance_search = self.env['advance.search'].search([('website_id', '=', self.website_id.id), ('model_id', '=', self.model_id.id), ('is_active', '=', True)])
            active_advance_search.is_active = False
        return super().write(vals)
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('is_active', False):
                active_advance_search = self.env['advance.search'].search([('website_id', '=', vals.get('website_id', False)), ('model_id', '=', vals.get('model_id', False)), ('is_active', '=', True)])
                active_advance_search.is_active = False
        return super().create(vals_list)