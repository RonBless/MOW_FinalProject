

class GlobalSettings:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if GlobalSettings.__instance is None:
            GlobalSettings()
        return GlobalSettings.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if GlobalSettings.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GlobalSettings.__instance = self
            self.training_url = 'https://gist.githubusercontent.com/RonBless/4ae08ab67ba24a25c6c3ada7b4e770dc/raw/' \
                                '9ac17ebc37d5aa812861ee99d47c3586ee544687/Training_Ver2_300_Movies'
            self.model_name = 'NN_Model_ver2'
            self.test_url = 'https://gist.githubusercontent.com/RonBless/4ae08ab67ba24a25c6c3ada7b4e770dc/' \
                            'raw/58bf11b1bf96ab7749b26af2b9eb7c5c7189269a/Test'

