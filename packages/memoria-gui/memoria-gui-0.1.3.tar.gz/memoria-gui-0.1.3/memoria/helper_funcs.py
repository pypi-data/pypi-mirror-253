import os
import sys
import webbrowser
from memoria.inputs import languages
import memoria
memoria_path = os.path.dirname(memoria.__file__)
sys.path.append(os.path.join(memoria_path, f"dictionaries/en_it"))

colors = ['#900C3F', '#C70039', '#FF5733', '#17BF14', '#FFC300']

def merge_dict(dict1, dict2):
    """Combine two dictionaries"""
    return {**dict1, **dict2}

def get_dictionary(book, chapter, card_type):
    """Load the selected dictionary"""
    if book == "nie_a0_a1pt5":
        if card_type == 'Vocabulary':
            from nie_a0_a1pt5 import vocab as chosen_dict
        elif card_type == 'Grammar':
            from nie_a0_a1pt5 import grammar as chosen_dict
        else:
            from nie_a0_a1pt5 import phrases as chosen_dict

    all_entries = {}
    if chapter == 'all':
        for cc in chosen_dict:
            all_entries = merge_dict(all_entries, chosen_dict[cc])

    else:
        # format strings
        chapter = chapter.replace(",", " ")   
        chapter = chapter.split()
        for cc in chapter:
            all_entries = merge_dict(all_entries, chosen_dict['ch' + cc])

    return all_entries


def translate(entry, source_dict, entry_language='English'):
    """Get the translation of 'entry' (either English to foreign language 
    or vice versa) from the dictionary 'source_dict'"""

    if entry_language == 'English':
        translation = source_dict[entry]
    else:
        translation = [i for i in source_dict if source_dict[i] == entry][0]
        
    return translation


def look_up_entry(entry, source_dict, reference_type, entry_language='Italian'):
    """Depending on 'reference_type', look up online the definition of a foreign 
    language word or phrase 'entry', its conjugation, or show the foreign language 
    form (as we provide in the `dictionaries` folder) on google translate to hear 
    it spoken."""

    if reference_type == 'define':
        if entry_language == 'Italian':
            link = f"https://www.wordreference.com/iten/{entry}"
    elif reference_type == 'conjugate': 
        if entry_language == 'Italian':
            link = f"https://sapere.virgilio.it/parole/coniuga-verbi/{entry}"
    else:
        link = "https://translate.google.com/?sl=it&tl=en&text="

        # for web address, must replace whitespace in 'entry'
        entry_no_spaces = entry.replace(" ", "%20")

        if entry_language == 'English':
            # don't want to call google translate on an English word/phrase, 
            # as its translation may differ from our stored one
            entry_no_spaces = translate(entry, source_dict, entry_language)
            
        link += f"{entry_no_spaces}%0A&op=translate"

    webbrowser.open(link, new=2)


def update_card(card, entry, source_dict, entry_language='English'):
    """For a button flashcard, update the card with the translation of 
    'entry' on first click; open a hyperlink on second click."""

    translation = translate(entry, source_dict, entry_language)

    if entry_language == 'English':
        english_entry = entry
        foreign_entry = translation
    else:
        foreign_entry = entry
        english_entry = translation

    if card['underline'] == 0:
        if english_entry.startswith(('to ', 'To ')):
            reference_type = 'conjugate'
        elif " " in entry:
            reference_type = 'hear'
        else:
            reference_type = 'define'

        if 'Italian' in languages:
            look_up_entry(foreign_entry, source_dict, reference_type, entry_language='Italian')

    else:
        new_text = f"{card['text']}\n\n{translation}"
        # update button color once it's clicked
        card.config(text=new_text, fg=colors[2], underline=0)
        