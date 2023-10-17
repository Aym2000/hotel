from odoo import api, fields, models
from datetime import date, datetime

class hotel_invoice(models.Model): 
    
    _name = "hotel.invoice"
    reservation_no = fields.Char(string = "reservation no")
    customer_id = fields.Many2one(string = "customer", comodel_name = "hotel.customer")
    room_id  = fields.Many2one(string = "room", comodel_name = "hotel.room")
    invoice_date = fields.Date(string = "invoice date", default=datetime.today())
    date_check_in = fields.Date(string = "check-in")
    date_check_out = fields.Date(string = "data check-out")
    actual_price = fields.Float(string = "actual price")
    state = fields.Selection([
        
            ('new', 'New'),
            ('run', 'Run'),
            ('close', 'close'),
           ('cancel','cancel'),
        ], required = True, readonly = True,
        default = 'new'
    )


    











