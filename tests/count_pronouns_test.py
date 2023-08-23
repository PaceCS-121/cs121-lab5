import re
import count_pronouns

def test_count_pronouns_total(capsys):
    output = '960'
    count_pronouns.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_count_pronouns_freq(capsys):
    output = r'(?=.*you)(?=.*163)'
    count_pronouns.main()
    captured = capsys.readouterr()
    assert re.search(output, captured.out, re.IGNORECASE)