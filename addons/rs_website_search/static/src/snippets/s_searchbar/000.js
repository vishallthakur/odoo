/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { markup } from "@odoo/owl";
import { jsonrpc } from "@web/core/network/rpc_service";

publicWidget.registry.searchBar.include({
    _getFieldsNames() {
        var res = this._super.apply(this, arguments);
        res.push('default_code')
        res.push('product_template_attribute_value_ids.name')
        return res
    },
})