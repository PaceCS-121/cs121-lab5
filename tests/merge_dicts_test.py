import merge_dicts

def test_merge_dicts_newfile():
    merge_dicts.main()
    f = open('data/combined_glossary.txt', 'r')
    txt = f.read()
    assert 'dictionary' in txt
    f.close()

def test_merge_dicts_2defs():
    merge_dicts.main()
    f = open('data/combined_glossary.txt', 'r')
    txt = f.read()
    assert 'A test for combining dictionaries.' in txt and 'Another test for combining dictionaries.' in txt
    f.close()