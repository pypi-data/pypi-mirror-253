# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase


class NereidBaseTestCase(ModuleTestCase):
    "Test Nereid Base module"
    module = 'nereid_base'


del ModuleTestCase
