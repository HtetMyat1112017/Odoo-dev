import datetime
from odoo.exceptions import ValidationError
from odoo import models, fields, api

class RealEstate(models.Model):
    _name="real.estate"
    _description="Test Model"

    name=fields.Char(string="Name",default="Unknow")
    description=fields.Text(string="Description")
    postCode=fields.Char(string="Post Code")
    last_seen=fields.Date(string="Available From",default=lambda self:fields.Datetime.now())
    expected_price=fields.Float(string="Expected Price")
    selling_price=fields.Float(string="Selling Price")
    bedrooms=fields.Integer(string="BedRooms",default="2")
    living_area=fields.Integer(string="Living Area")
    facades=fields.Integer(string="Facades")
    garage=fields.Boolean(string="garage",default=False)
    garden=fields.Boolean(string="Garden",defaulth=False)
    garden_area=fields.Integer(string="Garden Area")
    garden_orientation=fields.Selection([('north','North'),('east','East'),('south','South'),('west','West')],string="Garden Orientation")
    # active=fields.Boolean(string="Active",default=False)
    status=fields.Selection([('sold','Sold'),('cancel','Cancel')])
    state=fields.Selection(selection=[
        ('new','New'),
        ('offer_received','Offer Received'),
        ('offer_accepted','Offer Accepted'),
        ('cancel','Canceled')
    ],string="status",default='new')
    
    offer_id=fields.One2many('estate.property.offer','property_id',string="Partner")
    sale_man=fields.Many2one('res.users',string="Sale Man")
    property_type=fields.Many2one('estate.property.type',string="Property Type")
    property_tag=fields.Many2many('estate.property.tag',string="Tag")
    total_area=fields.Integer(string="Total Area",compute="_compute_total_areas")
    buyer=fields.Char(string='Buyer')

    @api.constrains('name')
    def _check_name(self):
        for rec in self :
            if rec.name!=rec.name :
                raise ValidationError("can't be name the same")
   
    @api.onchange('garden')
    def onchange_check(self):
        if self.garden!=True :
            self.garden_area=0
        
    @api.depends('garden_area')
    def _compute_total_areas(self):
        for rec in self:
            rec.total_area =  12 *rec.garden_area

    def action_sold(self):
        for rec in self:
            if rec.state=="cancel":
                return ValidationError("can't be sold canceled item")
            else:
                rec.status="sold"
    def action_cancel(self):
        for rec in self:
            if rec.status=="sold":
                return ValidationError("can't be cancel solded item")
            else:
                rec.status='cancel'


class EstateProperyOffer(models.Model):
    _name="estate.property.offer"
    _description="estate property offer"

    price=fields.Float(string="Price")
    status=fields.Selection([('accepted','Accepted'),('refused','Refused')],string="status")
    partner=fields.Many2one('res.partner',String='partner')
    property_id= fields.Many2one('real.estate',string='Property id')

    @api.model
    def create(self,vals):
        property_id=self.env['real.estate'].browse(vals['property_id'])
        property_id.state='offer_received'
        return super(EstateProperyOffer, self).create(vals)

    def action_accepted(self):
        for rec in self:
            rec.status='accepted'
            rec.property_id.state="offer_accepted"

    def action_refused(self):
        for rec in self:
            rec.status='refused'
            rec.property_id.state="offer_refused"
    