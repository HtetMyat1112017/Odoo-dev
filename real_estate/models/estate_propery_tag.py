from odoo import api,fields,models

class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description="estate property tag"

    tag_name=fields.Char(string="Tag Name",required=True)