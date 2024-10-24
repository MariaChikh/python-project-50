from gendiff.parser import parser
from gendiff.build_diff import build_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1 = parser(file_path1)
    file2 = parser(file_path2)
    diff = build_diff(file1, file2)
    if format_name == 'plain':
        format_diff = plain(diff)
    else:
        format_diff = stylish(diff)
    return format_diff
