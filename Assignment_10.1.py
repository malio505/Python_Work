#Reading and writing to a file.
#Begaye, Gamaliel
#11/7/2021

#Importing from employee log.
from _typeshed import Self
import logging


logging.basicConfig(filename='Employee.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')
#Setting up a class for my employee information.
class Employee:
    """Employee's name, address, and phone number"""

def __init__(Self, first, last, address, phonenumber):
    Self.first= first
    Self.last= last
    Self.address= address
    Self.phonenumber= phonenumber

print('Created Employee: {} - {}'.format(Self.fullname, Self.address, Self.phonenumber))

def address(self):
    return '{}'.format(self.first, self.last) 

def phonenumber(self):
    return '{}'.format(self.first, self.last) 