
import tempfile

from gensim.corpora import Dictionary



def convert_gs_dictionary_to_string(dictionary: Dictionary) -> str:
    """Convert corpora to string"""
    with tempfile.NamedTemporaryFile() as fp:
        dictionary.save_as_text(fp.file.name) # , sort_by_word=True) # save to text
        return fp.read().decode()

def convert_string_to_gs_dictionary(s: str) -> Dictionary:
    """Convert string to corpora"""
    with tempfile.NamedTemporaryFile() as fp:
        fp.write(s.encode('utf-8'))
        return Dictionary.load_from_text(fp.file.name)