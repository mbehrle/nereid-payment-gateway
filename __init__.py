# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from party import Party, PaymentProfile


def register():
    Pool.register(
        Party,
        PaymentProfile,
        module='nereid_payment_gateway', type_='model'
    )
