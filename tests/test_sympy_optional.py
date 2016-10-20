from decimal import Decimal

from .base import MeasurementTestBase


from sympy import S, Symbol
from decimal import Decimal

from measurement.base import MeasureBase


class Temperature_Sympy(MeasureBase):
    SU = Symbol('kelvin')
    STANDARD_UNIT = 'k'
    UNITS = {
        'c': SU - S(273.15),
        'f': (SU - S(273.15)) * S('9/5') + 32,
        'k': Decimal('1.0')
    }
    ALIAS = {
        'celsius': 'c',
        'fahrenheit': 'f',
        'kelvin': 'k',
    }


class TemperatureTest_WithSymPy(MeasurementTestBase):
    def test_sanity(self):
        fahrenheit = Temperature_Sympy(fahrenheit=70)
        celsius = Temperature_Sympy(celsius=21.1111111)

        self.assertAlmostEqual(
            fahrenheit.k,
            celsius.k
        )

    def test_conversion_to_non_si(self):
        celsius = Temperature_Sympy(celsius=21.1111111)
        expected_farenheit = 70

        self.assertAlmostEqual(
            celsius.f,
            expected_farenheit
        )

    def test_ensure_that_we_always_output_decimal(self):
        kelvin = Temperature_Sympy(kelvin=10)

        celsius = kelvin.c

        self.assertTrue(
            isinstance(celsius, Decimal)
        )
