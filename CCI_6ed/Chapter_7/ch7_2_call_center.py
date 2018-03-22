"""Imagine you have a call center with three levels of employees:
respondent, manager, and director. An incoming telephone call must be
first allocated to a respondent who is free. If the respondent can't
handle the call, he or she must escalate the call to a manager. If
the manager is not free or not able to handle it, then the call
should be escalated to a director. Design the classes and data
structures for this problem. Implement a method dispatchCall() which
assigns a call to the first available employee."""

import time
from collections import deque
import random

class Employee(object):
    """Base Employee class"""
    def __init__(self, name):
        self.name = name
        self.on_call = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '<{} - {}>'.format(self.name, 'free' if self.is_free else 'busy')

    def is_free(self):
        """Determine if an employee is free to receive a call."""
        if self.on_call:
            return False
        return True

    def take_call(self, call):
        """Attach employee to an incoming call"""
        self.on_call = call
        self.on_call.connect(self)
        print('{} answered a call from {}'.format(self.name, call.originator))

    def hang_up(self):
        call = self.on_call
        self.on_call = None
        if call:
            call.disconnect()
        print('{} ended a call from {}'.format(self.name, call.originator))

    def arrive(self, callcenter):
        self.callcenter = callcenter
        self.callcenter.employee_arrives(self)

    def leave(self):
        self.callcenter.employee_leaves(self)

class Respondent(Employee):
    """Respondent employee type"""
    def __init__(self, name):
        super().__init__(name)

class Manager(Employee):
    """Manager employee type"""
    def __init__(self, name):
        super().__init__(name)

class Director(Employee):
    """Director employee type"""
    def __init__(self, name):
        super().__init__(name)

class Call(object):
    """Call"""
    def __init__(self, originator):
        """Originator might be caller ID info or caller name"""
        self.originator = originator
        self.call_start = None
        self.call_end = None
        self.notes = None
        self.employee = None

    def call_notes(self, notes):
        """Update notes about the call."""
        self.notes = notes

    def connect(self, employee):
        """Answer an incoming call."""
        self.call_start = time.time()
        self.employee = employee

    def disconnect(self):
        """Disconnect the call."""
        self.call_end = time.time()
        if self.employee.on_call is self:
            self.employee.hang_up()
        
class CallCenter(object):
    """Call Center"""
    def __init__(self):
        self.employees = {}

    def employee_arrives(self, employee):
        employee_type = employee.__class__.__name__
        if employee_type not in self.employees:
            self.employees[employee_type] = set()
        self.employees[employee_type].add(employee)

    def employee_leaves(self, employee):
        employee_type = employee.__class__.__name__
        self.employees.get(employee_type, set()).discard(employee)

    def dispatch_call(self, call):
        available = [emp for emp in self.employees.get('Respondent',[]) if emp.is_free()]
        if available:
            random.choice(available).take_call(call)
            return
        available = [emp for emp in self.employees.get('Manager',[]) if emp.is_free()]
        if available:
            random.choice(available).take_call(call)
            return
        available = [emp for emp in self.employees.get('Director',[]) if emp.is_free()]
        if available:
            random.choice(available).take_call(call)
            return
        print('No one available to answer call from {}'.format(call.originator))
        return IndexError('No one is available to take the call.')


if __name__ == "__main__":
    mindy = Respondent('Mindy Lahiri')
    fonzie = Respondent('Arthur Fonzarelli')
    mork = Manager('Mork von Ork')
    orson = Director('Orson Wells')
    telefraud = CallCenter()
    telefraud.employee_arrives(mindy)
    telefraud.employee_arrives(fonzie)
    telefraud.employee_arrives(mork)
    telefraud.employee_arrives(orson)
    telefraud.dispatch_call(Call('Moaning Myrtle'))
    telefraud.dispatch_call(Call('Professor Snape'))
    telefraud.dispatch_call(Call('Albus Dumbledore'))
    telefraud.dispatch_call(Call('Lucius Malfoy'))
    mork.hang_up()
    telefraud.dispatch_call(Call('Rubeus Hagrid'))

    
    
    
    
        
        
        
