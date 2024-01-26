import os
import unittest

from dwca.base import DarwinCoreArchive


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.object = DarwinCoreArchive.from_archive(os.path.join("example_data", "IRMNG_genera_DwCA.zip"))
        return

    def test_attributes(self):
        self.assertTrue(self.object.has_metadata(), "Doesn't have metadata")
        self.assertEqual(3, self.object.extensions(), "Missing or wrong number of extensions")


if __name__ == '__main__':
    unittest.main()
