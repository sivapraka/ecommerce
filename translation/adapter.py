from abc import ABC,abstractmethod
from .services import *


class TranslationAdapter(ABC):
    @abstractmethod
    def translate(self, request)->str:
        pass
    @abstractmethod
    def get_supported_languages(self)->list:
        pass


class MicrosoftTranslationAdapter(TranslationAdapter):
    def __init__(self):
        self.translate_api = MicrosoftTranslateApi()

    def translate(self, request:TranslationRequest)->str:
       return self.translate_api.translate(text=request.text, source_language=request.source_language, target_language=request.target_language)

    def get_supported_languages(self)->list:
        return self.translate_api.get_supported_languages()


class GoogleTranslationAdapter(TranslationAdapter):
    def __init__(self):
        self.google_translate_api = GoogleTranslateApi()

    def translate(self, request:TranslationRequest)->str:
        google_translate=GoogleTranslationRequest(text=request.text, source_language=request.source_language, target_language=request.target_language,confidence_threshold=None)
        return self.google_translate_api.convert(google_translate)

    def get_supported_languages(self)->list:
        return self.google_translate_api.get_languages()
