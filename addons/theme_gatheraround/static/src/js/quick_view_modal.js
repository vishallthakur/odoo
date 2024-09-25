/** @odoo-module */

import Dialog from '@web/legacy/js/core/dialog';
import VariantMixin from '@website_sale/js/sale_variant_mixin';
import { WebsiteSale } from '@website_sale/js/website_sale';
import { uniqueId } from '@web/core/utils/functions';
import { jsonrpc } from '@web/core/network/rpc_service';


export const QuickViewModal = Dialog.extend(VariantMixin, {

    init: function (parent, params) {
        let self = this;

        let options = Object.assign({
            title: '',
            size: 'large',
            technical: !params.isWebsite,
            renderFooter: false
        }, params || {});

        this._super(parent, options);

        this.dialogClass = 'tg_product_quick_view';
        this.productId = params.productId;
        this.previousModalHeight = params.previousModalHeight;


        this._opened.then(function () {
            if (self.previousModalHeight) {
                self.$el.closest('.modal-content').css('max-height', self.previousModalHeight + 'px');
                self.$el.closest('.modal-dialog').addClass('modal-dialog-centered')
            }
        });

        this.rpc = this.bindService("rpc");

    },

    willStart: function () {
        let self = this;

        let url = "/shop/product/" + self.productId
        let getModalContent = $.get(url, {}, (modalContent) => {
            if (modalContent) {
                let $modalContent = $(modalContent).find("#product_detail_main");
                let $productDetailLink = `<div class="full_product_link">
                                            <a href='${url}'>
                                                <span>View full product detail</span>
                                                <i class="fa fa-arrow-circle-o-right"></i>
                                            </a>
                                        </div>`
                $modalContent.find('.o_wsale_product_images')?.append($productDetailLink)
                self.$content = $modalContent;
            } else {
                self.trigger('options_empty');
                self.preventOpening = true;
            }
        });

        let parentInit = self._super.apply(self, arguments);
        return Promise.all([getModalContent, parentInit]);
    },

    open: function (options) {
        $('.tooltip').remove(); // remove open tooltip if any to prevent them staying when modal is opened

        var self = this;
        this.appendTo($('<div/>')).then(function () {
            if (!self.preventOpening) {
                self.$modal.find(".modal-body").replaceWith(self.$el);
                self.$modal.attr('open', true);
                self.$modal.appendTo(self.container);
                const modal = new Modal(self.$modal[0], {
                    focus: true,
                });
                modal.show();
                self._openedResolver();
            }
        });
        if (options && options.shouldFocusButtons) {
            self._onFocusControlButton();
        }

        return self;
    },
});