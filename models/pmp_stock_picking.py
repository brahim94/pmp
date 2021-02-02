from odoo import models, fields, api
import qrcode
import base64
from io import BytesIO
from odoo.http import request

def generate_qr_code(url):
    qr = qrcode.QRCode(
             version=1,
             error_correction=qrcode.constants.ERROR_CORRECT_L,
             box_size=20,
             border=4,
             )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    temp = BytesIO()
    img.save(temp, format="PNG")
    qr_img = base64.b64encode(temp.getvalue())
    return qr_img
    

class PurchaseOrderLine(models.Model):
    _inherit = "stock.move.line"

    sequence = fields.Integer(string="sequence", default=10)

    number = fields.Integer(
        compute='_compute_get_number',
        store=True,
    )
    
    @api.depends('sequence', 'picking_id')
    def _compute_get_number(self):
        for order in self.mapped('picking_id'):
            number = 1
            for line in order.move_line_ids_without_package:
                line.number = number
                number += 1

class Picking(models.Model):
    _inherit = "stock.picking"
    

    qr_image = fields.Binary("QR Code", compute='_generate_qr_code')

    def _generate_qr_code(self):
        base_url = request.env['ir.config_parameter'].get_param('web.base.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        self.qr_image = generate_qr_code(base_url)
    
    def update_sequence(self):
        sequence = 0
        for line in self.move_line_ids_without_package:
            sequence += 1
            line.sequence = sequence
        return True

    @api.model
    def create(self, vals):
        res = super(Picking, self).create(vals)
        if vals.get('move_line_ids_without_package'):
            res.update_sequence()
        return res

    def write(self, vals):
        res = super(Picking, self).write(vals)
        if vals.get('move_line_ids_without_package'):
            self.update_sequence()
        return res
