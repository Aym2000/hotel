from odoo import api, fields, models


class Hotel_Room(models.Model):
    _name = "hotel.room"

    
    room_no = fields.Char(String = " Room No :" required = True)
    category_id = fields.Many2one(string = "category",  comodel_name="hotel.catagory")
    price = fields.Float(string = "price ", )
    minmum_price = fields.Float(string = "minmum price ", )

    
    




    # # relationships 
    # hotel_name = fields.Many2one("hotel_id")
    
    

