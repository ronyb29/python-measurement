from decimal import Decimal as D

from measurement.base import MeasureBase, SimpleTransform as ST

__all__ = ['Temperature']


class Temperature(MeasureBase):
    STANDARD_UNIT = 'k'
    UNITS = {
        'c': ST(to=lambda c: c + D('273.15'),
                fro=lambda k: k - D('273.15')),
        'f': ST(to=lambda f: (f + D('459.67')) * D(5) / D(9),
                fro=lambda k: k * D(9) / D(5) - D('459.67')),
        'k': D('1.0')
    }
    ALIAS = {
        'celsius': 'c',
        'fahrenheit': 'f',
        'kelvin': 'k',
    }
