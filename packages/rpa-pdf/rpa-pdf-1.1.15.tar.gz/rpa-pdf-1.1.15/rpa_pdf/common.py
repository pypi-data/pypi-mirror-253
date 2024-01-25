
import os
from contextlib import contextmanager
from comtypes import COMError, errorinfo

def set_x_pos(horizontal_position, page_horizontal_margin, page_width, stamp_width) -> float:
    match horizontal_position:
        case 'center':
            return (page_width / 2) - (stamp_width / 2) + page_horizontal_margin
        case 'right':
            return page_width - stamp_width - page_horizontal_margin
        case _:
            return page_horizontal_margin

def set_y_pos(vertical_position, page_vertical_margin, page_height, stamp_height) -> float:
    match vertical_position:
        case 'center':
            return (page_height / 2) - (stamp_height / 2) + page_vertical_margin
        case 'bottom':
            return page_height - stamp_height - page_vertical_margin
        case _:
            return page_vertical_margin

def parse_output_file_path(input_file_path: str, output_file_path: str) -> str:
        return f'{os.path.splitext(input_file_path)[0]}.pdf' if output_file_path is None else output_file_path
