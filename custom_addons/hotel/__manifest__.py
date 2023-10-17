{
    'name': 'Employees',
    'version': '1.1',
    'sequence': 95,


    'depends': ['base','hr'],
    'data': [
            'views/hotel_invoice.xml',
            'views/hotel_room.xml',
            'views/hotel_customer.xml',
            'views/hotel_room_catagory.xml',
            'views/menu.xml',
    ],
    
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
