"""This module runs tests to confirm the code is working correctly."""

from memoria.inputs import books, card_types, languages
from memoria.helper_funcs import get_dictionary, look_up_entry, translate
from memoria.gui import selection_gui, flashcard_gui

book = 'nie_a0_a1pt5'
chapter = '1'
card_type = 'Vocabulary'
card_language=['English', 'Italian']

def test_get_dict():
    """Test that we can fetch a dictionary"""
    get_dictionary(book, chapter, card_type)

def test_translate():
    """Test that we can translate to/from Italian"""
    source_dict = get_dictionary(book, chapter, card_type)
    translate('to be', source_dict, entry_language='English')
    translate('essere', source_dict, entry_language='Italian')

def test_look_up_entry():
    """Test that we can look up an entry in a dictionary"""
    source_dict = get_dictionary(book, chapter, card_type)
    look_up_entry('essere', source_dict, 'define', 'Italian')

def test_generate_selection_gui():
    """Test that the selection GUI launches"""
    selection_gui(books, card_types, languages)

def test_generate_flashcard_gui():
    """Test that the flaschard GUI launches"""
    flashcard_gui(book='New Italian Espresso: A0 - A1.5', 
                  chapter=chapter, 
                  card_type=card_type, 
                  card_language=card_language[0])