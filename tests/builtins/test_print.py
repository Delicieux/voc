from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class PrintTests(TranspileTestCase):
    pass


class BuiltinPrintFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["print"]

    not_implemented = [
        'test_bytearray',
        'test_class',
        'test_complex',
        'test_frozenset',
        'test_slice',
    ]
