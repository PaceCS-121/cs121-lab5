import re
import contact_info

def test_contact_info_911(capsys, monkeypatch):
    inputs = "Emergency"
    output = "911"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    contact_info.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_contact_info_security(capsys, monkeypatch):
    inputs = "Pace Security"
    output = "914-773-3400"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    contact_info.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_contact_info_missing(capsys, monkeypatch):
    inputs = "Ghostbusters"
    missing = [
        r'(\d){3}-(\d){3}-(\d){4}',
        r'(\d){3}'
    ]
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    contact_info.main()
    captured = capsys.readouterr()
    for pattern in missing:
        assert re.search(pattern, captured.out) is None