from odoo import api,models,fields,Command

class EstateInvoice(models.Model):
    _inherit="real.estate"
    
    def action_sold(self):
        invoice_vals={
            'partner_id':self.offer_id.id,
            'move_type':'out_invoice',
            'invoice_line_ids':[
                Command.create({
                    'name':'Selling Price Commission',
                    'quantity':1,
                    'price_unit':self.selling_price  * 0.06
                }),
            ]
        }
        self.env['account.move'].create(invoice_vals)
        return super(EstateInvoice, self).action_sold()
    
 

   