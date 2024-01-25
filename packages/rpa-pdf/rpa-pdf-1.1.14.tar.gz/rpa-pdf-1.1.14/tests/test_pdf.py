import unittest
import os
from rpa_pdf import Pdf

PDF: Pdf = Pdf()
TEST_FILES: list = [
    'c:\\temp\\file1.pdf',
    'c:\\temp\\file2.pdf'
]

class test_pdf(unittest.TestCase):
    def test_compress(self) -> None:
        print(os.stat(TEST_FILES[0]).st_size)
        PDF.compress(TEST_FILES[0])
        print(os.stat(TEST_FILES[0]).st_size)

    def test_text_to_pdf(self):
        PDF.text_to_pdf('abcdef', TEST_FILES[0])
    
    def test_merge(self) -> None:
        PDF.merge(TEST_FILES, 'c:/temp/merged.pdf')
    
    def test_print(self) -> None:
        PDF.print(TEST_FILES[0], printer='Bullzip PDF Printer')
        PDF.print(TEST_FILES[1])


if __name__ == '__main__':
    unittest.main()
