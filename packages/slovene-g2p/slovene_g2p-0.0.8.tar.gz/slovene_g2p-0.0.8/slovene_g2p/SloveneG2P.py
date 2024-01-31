import json
import os
from collections import defaultdict as dd

current_folder = os.path.dirname(__file__)

class SloveneG2P:

    def __init__(self):
        self.ipa_converter = SloveneG2PBase("ipa_symbol", "cjvt_ipa_detailed_representation", "phoneme_string")
        self.sampa_converter = SloveneG2PBase("sampa_symbol", "cjvt_sampa_detailed_representation", "phoneme_string")

    def ipa(self, word, msd, mpc):
        return self.ipa_converter.convert_to_phonetic_transcription(word, msd, mpc)

    def sampa(self, word, msd, mpc):
        return self.sampa_converter.convert_to_phonetic_transcription(word, msd, mpc)


class SloveneG2PBase:

    def __init__(self, representation_option, phoneme_set_option, output_option):
        self.phoneme_set_file_path = os.path.join(current_folder, "resources/SloveneG2P_phoneme_set.json")
        self.conversion_file_path = os.path.join(current_folder, "resources/table_of_obstruent_conversions.tsv")
        self.representation_option = representation_option
        self.phoneme_set_option = phoneme_set_option

        self.output_option = output_option
        self.phoneme_representation_dictionary = self.load_phoneme_representation_dictionary(self.phoneme_set_file_path, self.representation_option)
        self.phoneme_id_dictionary = self.load_phoneme_id_dictionary(self.phoneme_set_file_path, self.phoneme_set_option)
        self.id_phoneme_dictionary = {phoneme_id: phoneme for phoneme, phoneme_id in self.phoneme_id_dictionary.items()}
        self.voiced_to_voiceless_obstruent_conversions = self.get_dict_voiced_to_voiceless_obstruent_conversions(self.conversion_file_path)
        self.voiceless_to_voiced_obstruent_conversions = self.get_dict_voiceless_to_voiced_obstruent_conversions(self.conversion_file_path)

        # GET LISTS OF GRAPHEME SYMBOLS
        self.list_of_consonant_graphemes = self.get_consonant_graphemes()
        self.list_of_vowel_graphemes = self.get_vowel_graphemes()
        self.list_of_sonorant_graphemes = self.get_sonorant_graphemes()
        self.list_of_voiced_obstruent_graphemes = self.get_voiced_obstruent_graphemes()
        self.list_of_voiceless_obstruent_graphemes = self.get_voiceless_obstruent_graphemes()

        # GET LISTS OF PHONEME SYMBOLS
        self.vowel_phoneme_symbols = self.get_vowel_phoneme_symbols(phoneme_id_dictionary=self.id_phoneme_dictionary)
        self.sonorant_phoneme_symbols = self.get_sonorant_phoneme_symbols(phoneme_id_dictionary=self.id_phoneme_dictionary)
        self.voiced_obstruent_phoneme_symbols = self.get_voiced_obstruent_phoneme_symbols(phoneme_id_dictionary=self.id_phoneme_dictionary)
        self.voiceless_obstruent_phoneme_symbols = self.get_voiceless_obstruent_phoneme_symbols(phoneme_id_dictionary=self.id_phoneme_dictionary)

        # GET LIST OF SCHWA RULES
        self.set_schwa_combinations = set()
        file_with_schwa_rules = open(os.path.join(current_folder, "resources/schwa_rules.tsv"), "r", encoding="UTF-8").readlines()
        for line in file_with_schwa_rules:
            all_info = line.strip("\n").split("\t")
            morph_code = all_info[0]
            morph_example = all_info[1]
            relevant_msds = all_info[2]
            for relevant_msd in relevant_msds.split(", "):
                schwa_combination = f"{morph_code} ~ {relevant_msd}"
                self.set_schwa_combinations.add(schwa_combination)

    # RESOURCE FUNCTION - LIST OF VOWEL GRAPHEMES
    # This includes the accented 'r' grapheme
    def get_vowel_graphemes(self):
        return ['à', 'á', 'é', 'è', 'ê', 'ì', 'í', 'ó', 'ô', 'ò', 'ú', 'a', 'e', 'i', 'o', 'u', 'ŕ', 'ə']


    # RESOURCE FUNCTION - LIST OF SONORANT GRAPHEMES
    def get_sonorant_graphemes(self):
        return ['m', 'n', 'v', 'l', 'r', 'j']


    # RESOURCE FUNCTION - LIST OF VOICED OBSTRUENT GRAPHEMES
    def get_voiced_obstruent_graphemes(self):
        return ['b', 'd', 'z', 'ž', 'g']


    # RESOURCE FUNCTION - LIST OF VOICELESS OBSTRUENT GRAPHEMES
    def get_voiceless_obstruent_graphemes(self):
        return ['p', 't', 's', 'š', 'č', 'k', 'f', 'h', 'c']


    # RESOURCE FUNCTION - LIST OF ALL CONSONANT GRAPHEMES
    def get_consonant_graphemes(self):
        return ['m', 'n', 'v', 'l', 'r', 'j', 'b', 'd', 'z', 'ž', 'g', 'p', 't', 's', 'š', 'č', 'k', 'f', 'h', 'c']


    # RESOURCE FUNCTION - LOAD PHONEME REPRESENTATION DICTIONARY
    def load_phoneme_representation_dictionary(self, phoneme_set_file_path, representation_option):
        with open(phoneme_set_file_path, 'r', encoding='UTF-8') as file:
            json_reader = json.load(file)
        dict_phoneme_id_and_representation = dd()
        for phoneme_dictionary in json_reader:
            for phoneme_id in phoneme_dictionary:
                phoneme_representation = phoneme_dictionary[phoneme_id][representation_option]
                dict_phoneme_id_and_representation[phoneme_id] = phoneme_representation
        return dict_phoneme_id_and_representation


    # RESOURCE FUNCTION - LOAD PHONEME ID DICTIONARY
    def load_phoneme_id_dictionary(self, phoneme_set_file_path, phoneme_set_option):
        with open(phoneme_set_file_path, 'r', encoding="UTF-8") as file:
            json_reader = json.load(file)
        dict_phoneme_symbol_and_id = dd()
        for phoneme_dictionary in json_reader:
            for phoneme_id in phoneme_dictionary:
                phoneme_symbol = phoneme_dictionary[phoneme_id][phoneme_set_option]
                dict_phoneme_symbol_and_id[phoneme_symbol] = phoneme_id
        return dict_phoneme_symbol_and_id


    # RESOURCE FUNCTION - LIST OF VOWEL PHONEME SYMBOLS
    def get_vowel_phoneme_symbols(self, phoneme_id_dictionary):
        relevant_phoneme_ids = ['V_1.1', 'V_1.2', 'V_2.1', 'V_2.2', 'V_3.1', 'V_3.2', 'V_4',
                                'V_5', 'V_6.1', 'V_6.2', 'V_7.1', 'V_7.2', 'V_8', 'V_9.1', 'V_9.2',
                                'V_10.1', 'V_10.2']
        return [phoneme_id_dictionary[relevant_phoneme_id] for relevant_phoneme_id in relevant_phoneme_ids]


    # RESOURCE FUNCTION - LIST OF SONORANT PHONEME SYMBOLS
    def get_sonorant_phoneme_symbols(self, phoneme_id_dictionary):
        relevant_phoneme_ids = ['C_10', 'C_11', 'C_12.1', 'C_12.2', 'C_12.3',
                                'C_12.4', 'C_13.1', 'C_13.2', 'C_14.1',
                                'C_14.2', 'C_15.1', 'C_15.2', 'C_15.3']
        return [phoneme_id_dictionary[relevant_phoneme_id] for relevant_phoneme_id in relevant_phoneme_ids]


    # RESOURCE FUNCTION - LIST OF VOICED OBSTRUENT SYMBOLS
    def get_voiced_obstruent_phoneme_symbols(self, phoneme_id_dictionary):
        relevant_phoneme_ids = ['C_1.2.1', 'C_1.2.2', 'C_1.2.3', 'C_2.2.1',
                                'C_2.2.2', 'C_2.2.3', 'C_3.2', 'C_5.2', 'C_6.2',
                                'C_7.2', 'C_8.2', 'C_9.2']
        return [phoneme_id_dictionary[relevant_phoneme_id] for relevant_phoneme_id in relevant_phoneme_ids]


    # RESOURCE FUNCTION - GET LIST OF VOICELESS OBSTRUENT SYMBOLS
    def get_voiceless_obstruent_phoneme_symbols(self, phoneme_id_dictionary):
        relevant_phoneme_ids = ['C_1.1.1', 'C_1.1.2', 'C_1.1.3', 'C_2.1.1',
                                'C_2.1.2', 'C_2.1.3', 'C_3.1', 'C_4',
                                'C_5.1', 'C_6.1', 'C_7.1', 'C_8.1', 'C_9.1']
        return [phoneme_id_dictionary[relevant_phoneme_id] for relevant_phoneme_id in relevant_phoneme_ids]


    # RESOURCE FUNCTION - LOAD DICTIONARY OF VOICED-TO-VOICELESS-OBSTRUENT CONVERSIONS
    def get_dict_voiced_to_voiceless_obstruent_conversions(self, conversion_file_path):
        dict_voiced_to_voiceless_obstruent_conversions = dd()
        lines = open(conversion_file_path, "r", encoding="UTF-8").readlines()
        for line in lines[1:]:  # SKIP HEADERS
            conversion_type, original_phoneme, converted_phoneme = line.strip("\n").split("\t")[0:3]
            if conversion_type == 'voiced_to_voiceless_obstruent':
                dict_voiced_to_voiceless_obstruent_conversions[original_phoneme] = converted_phoneme
        return dict_voiced_to_voiceless_obstruent_conversions


    # RESOURCE FUNCTION - LOAD DICTIONARY OF VOICELESS-TO-VOICED-OBSTRUENT CONVERSIONS
    def get_dict_voiceless_to_voiced_obstruent_conversions(self, conversion_file_path):
        dict_voiceless_to_voiced_obstruent_conversions = dd()
        lines = open(conversion_file_path, "r", encoding="UTF-8").readlines()
        for line in lines[1:]:  # SKIP HEADERS
            conversion_type, original_phoneme, converted_phoneme = line.strip("\n").split("\t")[0:3]
            if conversion_type == 'voiceless_to_voiced_obstruent':
                dict_voiceless_to_voiced_obstruent_conversions[original_phoneme] = converted_phoneme
        return dict_voiceless_to_voiced_obstruent_conversions

    # HELPER FUNCTION - DETERMINE IF SYLLABLE IS ACCENTED OR NOT
    def is_syllable_accented(self, syllable):
        accented_graphemes = [u'ŕ', u'á', u'à', u'é', u'è', u'ê', u'í', u'ì', u'ó', u'ô', u'ò', u'ú', u'ù', u'ə̀']
        for grapheme in syllable:
            if grapheme in accented_graphemes:
                return True
        return False


    # HELPER FUNCTION - DETERMINE WHETHER A CHARACTER IS A VOWEL GRAPHEME OR A SYLLABIC R
    def is_vowel(self, list_of_characters_in_word, position, vowels):
        # Check if the character is a vowel
        if list_of_characters_in_word[position] in vowels:
            return True
        # Check if the character is a syllabic R
        if (list_of_characters_in_word[position] == u'r' or list_of_characters_in_word[position] == u'R') and (position - 1 < 0 or list_of_characters_in_word[position - 1] not in vowels) and (
                            position + 1 >= len(list_of_characters_in_word) or list_of_characters_in_word[position + 1] not in vowels):
            return True
        return False


    # HELPER FUNCTION - SPLIT CONSONANTS BETWEEN SYLLABLE 1 AND SYLLABLE 2
    def split_consonant_graphemes_between_syllables(self, consonants):
        # GET LISTS OF GRAPHEMES BY CATEGORY
        sonorant_graphemes = self.get_sonorant_graphemes()
        voiced_obstruent_graphemes = self.get_voiced_obstruent_graphemes()
        voiceless_obstruent_graphemes = self.get_voiceless_obstruent_graphemes()

        # If there are no consonant graphemes, return empty lists for syllable 1 and syllable 2
        if len(consonants) == 0:
            return [''], ['']

        # If there's only one consonant grapheme, attach it to syllable 2
        elif len(consonants) == 1:
            return [''], consonants

        # If there are more consonant graphemes, perform the following:
        else:
            split_options = []
            for i in range(len(consonants)-1):
                current_consonant_grapheme = consonants[i]
                next_consonant_grapheme = consonants[i+1]

                if current_consonant_grapheme in ['-', '_']:
                    split_options.append([i, -1])
                # If the consonants are the same (oDDaja)
                elif current_consonant_grapheme == next_consonant_grapheme:
                    split_options.append([i, 0])
                # Combination of sonorant + obstruent grapheme (objeM-Ka, soN-Da)
                elif current_consonant_grapheme in sonorant_graphemes:
                    if next_consonant_grapheme in voiced_obstruent_graphemes or next_consonant_grapheme in voiceless_obstruent_graphemes:
                        split_options.append([i, 2])
                    # TODO - ADD SONORANT + SONORANT (Narvik - narviški)
                    elif next_consonant_grapheme in sonorant_graphemes:
                        split_options.append([i, 2])
                # Combination of two voiced obstruents (oD-Ganjati) or a voiced and a voiceless obstruent grapheme (oD-Kleniti)
                elif current_consonant_grapheme in voiced_obstruent_graphemes:
                    if next_consonant_grapheme in voiced_obstruent_graphemes:
                        split_options.append([i, 1])
                    elif next_consonant_grapheme in voiceless_obstruent_graphemes:
                        split_options.append([i, 3])
                    # TODO - ADD VOICED OBSTRUENT + SONORANT
                    elif next_consonant_grapheme in sonorant_graphemes:
                        split_options.append([i, 2])
                # Combination of a voiceless and a voiced obstruent grapheme (glas-Ba)
                elif current_consonant_grapheme in voiceless_obstruent_graphemes:
                    if next_consonant_grapheme in voiced_obstruent_graphemes:
                        split_options.append([i, 4])
                    # TODO - Add TWO VOICELESS OBSTRUENTS? (poS-Tulat)
                    #elif next_consonant_grapheme in voiceless_obstruent_graphemes:
                    #    split_options.append([i, 2])
                    # TODO - Add VOICELESS OBSTRUENT + SONORANT
                    #elif next_consonant_grapheme in sonorant_graphemes:
                    #    split_options.append([i, 2])

            if split_options == []:
                return [''], consonants
            else:
                split = min(split_options, key=lambda x: x[1])
                return consonants[:split[0] + 1], consonants[split[0] + 1:]


    # HELPER FUNCTION - SPLIT WORD INTO SYLLABLES
    def create_syllables(self, word, vowels):
        list_of_characters_in_word = list(word)
        consonants = []
        syllables = []
        for i in range(len(list_of_characters_in_word)):
            if self.is_vowel(list_of_characters_in_word, i, vowels):
                if syllables == []:
                    consonants.append(list_of_characters_in_word[i])
                    syllables.append(''.join(consonants))
                else:
                    left_consonants, right_consonants = self.split_consonant_graphemes_between_syllables(list(''.join(consonants).lower()))  # TODO - EVERYTHING IS CONVERTED TO LOWER-CASE HERE
                    syllables[-1] += ''.join(left_consonants)
                    right_consonants.append(list_of_characters_in_word[i])
                    syllables.append(''.join(right_consonants))
                consonants = []
            else:
                consonants.append(list_of_characters_in_word[i])
        if len(syllables) < 1:
            return word
        syllables[-1] += ''.join(consonants)

        return syllables


    # MAIN FUNCTION - CONVERT ACCENTED WORD FORM TO PHONETIC TRANSCRIPTION
    def convert_to_phonetic_transcription(self, word, msd_sl, morphological_pattern_code):

        # GET DICTIONARIES
        phoneme_representation_dictionary = self.phoneme_representation_dictionary
        phoneme_id_dictionary = self.phoneme_id_dictionary
        voiced_to_voiceless_obstruent_conversions = self.voiced_to_voiceless_obstruent_conversions
        voiceless_to_voiced_obstruent_conversions = self.voiceless_to_voiced_obstruent_conversions

        # Get the primary stress mark for stressed syllables (e.g. "'" for IPA, '"' for SAMPA)
        primary_stress_mark = phoneme_representation_dictionary['S_2.1']

        # GET LISTS OF GRAPHEMES
        list_of_consonant_graphemes = self.list_of_consonant_graphemes
        list_of_vowel_graphemes = self.list_of_vowel_graphemes
        list_of_sonorant_graphemes = self.list_of_sonorant_graphemes
        list_of_voiced_obstruent_graphemes = self.list_of_voiced_obstruent_graphemes
        list_of_voiceless_obstruent_graphemes = self.list_of_voiceless_obstruent_graphemes

        # Convert all letters to lower-case
        word = word.lower()
        # Split the word into syllables
        syllables = self.create_syllables(word, list_of_vowel_graphemes)
        # First, assume that all characters in the word are unaccented
        accentuation_of_all_characters_in_word = [False] * len(word)
        # The "l" variable keeps track of word length
        l = 0
        # Go through all the syllables
        for syllable in syllables:
            # If the syllable is accented (i.e. it contains an accented character)
            if self.is_syllable_accented(syllable):
                for i in range(len(syllable)):
                    # Mark character as accented (by switching its value to True)
                    accentuation_of_all_characters_in_word[l + i] = True
            l += len(syllable)

        # Split the word into individual graphemes
        graphemes_in_word = list(word)

        # GENERATE A LIST TO CONTAIN PHONEMES (AND OTHER PHONETIC SYMBOLS)
        phonemes_in_word = []

        # COUNTER TO COUNT EXTRA SYMBOLS IN WORD
        """
        They are added to the phoneme list and affect the length of the word.
        If there are more accents (kultúrnovárstven), you need to take into account that when you add the first symbol,
        the phoneme list is lengthened, so the next accent is inserted in the wrong position
        unless you take previous accent symbols into account.
        """
        count_extra_symbols_in_word = 0

        # G2P - For each grapheme index in the word, convert the grapheme into the corresponding phoneme
        for i in range(len(graphemes_in_word)):
            current_grapheme = graphemes_in_word[i]
            try:
                previous_grapheme = graphemes_in_word[i-1]
            except:
                # If the current grapheme is at the beginning of the word, there is no previous grapheme.
                previous_grapheme = ''
            try:
                next_grapheme = graphemes_in_word[i+1]
            except:
                # If the current grapheme is the last grapheme in the word, there is no next grapheme.
                next_grapheme = ''

            # VOWEL GRAPHEMES
            # aeiouáàéèêíìóòôúùəə̀

            # A-GRAPHEMES
            if current_grapheme == 'a':
                phoneme = phoneme_representation_dictionary['V_1.1']  # phoneme = 'a'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'á':
                phoneme = phoneme_representation_dictionary['V_1.2']  # phoneme = 'a:'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'à':
                # TODO - make the "a" vs. "ʌ" distinction
                phoneme = phoneme_representation_dictionary['V_1.1']  # phoneme = 'a'
                phonemes_in_word.append(phoneme)

            # E-GRAPHEMES
            # NOTE: We don't include the schwah 'e' here for now. It's too unpredictable.
            # We'll see if we can correct some of it in postprocessing by taking POS into account,
            # e.g. adjectives (-en), nouns (-er, minister, december, pes).
            elif current_grapheme == 'e':
                phoneme = phoneme_representation_dictionary['V_2.1']  # phoneme = 'E'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'é':
                phoneme = phoneme_representation_dictionary['V_6.2']  # phoneme = 'e:'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'è':
                phoneme = phoneme_representation_dictionary['V_2.1']  # phoneme = 'E'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'ê':
                phoneme = phoneme_representation_dictionary['V_2.2']  # phoneme = 'E:'
                phonemes_in_word.append(phoneme)

            # I-GRAPHEMES
            elif current_grapheme == 'í':
                phoneme = phoneme_representation_dictionary['V_9.2']  # phoneme = 'i:'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'ì':
                phoneme = phoneme_representation_dictionary['V_9.1']  # phoneme = 'i'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'i':
                phoneme = phoneme_representation_dictionary['V_9.1']  # phoneme = 'i'
                phonemes_in_word.append(phoneme)

            # O-GRAPHEMES
            elif current_grapheme == 'o':
                phoneme = phoneme_representation_dictionary['V_3.1']  # phoneme = 'O'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'ó':
                phoneme = phoneme_representation_dictionary['V_7.2']  # phoneme = 'o:'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'ô':
                phoneme = phoneme_representation_dictionary['V_3.2']  # phoneme = 'O:'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'ò':
                phoneme = phoneme_representation_dictionary['V_3.1']  # phoneme = 'O'
                phonemes_in_word.append(phoneme)

            # U-GRAPHEMES
            elif current_grapheme == 'ú':
                phoneme = phoneme_representation_dictionary['V_10.2']  # phoneme = 'u:'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'ù':
                phoneme = phoneme_representation_dictionary['V_10.1']  # phoneme = 'u'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'u':
                phoneme = phoneme_representation_dictionary['V_10.1']  # phoneme = 'u'
                phonemes_in_word.append(phoneme)

            # SCHWA GRAPHEMES
            elif current_grapheme == 'ə̀':
                phoneme = phoneme_representation_dictionary['V_5']  # phoneme = 'ə'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'ə':
                phoneme = phoneme_representation_dictionary['V_5']  # phoneme = 'ə̀'
                phonemes_in_word.append(phoneme)

            # SONORANT GRAPHEMES
            # mlnrvj

            # M-GRAPHEMES
            elif current_grapheme == 'm':
                # 'm' followed by 'f' or 'v'
                if next_grapheme in ['f', 'v']:
                    phoneme = phoneme_representation_dictionary['C_14.2']  # phoneme = 'F'
                    phonemes_in_word.append(phoneme)
                # 'm' in all other positions
                else:
                    phoneme = phoneme_representation_dictionary['C_14.1']  # phoneme = 'm'
                    phonemes_in_word.append(phoneme)

            # N-GRAPHEMES
            elif current_grapheme == 'n':
                # if 'n' is followed by 'k', 'g', or 'h' (e.g. angel, Anhovo, banka)
                if next_grapheme in ['k', 'g', 'h']:
                    phoneme = phoneme_representation_dictionary['C_15.2']  # phoneme = 'N'
                    phonemes_in_word.append(phoneme)
                # if 'n' is followed by 'f' or 'v' (e.g. sinfonija, informacije, inverzija)
                elif next_grapheme in ['f', 'v']:
                    phoneme = phoneme_representation_dictionary['C_14.2']  # phoneme = 'F'
                    phonemes_in_word.append(phoneme)
                # TODO - mehčani n - elif word[letter_i] == 'n' and not word[next_letter_i] in vowels and letter_i == len(word) - 2:
                # TODO -    new_word[letter_i] = 'n\''
                # 'n' in all other positions
                else:
                    phoneme = phoneme_representation_dictionary['C_15.1']  # phoneme = 'n'
                    phonemes_in_word.append(phoneme)

            # J-GRAPHEMES
            elif current_grapheme == 'j':
                # if 'j' is the last grapheme and preceded by a vowel (e.g. lakaj, zakaj, poglej, Matej)
                if i == len(graphemes_in_word)-1 and previous_grapheme in list_of_vowel_graphemes:
                    phoneme = phoneme_representation_dictionary['V_8']  # phoneme = 'I'
                    phonemes_in_word.append(phoneme)
                # if 'j' is followed by a consonant (e.g. zajklja, balalajka)
                elif next_grapheme in list_of_consonant_graphemes:
                    phoneme = phoneme_representation_dictionary['V_8']  # phoneme = 'I'
                    phonemes_in_word.append(phoneme)
                # TODO - lj/nj (bolj, konjski, vonj)
                # 'j' in all other positions?
                else:
                    phoneme = phoneme_representation_dictionary['C_11']  # phoneme = 'j'
                    phonemes_in_word.append(phoneme)

            # L-GRAPHEMES
            # NOTE: "l" is problematic as it can be pronounced as "l" (polk, altistka, Malta) or "u" (polt, malta).
            # This is not systematic or rule-based, so it needs to be corrected (manually) in post-processing.
            # In this script, we naively treat it as "l".
            # TODO - can you always treat it as "l" if it's between two vowel graphemes? (polotok, uloviti, prelen ...)
            # TODO - If it's not between two vowels or at the beginning of the word, maybe return a warning in the end?
            elif current_grapheme == 'l':
                phoneme = phoneme_representation_dictionary['C_13.1']  # phoneme = 'l'
                phonemes_in_word.append(phoneme)
            # TODO - mehčani l - elif word[letter_i] == 'l' and not word[next_letter_i] in vowels and letter_i == len(word) - 2:
            # TODO -    new_word[letter_i] = 'l\''

            # REGULAR R vs. SYLLABIC R (schwah + R)
            # First check if the 'r' is accented
            # If it is, treat it as a combination of two phonemes: a schwah and "r"
            elif current_grapheme == 'ŕ':
                phoneme_1 = phoneme_representation_dictionary['V_5']  # phoneme_1 = '@'
                phoneme_2 = phoneme_representation_dictionary['C_10']  # phoneme_2 = 'r'
                phonemes_in_word.append(phoneme_1)
                phonemes_in_word.append(phoneme_2)
                accentuation_of_all_characters_in_word.insert(i, True)  # Add the accented schwah to accentuation list
            # If the 'r' grapheme is not accented, check the following:
            elif current_grapheme == 'r':
                # If it's not the first or last character in the word
                if not i == 0 and not i == len(graphemes_in_word)-1:
                    # check if it occurs between two consonants (e.g. alabastrn)
                    if previous_grapheme in list_of_consonant_graphemes and next_grapheme in list_of_consonant_graphemes:
                        phoneme_1 = phoneme_representation_dictionary['V_5']  # phoneme_1 = '@'
                        phoneme_2 = phoneme_representation_dictionary['C_10']  # phoneme_2 = 'r'
                        phonemes_in_word.append(phoneme_1)
                        phonemes_in_word.append(phoneme_2)
                        accentuation_of_all_characters_in_word.insert(i, False) # Add the unaccented schwah to accentuation list
                    else:
                        phoneme = phoneme_representation_dictionary['C_10']  # phoneme = 'r'
                        phonemes_in_word.append(phoneme)
                # If it's at the beginning of a word followed by consonant grapheme (e.g. rdeč)
                elif i == 0 and next_grapheme in list_of_consonant_graphemes:
                    phoneme_1 = phoneme_representation_dictionary['V_5']  # phoneme_1 = '@'
                    phoneme_2 = phoneme_representation_dictionary['C_10']  # phoneme_2 = 'r'
                    phonemes_in_word.append(phoneme_1)
                    phonemes_in_word.append(phoneme_2)
                    accentuation_of_all_characters_in_word.insert(i, False) # Add the unaccented schwah to accentuation list
                # If it's at the end of a word and preceded by a consonant (e.g. žanr)
                elif i == len(graphemes_in_word)-1 and previous_grapheme in list_of_consonant_graphemes:
                    phoneme_1 = phoneme_representation_dictionary['V_5']  # phoneme_1 = '@'
                    phoneme_2 = phoneme_representation_dictionary['C_10']  # phoneme_2 = 'r'
                    phonemes_in_word.append(phoneme_1)
                    phonemes_in_word.append(phoneme_2)
                    accentuation_of_all_characters_in_word.insert(i, False) # Add the unaccented schwah to accentuation list
                # 'r' in all other positions
                else:
                    phoneme = phoneme_representation_dictionary['C_10']  # phoneme = 'r'
                    phonemes_in_word.append(phoneme)

            # 'V' AND ITS VARIANTS
            # TODO - 'v' should be further processed to determine variants (w, u) - important for accent symbol insertion!
            elif current_grapheme == 'v':
                # 'v' at the beginning of a word
                if i == 0:
                    # if the 'v' is followed by a vowel (e.g. voda, voditelj)
                    if next_grapheme in list_of_vowel_graphemes:
                        phoneme = phoneme_representation_dictionary['C_12.1']  # phoneme = 'v'
                        phonemes_in_word.append(phoneme)
                    # if the 'v' is followed by a sonorant (e.g. vnesti, vmesen, vrata, vlak)
                    elif next_grapheme in list_of_sonorant_graphemes:
                        phoneme = phoneme_representation_dictionary['C_12.2']  # phoneme = 'w'
                        phonemes_in_word.append(phoneme)
                        accentuation_of_all_characters_in_word.insert(i, False)  # Add the unaccented semivowel to accentuation list
                    # if the 'v' is followed by a voiced obstruent (e.g. vbrizg, vbod)
                    elif next_grapheme in list_of_voiced_obstruent_graphemes:
                        phoneme = phoneme_representation_dictionary['C_12.2']  # phoneme = 'w'
                        phonemes_in_word.append(phoneme)
                        accentuation_of_all_characters_in_word.insert(i, False)  # Add the unaccented semivowel to accentuation list
                    # if the 'v' is followed by a voiceless obstruent (e.g. vtis, vpenjati)
                    elif next_grapheme in list_of_voiceless_obstruent_graphemes:
                        phoneme = phoneme_representation_dictionary['C_12.3']  # phoneme = 'W'
                        phonemes_in_word.append(phoneme)
                        accentuation_of_all_characters_in_word.insert(i, False)  # Add the unaccented semivowel to accentuation list
                    else:
                        phoneme = phoneme_representation_dictionary['C_12.1']  # phoneme = 'v'
                        phonemes_in_word.append(phoneme)
                        # TODO - vrhgorski! should be v@rGg"O:rski, not w@rGg"O:rski

                # if the 'v' is at the end of the word
                elif i == len(graphemes_in_word)-1:
                    # if the 'v' is preceded by a vowel (e.g. ponovitev, molitev, ulov)
                    if previous_grapheme in list_of_vowel_graphemes:
                        phoneme = phoneme_representation_dictionary['C_12.4']  # phoneme = 'U'
                        phonemes_in_word.append(phoneme)
                        # NOTE: We're not adding it to the accentuation list here as it doesn't act as an independent vowel phoneme and doesn't form a syllable
                    # if the 'v' is preceded by a 'r' (e.g. črv, brv, obrv)
                    elif previous_grapheme in ["r", "ŕ"]:
                        phoneme = phoneme_representation_dictionary['C_12.4']  # phoneme = 'U'
                        phonemes_in_word.append(phoneme)
                    else:
                        phoneme = phoneme_representation_dictionary['C_12.1']  # phoneme = 'v'
                        phonemes_in_word.append(phoneme)

                # 'v' not at the end and not at the beginning
                elif not i == 0 and not i == len(graphemes_in_word)-1:
                    # if the 'v' is followed by a consonant (e.g. klovn, Miklavž, terapevt, Vovk, detektivk)
                    if next_grapheme in list_of_consonant_graphemes:
                        phoneme = phoneme_representation_dictionary['C_12.4']  # phoneme = 'U'
                        phonemes_in_word.append(phoneme)
                        # NOTE: We're not adding it to the accentuation list here as it doesn't act as an independent vowel phoneme and doesn't form a syllable
                    # 'v' in all other remaining positions
                    else:
                        phoneme = phoneme_representation_dictionary['C_12.1']  # phoneme = 'v'
                        phonemes_in_word.append(phoneme)

            # VOICED OBSTRUENT GRAPHEMES
            # bdgzž
            # B-GRAPHEMES
            elif current_grapheme == 'b':
                # if 'b' is followed by 'm' (e.g. obmejen)
                if next_grapheme == 'm':
                    phoneme = phoneme_representation_dictionary['C_1.2.2']  # phoneme = 'b_n'
                    phonemes_in_word.append(phoneme)
                # if 'b' is followed by 'f' or 'v' (e.g. obveza)
                elif next_grapheme in ['f', 'v']:
                    phoneme = phoneme_representation_dictionary['C_1.2.3']  # phoneme = 'b_f'
                    phonemes_in_word.append(phoneme)
                # 'b' in all other remaining positions
                else:
                    phoneme = phoneme_representation_dictionary['C_1.2.1']  # phoneme = 'b'
                    phonemes_in_word.append(phoneme)

            # D-GRAPHEMES
            elif current_grapheme == 'd':
                # if 'd' is followed by 'l' (e.g. skodla, dlan)
                if next_grapheme == 'l':
                    phoneme = phoneme_representation_dictionary['C_2.2.2']  # phoneme = 'd_l'
                    phonemes_in_word.append(phoneme)
                # if 'd' is followed by 'n' (e.g. dno, dneven, pridnega)
                elif next_grapheme == 'n':
                    phoneme = phoneme_representation_dictionary['C_2.2.3']  # phoneme = 'd_n'
                    phonemes_in_word.append(phoneme)
                # 'd' in all other positions
                else:
                    phoneme = phoneme_representation_dictionary['C_2.2.1']  # phoneme = 'd'
                    phonemes_in_word.append(phoneme)

            elif current_grapheme == 'g':
                phoneme = phoneme_representation_dictionary['C_3.2']  # phoneme = 'g'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'z':
                phoneme = phoneme_representation_dictionary['C_5.2']  # phoneme = 'z'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'ž':
                phoneme = phoneme_representation_dictionary['C_6.2']  # phoneme = 'Z'
                phonemes_in_word.append(phoneme)

            # VOICELESS OBSTRUENT GRAPHEMES
            # tshškfcpč
            # T-GRAPHEMES
            elif current_grapheme == 't':
                # if 't' is followed by an 'l' (e.g. tla, kotlovnica)
                if next_grapheme == 'l':
                    phoneme = phoneme_representation_dictionary['C_2.1.2']  # phoneme = 't_l'
                    phonemes_in_word.append(phoneme)
                # if 't' is followed by an 'n' (e.g. zakotnega)
                elif next_grapheme == 'n':
                    phoneme = phoneme_representation_dictionary['C_2.1.3']  # phoneme = 't_n'
                    phonemes_in_word.append(phoneme)
                # 't' in all other remaining positions
                else:
                    phoneme = phoneme_representation_dictionary['C_2.1.1']  # phoneme = 't'
                    phonemes_in_word.append(phoneme)

            elif current_grapheme == 's':
                phoneme = phoneme_representation_dictionary['C_5.1']  # phoneme = 's'
                phonemes_in_word.append(phoneme)

            # H-GRAPHEMES
            elif current_grapheme == 'h':
                # if 'h' is followed by 'g' (usually only occurs between words, but hypothetically: vrhgorski)
                if next_grapheme == 'g':
                    phoneme = phoneme_representation_dictionary['C_7.2']  # phoneme = 'G'
                    phonemes_in_word.append(phoneme)
                # 'h' in all other remaining positions
                else:
                    phoneme = phoneme_representation_dictionary['C_7.1']  # phoneme = 'x'
                    phonemes_in_word.append(phoneme)

            # Š-, K-, F- and C-GRAPHEMES
            elif current_grapheme == 'š':
                phoneme = phoneme_representation_dictionary['C_6.1']  # phoneme = 'S'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'k':
                phoneme = phoneme_representation_dictionary['C_3.1']  # phoneme = 'k'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'f':
                phoneme = phoneme_representation_dictionary['C_4']  # phoneme = 'f'
                phonemes_in_word.append(phoneme)
            elif current_grapheme == 'c':
                phoneme = phoneme_representation_dictionary['C_8.1']  # phoneme = 'ts'
                phonemes_in_word.append(phoneme)

            # P-GRAPHEMES
            elif current_grapheme == 'p':
                # if 'p' is followed by 'm'
                if next_grapheme == 'm':
                    phoneme = phoneme_representation_dictionary['C_1.1.2']  # phoneme = 'p_n'
                    phonemes_in_word.append(phoneme)
                # if 'p' is followed by 'f' or 'v'
                elif next_grapheme in ['f', 'v']:
                    phoneme = phoneme_representation_dictionary['C_1.1.3']  # phoneme = 'p_f'
                    phonemes_in_word.append(phoneme)
                # 'p' in all other positions
                else:
                    phoneme = phoneme_representation_dictionary['C_1.1.1']  # phoneme = 'p'
                    phonemes_in_word.append(phoneme)

            # Č-GRAPHEME
            elif current_grapheme == 'č':
                phoneme = phoneme_representation_dictionary['C_9.1']  # phoneme = 'tS'
                phonemes_in_word.append(phoneme)

            # Ć-GRAPHEME
            elif current_grapheme == 'ć':
                phoneme = phoneme_representation_dictionary['C_9.1']  # phoneme = 'tS'
                phonemes_in_word.append(phoneme)

            # Đ-GRAPHEME
            elif current_grapheme == 'đ':
                phoneme = phoneme_representation_dictionary['C_9.2']  # phoneme = 'dZ'
                phonemes_in_word.append(phoneme)

            else:
                # TODO - POTENTIALLY ADD POTENTIALLY SOME ADDITIONAL GRAPHEME-PHONEME CONVERSIONS?
                phoneme = current_grapheme
                phonemes_in_word.append(phoneme)

        # COUNT ACCENT SYMBOLS NOT PRESENT IN THE GRAPHEME AND PHONEME LIST
        """
        They are added to the phoneme list and affect the length of the word
        If there are more accents (kultúrnovárstven), you need to take into account that when you add the first symbol,
        the word is lengthened, so the next accent is inserted in the wrong position unless you take previous accent symbols into account.
        """
        # IF THE FIRST CHARACTER IN THE WORD IS ACCENTED, ADD PRIMARY ACCENT SYMBOL BEFORE IT
        if accentuation_of_all_characters_in_word[0]:
            # Add the primary accent symbol as a separate entry in the list of phonemes at the beginning
            phonemes_in_word.insert(0, primary_stress_mark)
            # Track the number of already added accent symbols
            count_extra_symbols_in_word += 1

        # IF ANY OF THE OTHER CHARACTERS IN THE WORD ARE ACCENTED, ADD PRIMARY ACCENT SYMBOL BEFORE THEM
        for i in range(1, len(accentuation_of_all_characters_in_word)):
            # If the previous character in the word is not accented and the current character is accented
            if not accentuation_of_all_characters_in_word[i-1] and accentuation_of_all_characters_in_word[i]:
                # Add the primary accent symbol in the middle of the phoneme list
                phonemes_in_word.insert(i+count_extra_symbols_in_word, primary_stress_mark)
                # Track the number of already added accent symbols
                count_extra_symbols_in_word += 1



        # TAKE THE INITIAL LIST OF PHONEMES IN THE WORD AND APPLY PRONUNCIATION RULES (ASSIMILATION etc.)

        # GET PHONEME LISTS (REQUIRED TO CHECK WHICH PHONEMES FALL UNDER WHICH CATEGORY)
        # We can't use grapheme lists at this point anymore, so we need to generate lists of phonemes
        # from the dictionaries selected at the beginning of the function.

        # Reverse phoneme_id_dictionary so you can search phonemes by ID
        id_phoneme_dictionary = self.id_phoneme_dictionary

        # GET LISTS OF PHONEME SYMBOLS
        vowel_phoneme_symbols = self.vowel_phoneme_symbols
        sonorant_phoneme_symbols = self.sonorant_phoneme_symbols
        voiced_obstruent_phoneme_symbols = self.voiced_obstruent_phoneme_symbols
        voiceless_obstruent_phoneme_symbols = self.voiceless_obstruent_phoneme_symbols

        # If the word ends with a voiced obstruent, it becomes voiceless
        if phonemes_in_word[-1] in voiced_obstruent_phoneme_symbols:
            final_voiced_obstruent_id = phoneme_id_dictionary[phonemes_in_word[-1]]
            converted_phoneme_id = voiced_to_voiceless_obstruent_conversions[final_voiced_obstruent_id]
            converted_phoneme = id_phoneme_dictionary[converted_phoneme_id]
            phonemes_in_word[-1] = converted_phoneme

        # Check all obstruents from the end to the beginning of the word;
        # if they are voiced obstruents and preceded by voiceless obstruents, the voiceless obstruents become voiced (e.g. prerokba, glasba, označba);
        # conversely, if they are voiceless obstruents and preceded by voiced obstruents, the voiced obstruents become voiceless (e.g. sladkor, gladko, gibkost, obsoditi)
        for i in reversed(range(0, len(phonemes_in_word))):  #
            if not i == 0:  # Skip i=0 because there is no left phoneme in that case (there is no -1 phoneme)
                right_phoneme = phonemes_in_word[i]
                left_phoneme = phonemes_in_word[i-1]
                if right_phoneme in voiceless_obstruent_phoneme_symbols:
                    if left_phoneme in voiced_obstruent_phoneme_symbols:
                        left_phoneme_id = phoneme_id_dictionary[left_phoneme]  # Get ID of the left phoneme
                        converted_phoneme_id = voiced_to_voiceless_obstruent_conversions[left_phoneme_id]  # Get converted phoneme ID
                        converted_phoneme = id_phoneme_dictionary[converted_phoneme_id]  # Get converted phoneme
                        phonemes_in_word[i-1] = converted_phoneme  # Replace the original phoneme with the converted phoneme
                    elif left_phoneme == primary_stress_mark and not i == 1:  # Skip i=1 because there is no -1 phoneme
                        previous_left_phoneme = phonemes_in_word[i-2]
                        if previous_left_phoneme in voiced_obstruent_phoneme_symbols:
                            previous_left_phoneme_id = phoneme_id_dictionary[previous_left_phoneme]
                            converted_phoneme_id = voiced_to_voiceless_obstruent_conversions[previous_left_phoneme_id]  # Get converted phoneme ID
                            converted_phoneme = id_phoneme_dictionary[converted_phoneme_id]  # Get converted phoneme
                            phonemes_in_word[i-2] = converted_phoneme  # Replace the original phoneme with the converted phoneme
                elif right_phoneme in voiced_obstruent_phoneme_symbols:
                    if left_phoneme in voiceless_obstruent_phoneme_symbols:
                        left_phoneme_id = phoneme_id_dictionary[left_phoneme]  # Get ID of the left phoneme
                        converted_phoneme_id = voiceless_to_voiced_obstruent_conversions[left_phoneme_id]  # Get converted phoneme ID
                        converted_phoneme = id_phoneme_dictionary[converted_phoneme_id]  # Get converted phoneme
                        phonemes_in_word[i-1] = converted_phoneme  # Replace the original phoneme with the converted phoneme
                    elif left_phoneme == primary_stress_mark and not i == 1:  # Skip i=1 because there is no -1 phoneme
                        previous_left_phoneme = phonemes_in_word[i-2]
                        if previous_left_phoneme in voiceless_obstruent_phoneme_symbols:
                            previous_left_phoneme_id = phoneme_id_dictionary[previous_left_phoneme]
                            converted_phoneme_id = voiceless_to_voiced_obstruent_conversions[previous_left_phoneme_id]  # Get converted phoneme ID
                            converted_phoneme = id_phoneme_dictionary[converted_phoneme_id]  # Get converted phoneme
                            phonemes_in_word[i-2] = converted_phoneme  # Replace the original phoneme with the converted phoneme

        # Phonemes consisting of two graphemes / Assimilate two sounds into one
        # Check combinations of two phonemes from the beginning to the end of the word
        for i in range(0, len(phonemes_in_word)-1):  # Skip the last phoneme iteration (there is no phoneme after the last)
            first_phoneme = phonemes_in_word[i]
            second_phoneme = phonemes_in_word[i+1]

            # If the first phoneme is 'd'
            if first_phoneme == phoneme_representation_dictionary['C_2.2.1']:  # phoneme = 'd'
                # d + z = dz (odziv)
                if second_phoneme == phoneme_representation_dictionary['C_5.2']:  # phoneme = 'z'
                    phonemes_in_word[i+1] = phoneme_representation_dictionary['C_8.2']  # the second phoneme becomes 'dz'
                    phonemes_in_word[i] = '' # the first phoneme becomes empty
                # d + ž = dZ (odžeti, džungla)
                elif second_phoneme == phoneme_representation_dictionary['C_6.2']:  # phoneme = 'Z'
                    phonemes_in_word[i + 1] = phoneme_representation_dictionary['C_9.2']  # the second phoneme becomes 'dZ'
                    phonemes_in_word[i] = ''  # the first phoneme becomes empty
                # If the primary stress mark is between the 'd' and the next phoneme
                elif second_phoneme == primary_stress_mark and not i == len(phonemes_in_word)-1:
                    # d'z = 'dz
                    third_phoneme = phonemes_in_word[i+2]
                    if third_phoneme == phoneme_representation_dictionary['C_5.2']:  # phoneme = 'z'
                        phonemes_in_word[i+2] = phoneme_representation_dictionary['C_8.2']  # the third phoneme becomes 'dz'
                        phonemes_in_word[i] = ''  # the first phoneme becomes empty
                    # d'Z = 'dZ
                    elif third_phoneme == phoneme_representation_dictionary['C_6.2']:  # phoneme = 'Z'
                        phonemes_in_word[i+2] = phoneme_representation_dictionary['C_9.2']  # the third phoneme becomes 'dz'
                        phonemes_in_word[i] = ''  # the first phoneme becomes empty

            # If the first phoneme is 't'
            elif first_phoneme == phoneme_representation_dictionary['C_2.1.1']:  # phoneme = 't'
                second_phoneme = phonemes_in_word[i+1]
                # d + s = t + s = c, ts (predsednik)
                if second_phoneme == phoneme_representation_dictionary['C_5.1']:  # phoneme = 's'
                    phonemes_in_word[i+1] = phoneme_representation_dictionary['C_8.1']  # the second phoneme becomes 'ts'
                    phonemes_in_word[i] = ''  # the first phoneme becomes empty
                # d + Š = t + S = č, tS (predšolski)
                elif second_phoneme == phoneme_representation_dictionary['C_6.1']:  # phoneme = 'S'
                    phonemes_in_word[i+1] = phoneme_representation_dictionary['C_9.1']  # the second phoneme becomes 'tS'
                    phonemes_in_word[i] = ''  # the first phoneme becomes empty
                # If the primary stress mark is between the 't' and the next phoneme
                elif second_phoneme == primary_stress_mark and not i == len(phonemes_in_word)-1:
                    # t's = 'ts
                    third_phoneme = phonemes_in_word[i+2]
                    if third_phoneme == phoneme_representation_dictionary['C_5.1']:  # phoneme = 's'
                        phonemes_in_word[i+2] = phoneme_representation_dictionary['C_8.1']  # the third phoneme becomes 'ts'
                        phonemes_in_word[i] = ''  # the first phoneme becomes empty
                    # t'S = 'tS
                    elif third_phoneme == phoneme_representation_dictionary['C_6.1']:  # phoneme = 'S'
                        phonemes_in_word[i+2] = phoneme_representation_dictionary['C_9.1']  # the third phoneme becomes 'tS'
                        phonemes_in_word[i] = ''  # the first phoneme becomes empty

            # l + j = l' (at end of word; Ljubelj, datelj), l + I = l' (svaljkati, poljski)
            elif first_phoneme == phoneme_representation_dictionary['C_13.1']:  # phoneme = 'l'
                second_phoneme = phonemes_in_word[i+1]
                if second_phoneme == phoneme_representation_dictionary['C_11'] and i+1 == len(phonemes_in_word)-1:  # last phoneme = 'j'
                    phonemes_in_word[i] = phoneme_representation_dictionary['C_13.2']  # the first phoneme become "l'"
                    phonemes_in_word[i+1] = ''  # the second (last) phoneme becomes empty
                elif second_phoneme == phoneme_representation_dictionary['V_8']:  # last phoneme is 'I'
                    phonemes_in_word[i] = phoneme_representation_dictionary['C_13.2']  # the first phoneme become "l'"
                    phonemes_in_word[i + 1] = ''  # the second (last) phoneme becomes empty

            # n + j = n' (vonj, konj, konjski)
            elif first_phoneme == phoneme_representation_dictionary['C_15.1']:  # phoneme = 'n'
                second_phoneme = phonemes_in_word[i+1]
                if second_phoneme == phoneme_representation_dictionary['C_11'] and i+1 == len(phonemes_in_word)-1:  # last phoneme = 'j'
                    phonemes_in_word[i] = phoneme_representation_dictionary['C_15.3']  # the first phoneme become "l'"
                    phonemes_in_word[i+1] = ''  # the second (last) phoneme becomes empty
                elif second_phoneme == phoneme_representation_dictionary['V_8']:  # last phoneme is 'I'
                    phonemes_in_word[i] = phoneme_representation_dictionary['C_15.3']  # the first phoneme become "l'"
                    phonemes_in_word[i+1] = ''  # the second (last) phoneme becomes empty

        # REMOVE EMPTY PHONEMES FROM LIST
        if '' in phonemes_in_word:
            for i in range(0, phonemes_in_word.count('')):
                phonemes_in_word.remove('')

        # Other transformations
        for i in range(0, len(phonemes_in_word)-1):
            first_phoneme = phonemes_in_word[i]
            # Final approximant omission / post-i pre-consonant approximant omission
            # ópij  "o: p i
            # biologíj  b i j O l O "g i:
            # razbíj  r a z "b i:
            # informacijski, azijski, Avstrijci, Azijke
            # i + j, i + I = i (informacijski, opij, razbij)
            if first_phoneme in [phoneme_representation_dictionary['V_9.1'], phoneme_representation_dictionary['V_9.2']]:  # phoneme = 'i' / 'i:'
                second_phoneme = phonemes_in_word[i+1]
                if second_phoneme == phoneme_representation_dictionary['V_8']:  # phoneme = 'I'
                    phonemes_in_word[i+1] = ""  # the 'I' becomes an empty phoneme

            # Sibilant assimilation
            # When /s/, /z/ and /ts/ are followed by /ʃ/, /ʒ/,/dʒ/ or /tʃ/,
            # they are pronounced as /ʃ/, /ʒ/ or /tʃ/
            #(e.g. sčasoma [ˈʃtʃaːsɔma], iz žepa [iˈʒɛːpa].) razžaliti
            # s + S = S + S; s + tS = S + tS (razčesniti)
            elif first_phoneme == phoneme_representation_dictionary['C_5.1']:  # phoneme = 's'
                second_phoneme = phonemes_in_word[i+1]
                if second_phoneme in [phoneme_representation_dictionary['C_6.1'], phoneme_representation_dictionary['C_9.1']]:  # phoneme = 'S' or 'tS'
                    phonemes_in_word[i] = phoneme_representation_dictionary['C_6.1']  # the first phoneme becomes 'S'
                elif second_phoneme == primary_stress_mark and not i==len(phonemes_in_word)-1:
                    third_phoneme = phonemes_in_word[i+2]
                    if third_phoneme in [phoneme_representation_dictionary['C_6.1'], phoneme_representation_dictionary['C_9.1']]:  # phoneme = 'S' or 'tS'
                        phonemes_in_word[i] = phoneme_representation_dictionary['C_6.1']  # the first phoneme becomes 'S'
            # z + Z = Z + Z; z + dZ = Z + dZ
            elif first_phoneme == phoneme_representation_dictionary['C_5.2']:  # phoneme = 'z'
                second_phoneme = phonemes_in_word[i+1]
                if second_phoneme in [phoneme_representation_dictionary['C_6.2'], phoneme_representation_dictionary['C_9.2']]:  # phoneme = 'Z' or 'dZ'
                    phonemes_in_word[i] = phoneme_representation_dictionary['C_6.2']  # the first phoneme becomes 'Z'
                elif second_phoneme == primary_stress_mark and not i==len(phonemes_in_word)-1:
                    third_phoneme = phonemes_in_word[i+2]
                    if third_phoneme in [phoneme_representation_dictionary['C_6.2'], phoneme_representation_dictionary['C_9.2']]:  # phoneme = 'Z' or 'dZ'
                        phonemes_in_word[i] = phoneme_representation_dictionary['C_6.2']  # the first phoneme becomes 'Z'

        # REMOVE EMPTY PHONEMES FROM LIST
        if '' in phonemes_in_word:
            for i in range(0, phonemes_in_word.count('')):
                phonemes_in_word.remove('')

        # Long consonants and double vowels
        # TODO - TREAT VOWELS AND CONSONANTS DIFFERENTLY? VOWELS CAN BE TREATED AS EXTRA-LONG (e.g. a::)
        # oddája  o "d: a: j a
        # izsévati  i "s: e: v a t i
        # podtíp  p O "t: i: p
        # razsôdb  r a "s: O: t p
        # pooblaščenec -> p O:: b l a S "tS E n @ ts
        # naapriliti -> n a:: p "r i l i t i
        for i in range(0, len(phonemes_in_word)-1):
            first_phoneme = phonemes_in_word[i]
            second_phoneme = phonemes_in_word[i+1]
            if first_phoneme == second_phoneme:
                phonemes_in_word[i+1] = '{}{}'.format(phonemes_in_word[i+1], phoneme_representation_dictionary['S_1'])  # Add symbol for vowel length
                phonemes_in_word[i] = ""  # the first phoneme becomes empty
            elif second_phoneme == primary_stress_mark:
                try:  # IF THE WORD IS NOT LONG ENOUGH, IT PRODUCES AN ERROR (BUG WITH vs\o, vzšl\o)
                    third_phoneme = phonemes_in_word[i+2]
                    if first_phoneme == third_phoneme:
                        phonemes_in_word[i+2] = '{}{}'.format(phonemes_in_word[i+2], phoneme_representation_dictionary['S_1'])
                        phonemes_in_word[i] = ""  # the first phoneme becomes empty
                except:
                    continue

        # Inter-vowel approximant addition
        # materiál  m a t E r i "j a: l
        # biológ  b i j O "l o: k

        # APPLY END-L RULES
        # If a word ends with L and has a specific MSD_SL, the end "l" is pronounced as "U"
        if phonemes_in_word[-1] == phoneme_representation_dictionary['C_13.1'] and msd_sl in ["Ggdd-em", "Ggnd-em", "Ggvd-em", "Gp-d-em", "Pdnmein", "Pdnmetn"]:
            phonemes_in_word[-1] = phoneme_representation_dictionary['C_12.4']  # Change "l" to "u̯"

        # APPLY SCHWA RULES
        # In some words with specific MSD_SLs, the last vowel in a word is not "ɛ", but rather "ə"
        # e.g. agraren - agrarən
        schwa_combination_to_check = f"{morphological_pattern_code} ~ {msd_sl}"
        if schwa_combination_to_check in self.set_schwa_combinations:
            for index, phoneme in reversed(list(enumerate(phonemes_in_word))):
                if phoneme == phoneme_representation_dictionary['V_2.1']:  # "ɛ":
                    phonemes_in_word[index] = phoneme_representation_dictionary['V_5']  # "ə"
                    break

        # print(phonemes_in_word)
        phonetic_transcription = ''.join(phonemes_in_word)
        if self.output_option == 'phoneme_list':
            return phonemes_in_word
        elif self.output_option == 'phoneme_string':
            return phonetic_transcription
        else:
            print("ERROR: Invalid input option. Please select between 'phoneme_list' and 'phoneme_string'.")
