import re
import store

def test_store(capsys, monkeypatch):
    # test that program asks for 5 inputs and outputs a message with a number
    inputs = iter(['1', '2', '1', '2', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    store.main()
    captured = capsys.readouterr()
    total_cost = re.findall("[\\d.]+", captured.out)
    assert len(total_cost) == 1