import pickle
from collections import defaultdict as dd
import json
import os

class VectorizeLemma:

    def __init__(self):

        self.dict_msd = {'verbs': 'G',
                        'masculine_nouns': ('Som', 'Slm'),
                        'feminine_nouns': ('Soz', 'Slz'),
                        'neuter_nouns': ('Sos', 'Sls'),
                        'adjectives': 'P',
                        'adverbs': 'R',
                        'abbreviations': 'O',
                        'interjections': 'M',
                        'conjunctions': 'V',
                        'prepositions': 'D',
                        'numeral': 'K',
                        'pronouns': 'Z',
                        'particle': 'L',
                        'residual': 'N',
                        'punctuation': 'U'}

        # LOAD LISTS OF ENDING PARTS
        self.ending_parts_for_verbs = [line.strip("\n") for line in open(os.path.join(os.path.dirname(__file__),"resources/ending_parts_for_verbs.tsv"), "r", encoding="UTF-8").readlines()]
        self.ending_parts_for_masculine_nouns = [line.strip("\n") for line in open(os.path.join(os.path.dirname(__file__),"resources/ending_parts_for_masculine_nouns.tsv"), "r", encoding="UTF-8").readlines()]
        self.ending_parts_for_feminine_nouns = [line.strip("\n") for line in open(os.path.join(os.path.dirname(__file__),"resources/ending_parts_for_feminine_nouns.tsv"), "r", encoding="UTF-8").readlines()]
        self.ending_parts_for_neuter_nouns = [line.strip("\n") for line in open(os.path.join(os.path.dirname(__file__),"resources/ending_parts_for_neuter_nouns.tsv"), "r", encoding="UTF-8").readlines()]
        self.ending_parts_for_adjectives = [line.strip("\n") for line in open(os.path.join(os.path.dirname(__file__),"resources/ending_parts_for_adjectives.tsv"), "r", encoding="UTF-8").readlines()]
        self.ending_parts_for_adverbs = [line.strip("\n") for line in open(os.path.join(os.path.dirname(__file__),"resources/ending_parts_for_adverbs.tsv"), "r", encoding="UTF-8").readlines()]

    # ADDITIONAL FEATURE EXTRACTORS
    def lemma_endswith_cczsj(self, lemma):
        """FEATURE USED WITH MASCULINE NOUNS - Check if lemma ends with CČŽŠJ"""
        return 1.0 if lemma.lower().endswith(("c", "č", "ž", "š", "j", "ć", "đ")) else 0.0

    def lemma_endswith_r(self, lemma):
        """FEATURE USED WITH MASCULINE NOUNS - Check if lemma ends with R"""
        return 1.0 if lemma.lower().endswith("r") else 0.0

    def lemma_endswith_y(self, lemma):
        """FEATURE USED WITH MASCULINE NOUNS - Check if lemma ends with Y"""
        return 1.0 if lemma.lower().endswith("y") else 0.0

    def lemma_endswith_vowel(self, lemma):
        """FEATURE USED WITH MASCULINE NOUNS - Check if lemma ends with a vowel (a, e, i, o, u)"""
        return 1.0 if lemma.lower().endswith(("a", "e", "i", "o", "u")) else 0.0

    def lemma_endswith_o(self, lemma):
        """FEATURE USED WITH MASCULINE NOUNS - Check if lemma ends with O"""
        return 1.0 if lemma.lower().endswith("o") else 0.0

    def lemma_caps_ratio(self, lemma):
        """FEATURE USED WITH MASCULINE NOUNS - Check how many characters are uppercase to distinguish between acronynms and non-acronyms"""
        return float(len([character for character in list(lemma) if character.isupper()])/len(list(lemma)))

    def lemma_endswith_e(self, lemma):
        """FEATURE USED WITH FEMININE NOUNS - Check if lemma ends with E"""
        return 1.0 if lemma.lower().endswith("e") else 0.0

    def lemma_endswith_consonant_and_ra(self, lemma):
        """FEATURE USED WITH FEMININE NOUNS - Check if lemma ends with consonant + ra and not vowel + ra"""
        # magistra, Aleksandra
        if lemma.lower().endswith(("ara", "era", "ora", "ira", "ura")):
            return 0.0
        elif lemma.lower().endswith("ra"):
            return 1.0
        else:
            return 0.0

    def lemma_endswith_consonant_and_la(self, lemma):
        """FEATURE USED WITH FEMININE NOUNS - Check if lemma ends with consonant + la and not vowel + la"""
        # bakla, megla
        if lemma.lower().endswith(("ala", "ela", "ola", "ila", "ula")):
            return 0.0
        elif lemma.lower().endswith("la"):
            return 1.0
        else:
            return 0.0

    def lemma_endswith_consonant_and_ma(self, lemma):
        """FEATURE USED WITH FEMININE NOUNS - Check if lemma ends with consonant + ma and not vowel + ma"""
        # sintagma
        if lemma.lower().endswith(("ama", "ema", "oma", "ima", "uma")):
            return 0.0
        elif lemma.lower().endswith("ma"):
            return 1.0
        else:
            return 0.0

    def lemma_endswith_consonant_and_na(self, lemma):
        """FEATURE USED WITH FEMININE NOUNS - Check if lemma ends with consonant + na and not vowel + na"""
        # akna
        if lemma.lower().endswith(("ana", "ena", "ona", "ina", "una")):
            return 0.0
        elif lemma.lower().endswith("na"):
            return 1.0
        else:
            return 0.0

    def lemma_endswith_consonant_and_va(self, lemma):
        """FEATURE USED WITH FEMININE NOUNS - Check if lemma ends with consonant + va and not vowel + va"""
        # spužva
        if lemma.lower().endswith(("ava", "eva", "ova", "iva", "uva")):
            return 0.0
        elif lemma.lower().endswith("va"):
            return 1.0
        else:
            return 0.0

    def lemma_endswith_kma_gma_zma_hma(self, lemma):
        """FEATURE USED WITH FEMININE NOUNS - Check if lemma ends with -kma, -gma, -zma, -hma"""
        # tekma, magma, sintagma, plazma, drahma
        return 1.0 if lemma.lower().endswith(("hma", "gma", "zma", "kma")) else 0.0

    # EXTRACTOR OF FEATURES BASED ON A LIST OF ENDING PARTS
    def extract_vector_of_all_ending_parts(self, lemma, list_of_ending_parts):
        """Extracts a vector of ending part features based on a list of ending parts"""
        list_of_ending_part_features = []
        for ending_part in list_of_ending_parts:
            if lemma.endswith(ending_part):
                list_of_ending_part_features.append(1.0)
            else:
                list_of_ending_part_features.append(0.0)
        return list_of_ending_part_features

    # MAIN VECTOR GENERATOR
    def generate_vector(self, lemma, msd):
        """Generates a vector using ending part features and potential additional features"""

        # GENERATE VECTOR FOR VERBS
        if msd.startswith(self.dict_msd['verbs']):
            return self.extract_vector_of_all_ending_parts(lemma, self.ending_parts_for_verbs)

        # GENERATE VECTOR FOR MASCULINE NOUNS
        elif msd.startswith(self.dict_msd['masculine_nouns']):

            # ADD ENDING PART FEATURES FIRST
            feature_array = self.extract_vector_of_all_ending_parts(lemma, self.ending_parts_for_masculine_nouns)

            # ADD ADDITIONAL FEATURES PERTAINING TO MASCULINE NOUNS
            for value in [self.lemma_endswith_cczsj(lemma),
                          self.lemma_endswith_r(lemma),
                          self.lemma_endswith_y(lemma),
                          self.lemma_endswith_vowel(lemma),
                          self.lemma_endswith_o(lemma),
                          self.lemma_caps_ratio(lemma)]:
                feature_array.append(value)
            return feature_array

        # GENERATE VECTOR FOR FEMININE NOUNS
        elif msd.startswith(self.dict_msd['feminine_nouns']):

            # ADD ENDING PART FEATURES FIRST
            feature_array = self.extract_vector_of_all_ending_parts(lemma, self.ending_parts_for_feminine_nouns)

            # ADD ADDITIONAL FEATURES PERTAINING TO FEMININE NOUNS
            for value in [self.lemma_endswith_e(lemma),
                          self.lemma_endswith_consonant_and_ra(lemma),
                          self.lemma_endswith_consonant_and_la(lemma),
                          self.lemma_endswith_consonant_and_ma(lemma),
                          self.lemma_endswith_consonant_and_na(lemma),
                          self.lemma_endswith_consonant_and_va(lemma),
                          self.lemma_endswith_kma_gma_zma_hma(lemma)]:
                feature_array.append(value)

            return feature_array

        # GENERATE VECTOR FOR NEUTER NOUNS
        elif msd.startswith(self.dict_msd['neuter_nouns']):
            return self.extract_vector_of_all_ending_parts(lemma, self.ending_parts_for_neuter_nouns)

        # GENERATE VECTOR FOR ADJECTIVES
        elif msd.startswith(self.dict_msd['adjectives']):
            return self.extract_vector_of_all_ending_parts(lemma, self.ending_parts_for_adjectives)

        # GENERATE VECTOR FOR ADVERBS
        elif msd.startswith(self.dict_msd['adverbs']):
            return self.extract_vector_of_all_ending_parts(lemma, self.ending_parts_for_adverbs)

        else:
            pass
            # OTHER PARTS OF SPEECH


class PatternPredictor:

    def __init__(self):

        # INSTANTIATE LEMMA VECTORIZER
        self.lemma_vectorizer = VectorizeLemma()

        # LOAD PREDICTION MODELS
        self.logreg_verbs = pickle.load(open(os.path.join(os.path.dirname(__file__),"models/logreg_verbs.sav"), "rb"))
        self.logreg_adverbs = pickle.load(open(os.path.join(os.path.dirname(__file__),"models/logreg_adverbs.sav"), "rb"))
        self.logreg_adjectives = pickle.load(open(os.path.join(os.path.dirname(__file__),"models/logreg_adjectives.sav"), "rb"))
        self.logreg_masculine_nouns = pickle.load(open(os.path.join(os.path.dirname(__file__),"models/logreg_masculine-nouns.sav"), "rb"))
        self.logreg_feminine_nouns = pickle.load(open(os.path.join(os.path.dirname(__file__),"models/logreg_feminine-nouns.sav"), "rb"))
        self.logreg_neuter_nouns = pickle.load(open(os.path.join(os.path.dirname(__file__),"models/logreg_neuter-nouns.sav"), "rb"))

        # DICTIONARY OF FINEGRAINED POS FOR PATTERN KEY FEATURE
        self.dict_msd = {'verbs': 'G',
                             'masculine_nouns': ('Som', 'Slm'),
                             'feminine_nouns': ('Soz', 'Slz'),
                             'neuter_nouns': ('Sos', 'Sls'),
                             'adjectives': 'P',
                             'adverbs': 'R',
                             'abbreviations': 'O',
                             'interjections': 'M',
                             'conjunctions': 'V',
                             'prepositions': 'D',
                             'numerals': 'K',
                             'pronouns': 'Z',
                             'particles': 'L',
                             'residual': 'N',
                             'punctuation': 'U'}

    def get_defining_feature_for_patterns(self, msd):
        """FUNCTION - Gets the necessary feature from MSD to help determine the final morphological pattern"""

        # VERBS - RETURN ASPECT (PERFECTIVE, PROGRESSIVE OR BIASPECTUAL)
        if msd.startswith(self.dict_msd['verbs']):
            return msd[2]
        # NEUTER/FEMININE/MASCULINE NOUNS - RETURN TYPE (COMMON OR PROPER)
        elif msd.startswith(self.dict_msd['masculine_nouns']) or msd.startswith(self.dict_msd['feminine_nouns']) or msd.startswith(self.dict_msd['neuter_nouns']):
            return msd[1]
        # ADJECTIVES - RETURN TYPE (GENERAL, POSSESSIVE OR PARTICIPLE)
        elif msd.startswith(self.dict_msd['adjectives']):
            return msd[1]
        # ADVERBS - RETURN TYPE (GENERAL OR PARTICIPLE)
        elif msd.startswith(self.dict_msd['adverbs']):
            return msd[1]
        else:
            # OTHER PARTS OF SPEECH
            return None

    def predict_morphological_pattern(self, lemma, msd):
        self.vectorized_lemma = self.lemma_vectorizer.generate_vector(lemma=lemma, msd=msd)
        self.pattern_feature = self.get_defining_feature_for_patterns(msd=msd)

        # SELECT MODEL BASED ON MSD
        # VERBS
        if msd.startswith(self.dict_msd['verbs']):
            self.morphological_pattern_classifier = self.logreg_verbs

        # MASCULINE NOUNS
        elif msd.startswith(self.dict_msd['masculine_nouns']):
            self.morphological_pattern_classifier = self.logreg_masculine_nouns

        # FEMININE NOUNS
        elif msd.startswith(self.dict_msd['feminine_nouns']):
            self.morphological_pattern_classifier = self.logreg_feminine_nouns

        # NEUTER NOUNS
        elif msd.startswith(self.dict_msd['neuter_nouns']):
            self.morphological_pattern_classifier = self.logreg_neuter_nouns

        # ADVERBS
        elif msd.startswith(self.dict_msd['adverbs']):
            self.morphological_pattern_classifier = self.logreg_adverbs

        # ADJECTIVES
        elif msd.startswith(self.dict_msd['adjectives']):
            self.morphological_pattern_classifier = self.logreg_adjectives

        # OTHER PARTS OF SPEECH REQUIRE NO CLASSIFIER
        # NUMERALS
        # Numeral patterns are not predicted; they are rule-based.
        elif msd.startswith(self.dict_msd['numerals']):
            if msd == "Kag":
                return "Kag.1"
            elif msd == "Kav":
                return "Kav.1"
            elif msd == "Krg":
                return "Krg.1"
            elif msd == "Krv":
                return "Krv.1"
            elif msd.startswith("Kb"):
                if lemma.lower().endswith(("ji", "či")):
                    return "Kb.2"
                elif lemma.lower().endswith("i"):
                    return "Kb.1"
                elif lemma.lower().endswith("er"):
                    return "Kb.3"
                elif lemma.lower().endswith(("ojen", "eren")):
                    return "Kb.4"
                elif lemma.lower().endswith("et"):
                    return "Kb.5"
                elif lemma.lower().endswith("sto"):
                    return "Kb.6"
                elif lemma.lower().endswith("drug"):
                    return "Kb.7"
                elif lemma.lower().endswith("dva"):
                    return "Kb.8"
                elif lemma.lower().endswith("oj"):
                    return "Kb.9"
                elif lemma.lower().endswith("em"):
                    return "Kb.10"
                elif lemma.lower().endswith("štirje"):
                    return "Kb.11"
                elif lemma.lower().endswith("trije"):
                    return "Kb.12"
                elif lemma.lower().endswith("več"):
                    return "Kb.13"
                elif lemma.lower().endswith("en"):
                    return "Kb.14"
                else:
                    # If nothing of the above applies, it's most likely an error in POS-tagging.
                    # Return Kb.1 as default.
                    return "Kb.1"

        # OTHER POS
        elif msd.startswith(self.dict_msd['abbreviations']):
            return f"{self.dict_msd['abbreviations']}.1"
        elif msd.startswith(self.dict_msd['interjections']):
            return f"{self.dict_msd['interjections']}.1"
        elif msd.startswith(self.dict_msd['conjunctions']):
            return f"{msd}.1"  # Entire conjunction MSDs are included in their pattern codes
        elif msd.startswith(self.dict_msd['prepositions']):
            return f"{msd}.1"  # Entire preposition MSDs are included in their pattern codes
        elif msd.startswith(self.dict_msd['particles']):
            return f"{self.dict_msd['particles']}.1"
        elif msd.startswith(self.dict_msd['residual']):
            return f"{msd}.1"  # Entire residual MSDs are included in their pattern codes
        elif msd.startswith(self.dict_msd['punctuation']):
            return f"{self.dict_msd['punctuation']}.1"
        else:
            # The only remaining POS is pronoun; when tagged with classla(lexicon=True),
            # NOTHING SHOULD be tagged as a pronoun except actual pronouns.
            return None

        self.predicted_pattern_code = self.morphological_pattern_classifier.predict([self.vectorized_lemma])

        # GENERATE FULL PATTERN CODE
        # FOR VERBS/NOUNS/ADJECTIVES, THE CODE CONSISTS OF THE PREDICTED PATTERN CODE + PATTERN FEATURE
        if msd.startswith((self.dict_msd['verbs'], self.dict_msd['adjectives'])) \
                or msd.startswith(self.dict_msd['masculine_nouns'])\
                or msd.startswith(self.dict_msd['feminine_nouns'])\
                or msd.startswith(self.dict_msd['neuter_nouns']):
            self.full_pattern_code = f"{self.predicted_pattern_code[0]}.{self.pattern_feature}"

            return self.full_pattern_code

        # FOR ADVERBS, THE PATTERN CODES NEED TO TAKE THE PATTERN FEATURE INTO ACCOUNT A BIT DIFFERENTLY
        elif msd.startswith(self.dict_msd['adverbs']):
            # GENERAL ADVERBS CAN ONLY BE CLASSIFIED AS R1.1 - THIS IS TO CORRECT POTENTIAL COMMON MISCLASSIFICATIONS
            if self.pattern_feature in ['s', 'g'] and self.predicted_pattern_code[0] == "R2.1":
                return "R1.1"
            # PARTICIPIAL ADVERBS CAN ONLY BE CLASSIFIED AS R2.1 - THIS IS TO CORRECT POTENTIAL COMMON MISCLASSIFICATIONS
            elif self.pattern_feature in ['d', 'r'] and self.predicted_pattern_code[0] == "R1.1":
                return "R2.1"
            else:
                return self.predicted_pattern_code[0]

        # FOR ALL OTHER PARTS OF SPEECH, RETURN None for now
        else:
            return None


class FormGenerator:

    def __init__(self):

        # POPULATE DICTIONARY WITH MORPHOLOGICAL PATTERNS
        self.dict_morphological_patterns = dd()
        self.file_with_patterns_for_form_generation = open(os.path.join(os.path.dirname(__file__), "resources/patterns_for_generation.tsv"), "r", encoding="UTF-8").readlines()
        for line in self.file_with_patterns_for_form_generation:
            self.pattern_code, self.pattern = line.strip("\n").split("\t")[0:2]
            self.dict_morphological_patterns[self.pattern_code] = self.pattern

        # LIST OF FUNDAMENTAL MSDS USED FOR LEMMA FORMS
        # CAUTION - DO **NOT** CHANGE THE ORDER OF MSDs IN THE FILE UNDER ANY CIRCUMSTANCES.
        self.list_of_msds_for_lemmas = [line.strip("\n") for line in open(os.path.join(os.path.dirname(__file__), "resources/list_of_msds_for_lemmas.tsv"), "r", encoding="UTF-8").readlines()]



    def generate_forms(self, pattern_code, lemma):
        """FUNCTION - GENERATE FORMS FROM PATTERN, LEMMA AND POS"""
        # CHECK IF THE PATTERN CODE IS AVAILABLE IN THE PATTERN DICTIONARY, OTHERWISE
        if pattern_code in self.dict_morphological_patterns:
            self.pattern = self.dict_morphological_patterns[pattern_code]
        else:
            print(f"invalid MPC: {pattern_code}")
            return {}

        # POPULATE PATTERN DICTIONARY
        self.pattern_dictionary = dd(list)
        for element in self.pattern.split(", "):
            self.tag, self.ending_part = element.split(": ")
            for ending in self.ending_part.split("|"):
                self.pattern_dictionary[self.tag].append(ending.strip("~").replace("Ø", ""))

        # DETERMINE THE BASIC MSD OF THE LEMMA (i.e. THE FIRST AVAILABLE ON THE PRIORITY LIST)
        for item in self.list_of_msds_for_lemmas:
            if item in self.pattern_dictionary:
                self.basic_msd = item
                break

        # GET IMMUTABLE PART OF THE LEMMA
        ending_part_for_basic_msd = self.pattern_dictionary[self.basic_msd][0]
        if not ending_part_for_basic_msd == "":
            self.immutable_part = lemma[:(len(lemma) - len(ending_part_for_basic_msd))]
        else:
            self.immutable_part = lemma

        # POPULATE DICTIONARY WITH FORMS
        self.dict_with_forms = dd(list)
        for key in self.pattern_dictionary:
            for ending_part in self.pattern_dictionary[key]:
                self.dict_with_forms[key].append(f"{self.immutable_part}{ending_part}")

        return self.dict_with_forms


class PatternCodeRemapper:

    def __init__(self):
        # POPULATE DICTIONARY WITH PATTERN REMAPPINGS
        """
        The problem is that the models predict simplified pattern codes. For instance, 'Ss2.2.l' is actually 'Ss2.2.l-množina',
        but for the models' sake, we treat it as Ss2.2.l in order to conform to the mechanism that the model predicts the first
        part of the pattern code (i.e. 'Ss2.2'), while the second part is taken from the key feature of the MSD (e.g. 'l').
        There is no way of knowing whether "-množina", "-ednina" etc. should be added to the pattern code, so the only way to
        correct these is through rule-based remapping (included in the 'pattern-remapping.tsv' file).
        This pattern remapping dictionary converts the simplified pattern codes into their actual codes.
        """
        self.dict_pattern_remapping = dd()
        for line in open(os.path.join(os.path.dirname(__file__), "resources/pattern_remapping.tsv"), "r", encoding="UTF-8").readlines()[1:]:  # SKIP HEADER
            predicted_pattern, actual_remapped_pattern = line.strip("\n").split("\t")
            self.dict_pattern_remapping[predicted_pattern] = actual_remapped_pattern

    def remap_pattern_code(self, pattern_code):
        """FUNCTION - REMAP SIMPLIFIED PATTERN CODES TO ACTUAL PATTERN CODES"""
        return self.dict_pattern_remapping[
            pattern_code] if pattern_code in self.dict_pattern_remapping else pattern_code

class SloveneFormGenerator:
    def __init__(self):
                
        self.pattern_predictor = PatternPredictor()
        self.form_generator = FormGenerator()
        self.pattern_code_remapper = PatternCodeRemapper()

    def generate(self, lema_in, msd, pattern_code = None):

        # Get pattern code from input word or calculate it if it is not given
        if pattern_code is None:
            pattern_code = self.pattern_predictor.predict_morphological_pattern(lemma=lema_in, msd=msd)

        # Generate forms based on pattern code
        pattern_dictionary = self.form_generator.generate_forms(pattern_code=pattern_code, lemma=lema_in)
        remapped_pattern_code = self.pattern_code_remapper.remap_pattern_code(pattern_code=pattern_code)

        # Create response
        response = []
        for msd, form_list in pattern_dictionary.items():
            forms = []
            for form in form_list:
                orthographies = []
                orthographies.append({ "text": form, "morphologyPatterns": remapped_pattern_code })
                # Add more orthographies here if required

                # Add orthographies to current form
                forms.append({ 'orthographies': orthographies })

            # Add current form to msd entry
            response.append({'msd': msd, 'forms': forms})

        # Return whole response
        return response