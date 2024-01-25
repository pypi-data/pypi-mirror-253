import unittest
from rpa_pdf import Stamp

stamp = Stamp()
TEST_FILES: list = [
    'c:\\temp\\file1.pdf',
    'c:\\temp\\file2.pdf'
]

class test_stamp(unittest.TestCase):
    def test_generate_code39_stamp(self):
        stamp.generate_code39_stamp('12345678', 'c:/temp/stamp.pdf', width=80, height=40, vertical_position='top', horizontal_position='center', page_vertical_margin=50)

    def test_add_code39_stamp(self):
        stamp.add_code39_stamp(TEST_FILES[0], TEST_FILES[1], '10000000', horizontal_position='center', vertical_position='top', page_horizontal_margin=5, page_vertical_margin=5)

    def test_add_text_stamp(self):
        stamp.add_text_stamp(TEST_FILES[0], TEST_FILES[1], 'dupa', text_horizontal_position='right', text_vertical_position='top')
        stamp.add_text_stamp(TEST_FILES[0], 'c:/temp/output_sample.pdf', 'dupa', text_horizontal_position='right', text_vertical_position='top', page_vertical_margin=22)


if __name__ == '__main__':
    unittest.main()