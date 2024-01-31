from collections import defaultdict as dd
import os

featureNameMap = {
    '': ''
}
class Mte6Translate:

    def __init__(self):
        self.mte6_dict_en_to_sl = dd()
        self.mte6_dict_sl_to_en = dd()
        self.mte6_dict_sl_features = dd()
        self.mte6_dict_en_features = dd()

        file_with_msd_translations = open(os.path.join(os.path.dirname(__file__), "resources/mte_6_dict_sl_en.tsv"), "r", encoding="UTF-8").readlines()

        # LIST OF FUNDAMENTAL MSDS USED FOR LEMMA FORMS
        # CAUTION - DO **NOT** CHANGE THE ORDER OF MSDs IN THE FILE UNDER ANY CIRCUMSTANCES.
        self.list_of_msds_for_lemmas = [line.strip("\n") for line in open(os.path.join(os.path.dirname(__file__), "resources/list_of_msds_for_lemmas.tsv"), "r", encoding="UTF-8").readlines()]

        for line in file_with_msd_translations[1:]:  # SKIP HEADERS
            msd_en,\
            features_en,\
            msd_sl,\
            features_sl,\
            types,\
            tokens,\
            examples = line.strip("\n").split("\t")

            self.mte6_dict_sl_to_en[msd_sl] = msd_en
            self.mte6_dict_en_to_sl[msd_en] = msd_sl
            self.mte6_dict_sl_features[msd_sl] = features_sl
            self.mte6_dict_en_features[msd_en] = features_en

    def get_msd_language(self, msd):
        """ FUNCTION - Get MSD language (returns 'sl' or 'en' or raises Error if MSD is invalid."""
        if msd in self.mte6_dict_sl_to_en:
            return 'sl'
        elif msd in self.mte6_dict_en_to_sl:
            return 'en'
        else:
            raise ValueError('Invalid MSD.')
    
    def msd_en_to_sl(self, msd_en):
        """FUNCTION - Translate MSD_EN to MSD_SL"""
        if msd_en in self.mte6_dict_en_to_sl:
            return self.mte6_dict_en_to_sl[msd_en]
        return msd_en

    def msd_sl_to_en(self, msd_sl):
        """FUNCTION - Translate MSD_SL to MSD_EN"""
        if msd_sl in self.mte6_dict_sl_to_en:
            return self.mte6_dict_sl_to_en[msd_sl]
        return msd_sl

    def get_sl_features(self, msd_sl):
        msd_sl = self.msd_en_to_sl(msd_sl)
        if msd_sl not in self.mte6_dict_sl_features:
            print(f'uknown msd: {msd_sl}')
            return None, {}
        
        parts = self.mte6_dict_sl_features[msd_sl].split(' ')
        type = parts.pop(0)
        features = { }
        for feature in parts:
            f = feature.split('=')
            if f[0] in featureNameMap:
                f[0] = featureNameMap[f[0]]
            features[f[0]] = f[1]

        return type, features
    
    def get_en_features(self, msd_en):
        msd_en = self.msd_sl_to_en(msd_en)
        if msd_en not in self.mte6_dict_en_features:
            print(f'uknown msd: {msd_en}')
            return None, {}
        
        parts = self.mte6_dict_en_features[msd_en].split(' ')
        type = parts.pop(0)
        features = { }
        for feature in parts:
            f = feature.split('=')
            if f[0] in featureNameMap:
                f[0] = featureNameMap[f[0]]
            features[f[0]] = f[1]

        return type, features

    def get_lemma_msd(self, msd_sl):
        msd_sl = self.msd_en_to_sl(msd_sl)

        lemma_msd = ""
        for item in self.list_of_msds_for_lemmas:
            if item in msd_sl:
                lemma_msd = item
                break

        return lemma_msd
