from odoo import api, fields, models
# from odoo import api, fields, models, _

class HotelCustomer(models.Model):


    _name = "hotel.customer"
            
    name = fields.Char(string =  "name ")    
    email = fields.Char(string  = "email :")   
    country_id = fields.Many2one(string = "country " ,comodel_name="res.country")   
    
    passport_no = fields.Char(string = "passport_no")  
    nationality = fields.Char(string = "nationality")  
    x = fields.Float(string = "first num")
    y = fields.Float(string = "second num")
    result = fields.Float(string = "result :", readonly = True)
    
    
    def sum1(self):
        self.result = self.x + self.y

    def sum2(self):
        self.result = self.x - self.y

    def sum3(self):
        self.result = self.x * self.y

    def sum4(self):
        self.result = self.x / self.y
     
    
    

        
        











