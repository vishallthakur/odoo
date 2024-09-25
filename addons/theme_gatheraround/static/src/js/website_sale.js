/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import VariantMixin from "@website_sale/js/variant_mixin";
import wSaleUtils from "@website_sale/js/website_sale_utils";
import WebsiteSale from '@website_sale_stock/js/website_sale';
const cartHandlerMixin = wSaleUtils.cartHandlerMixin;
import "@website/libs/zoomodoo/zoomodoo";
import { extraMenuUpdateCallbacks } from "@website/js/content/menu";
import { ProductImageViewer } from "@website_sale/js/components/website_sale_image_viewer";
import { jsonrpc } from "@web/core/network/rpc_service";
import { debounce, throttleForAnimation } from "@web/core/utils/timing";
import { listenSizeChange, SIZES, utils as uiUtils } from "@web/core/ui/ui_service";
import { Component } from "@odoo/owl";
import { QuickViewModal } from "@theme_gatheraround/js/quick_view_modal";


WebsiteSale.include({

    events: Object.assign({}, WebsiteSale.prototype.events, {
        'click .tg-add-to-cart .a-submit': 'async _onClickAdd',
        'click .o_wsale_product_btn .tg-product-quick-view': '_onClickQuickView'
    }),

    start: function () {
        this._super(...arguments);
        let rootStyle = $(':root');
        rootStyle.css('--grid-product-image-height', $('#products_grid .oe_product_image:first')?.height() + "px");
    },

    _onClickQuickView: function (event) {
        this.QuickViewModal = new QuickViewModal(this, {
            productId: $(event.currentTarget).data('productTemplateId'),
            isWebsite: true,
            previousModalHeight: "500"
        }).open();
    }

});