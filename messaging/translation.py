from modeltranslation.translator import register, TranslationOptions
from .models import Message

@register(Message)
class MessageTranslationOptions(TranslationOptions):
    fields = ('content',)
