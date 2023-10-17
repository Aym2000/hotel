from odoo import api, fields, models


class Hotel_Catagory(models.Model):
    
    _name = "hotel.catagory"

    name = fields.Char(String = " name ")
    NOR = fields.Integer(String = " number of rooms",)

    employee_id = fields.Many2many(comodel_name ='hr.employee', string="Team")
    room_ids = fields.One2many(comodel_name ='hotel.room',   inverse_name ='category_id' ,string = "Rooms")
    #                            target model  reverse Id

    def addratio(self):
        
        print('-------------',self.room_ids)
        for x in self.room_ids:
            if x.id==7:
                x.unlink()
                continue
            print('-------------room_no',x.room_no)
            print('-------------price',x.price)
            print('-------------minmum_price',x.minmum_price)

            x.price = x.price + 1
            
        
    
    






    
    
    

