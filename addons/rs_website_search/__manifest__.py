{
    "name"                  : "Advance Website Search",
    "summary"               : """""",
    "category"              : "Website",
    "version"               : "1.0.0",
    "author"                : "",
    "license"               : "LGPL-3",
    "maintainer"            : "",
    "website"               : "https://store.webkul.com",
    "description"           : """""",
    "depends"               : [
                                "website_sale",
                            ],
    "data"                  : [
                                "security/ir.model.access.csv",
                                "views/snippets/snippets.xml",
                                "views/website_view.xml",
                                "views/res_config_setting_view.xml",
                            ],
    "assets"                : {
                                'web.assets_frontend': [
                                ],
                            },    
    "application"           : True,
    "installable"           : True,
    "auto_install"          : False,   
    "pre_init_hook"         :  "pre_init_check",
}
