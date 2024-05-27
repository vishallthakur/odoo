{
    "name"                  : "Theme Gather Around",
    "summary"               : """Odoo Website Theme: Gather Around .""",
    "category"              : "Theme/Corporate",
    "version"               : "1.0.0",
    "sequence"              : 1,
    "author"                : "",
    "license"               : "Other proprietary",
    "website"               : "",
    "description"           : """GatherAround theme""",
    "live_test_url"         : "",
    "depends"               : [
                                "website_sale",
                                "website_sale_wishlist",
                                "website_sale_comparison",
                                "website_sale_stock",
                            ],
    "data"                  : [
                                "views/slider_template.xml",
                                "views/header_template.xml",
                                "views/snippets.xml",
                            ],
    "demo"                  : [],
    "images"                : [],
    "assets"                : {
                                "web.assets_frontend": [
                                    "theme_gatheraround/static/src/scss/slider_popover.scss",
                                    "theme_gatheraround/static/src/scss/headers.scss",
                                    "theme_gatheraround/static/src/js/main.js",
                                    "theme_gatheraround/static/src/js/headers.js",
                                ],
                                "web._assets_primary_variables": [
                                    "theme_gatheraround/static/src/scss/primary_variables.scss",
                                ],
                                "web._assets_secondary_variables": [
                                    "theme_gatheraround/static/src/scss/secondary_variables.scss",
                                ],
                            },
    "installable"           : True,
    "auto_install"          : False,
    "price"                 : 149,
    "currency"              : "USD",
    "pre_init_hook"         : "pre_init_check",
}