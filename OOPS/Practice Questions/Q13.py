"""
Design a Payment System:

Base class: Payment
Subclasses:
    UPI
    Card
    NetBanking

Use:
    abstraction
    overriding
"""
from abc import ABC, abstractmethod

class Payement:
    @abstractmethod
    def pay(self):
        pass

class UPI(Payement):
    def pay(self, amount):
        print(f'Payment of {amount} is paid using UPI.')

class Card(Payement):
    def pay(self, amount):
        print(f'Payment of {amount} is paid using Card.')

class NetBanking(Payement):
    def pay(self, amount):
        print(f'Payment of {amount} is paid using NetBanking.')

def process(payment_method):
    payment_method.pay(10000)

process(UPI())
process(Card())
process(NetBanking())