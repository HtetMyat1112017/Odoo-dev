from odoo import api,fields,models

class EstateProperty(models.Model):
    _name="estate.property.type"
    _description="Estate Property Type"

    name=fields.Char(string="Name")
    
    
