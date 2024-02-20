from modeltranslation.translator import TranslationOptions, translator

from utils.models import State


class StateTranslationOptions(TranslationOptions):
    fields = ('title', 'attr',)


translator.register(State, StateTranslationOptions)
