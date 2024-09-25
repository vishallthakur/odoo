/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
import { _t } from "@web/core/l10n/translation";


publicWidget.registry.websiteSaleSliderPopover = publicWidget.Widget.extend({
    selector: '#wrapwrap',

    read_events: {
        'click .icons .o_wsale_my_wish, .icons .o_wsale_my_cart, .icons .user_slider, .icons .setting_slider': '_onClickSliderIcons',
        'click #close_slider' : '_closeSlider',
    },

    init: function() {
        this._super.apply(this, arguments);
        this.classToIconMap = {
            'o_wsale_my_wish': 'wishlist',
            'o_wsale_my_cart': 'cart',
            'user_slider': 'user',
            'setting_slider': 'setting',
        };
        this.selected_icon = "wishlist";
    },

    start: function () {
        var def = this._super.apply(this, arguments);
        // if (this.editableMode) {
        //     return def;
        // }
        // this.main_nav = $('#oe_main_menu_navbar');
        return def;
    },

    _onClickSliderIcons: function (event) {
        var self = this;
        event.preventDefault();
        event.stopPropagation();
        var $slider = $("#right_slider_popover");
        if (!$slider.hasClass('slide_left')) {
            $slider.toggleClass('slide_left')
            $(event.currentTarget).closest('.icons').toggleClass('slide_left')
        }

        Object.keys(self.classToIconMap).forEach(className => {
            if ($(event.currentTarget).hasClass(className)) {
                self.selected_icon = self.classToIconMap[className];
                return false; // Exit loop once a matching class is found
            }
        });

        $.get("/slider/content", {
            content: self.selected_icon,
        }).then(function (data) {
            $('.dynamic_slider_content').html(data)
        });        
    },

    _closeSlider: function(event) {
        var $slider = $("#right_slider_popover");
        $slider.toggleClass('slide_left')
        $('div.icons').toggleClass('slide_left')
    }
});

publicWidget.registry.StandardAffixedHeader.include({
});