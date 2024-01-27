import os
import unittest

from dwca.base import DarwinCoreArchive
from dwca.utils import Language


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.object = DarwinCoreArchive.from_archive(os.path.join("example_data", "IRMNG_genera_DwCA.zip"))
        return

    def test_attributes(self):
        self.assertTrue(self.object.has_metadata(), "Doesn't have metadata")
        self.assertEqual(3, len(self.object.extensions), "Missing or wrong number of extensions")
        self.assertEqual("taxon.txt", self.object.core.filename, "Wrong filename in Core")
        self.assertCountEqual(
            ["speciesprofile.txt", "reference.txt", "identifier.txt"],
            [extension.filename for extension in self.object.extensions],
            "Extension not read"
        )
        self.assertEqual(
            "The Interim Register of Marine and Nonmarine Genera", self.object.title, "Wrong title"
        )
        self.assertEqual(
            "The Interim Register of Marine and Nonmarine Genera [eng]",
            str(self.object),
            "Wrong representation"
        )
        self.assertEqual(
            "<Darwin Core Archive (The Interim Register of Marine and Nonmarine Genera [eng])>",
            repr(self.object),
            "Wrong representation"
        )
        self.assertEqual(Language.ENG, self.object.language, "Wrong language")


if __name__ == '__main__':
    unittest.main()
