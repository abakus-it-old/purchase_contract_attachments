from openerp import models, fields

class PurchaseContractWithAttachment(models.Model):
    _inherit = 'account.analytic.account'
    
    attachments_ids = fields.Many2many('ir.attachment', string="Attachments")