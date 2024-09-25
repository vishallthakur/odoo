from odoo import fields, http, tools
from odoo.http import Controller, request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class GatherAroundWebsiteSale(WebsiteSale):
    @http.route(["/slider/content"], type="http", website=True, auth="public")
    def featured_products_data(self, **kwargs):
        content = kwargs.get("content", False)
        icons = {"cart": "fa-shopping-cart", "wishlist": "fa-heart", "user": "fa-user", "setting": "fa-gear"}
        titles = {"cart": "Your Cart", "wishlist": "Your Wishlist", "user": "Account & Information", "setting": "Settings"}
        values = {"content": content, "_icon_class": icons.get(content), "slider_title": titles.get(content)}

        if content == "cart":
            website_sale_order_lines = (
                request.website.sale_get_order().website_order_line
            )
            values.update({"lines": website_sale_order_lines})

        if content == "wishlist":
            wishlist_lines = (
                request.env["product.wishlist"]
                .with_context(display_default_code=False)
                .current()
            )
            values.update({"lines": wishlist_lines})

        return request.render("theme_gatheraround.slider_cart_content", values)