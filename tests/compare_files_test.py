import re
import compare_files

def test_compare_files_chars(capsys):
    output = r"(?=.*file3.txt)(?=.*1251)"
    compare_files.main()
    captured = capsys.readouterr()
    assert re.search(output, captured.out, re.IGNORECASE)

def test_compare_files_lines(capsys):
    output = r"(?=.*file2.txt)(?=.*12)"
    compare_files.main()
    captured = capsys.readouterr()
    assert re.search(output, captured.out, re.IGNORECASE)

def test_compare_files_words(capsys):
    output = r"(?=.*file3.txt)(?=.*203)"
    compare_files.main()
    captured = capsys.readouterr()
    assert re.search(output, captured.out, re.IGNORECASE)