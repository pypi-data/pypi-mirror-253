import os
import unittest

from eml.base import EML
from dwca.utils import Language


class TestEML(unittest.TestCase):
    def setUp(self) -> None:
        self.eml = EML.from_xml(os.path.join("example_data", "eml.xml"))
        return

    def test_parse(self):
        self.assertEqual(self.eml.package_id, "IRMNG_export_2023-05-19")
        self.assertEqual(self.eml.language, Language.ENG)


if __name__ == '__main__':
    unittest.main()
