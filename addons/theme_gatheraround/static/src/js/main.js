/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
import { throttleForAnimation } from "@web/core/utils/timing";

var $wrapwrap = $("#wrapwrap");

export function apply_overlay(ev) {
    $wrapwrap.addClass("apply_overlay");
    $wrapwrap.css('overflow', "hidden");
    if ($(window).innerWidth() > 1200) {
        $wrapwrap.css("padding-right", "10px");
    }
    $("#top").css('z-index', 'auto');
};

export function remove_overlay() {
    $wrapwrap.removeClass("apply_overlay");
    $wrapwrap.css('overflow', "").css("padding-right", "");
    $("#top").css('z-index', '');
}