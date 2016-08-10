from openerp import models, fields

class PurchaseContractWithAttachment(models.Model):
    _inherit = ['sale.subscription']
    
    attachments_ids = fields.Many2many('ir.attachment', string="Attachments")
