{
    "name": "Smart Inventory BI Dashboard (PostgreSQL View)",
    "version": "19.0.1.0.0",
    "category": "Inventory",
    "summary": "Show BI dashboard in Odoo from PostgreSQL view bi_stock_moves",
    "author": "Your Team",
    "depends": ["stock"],   # chỉ cần stock để chạy menu và pivot; sale/crm/purchase có thì dữ liệu phong phú hơn
    "data": [
        "security/ir.model.access.csv",
        "views/bi_stock_moves_views.xml",
    ],
    "installable": True,
    "application": True,
}
