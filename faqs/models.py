from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

class FAQ(models.Model):
    LANGUAGES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ]

    question = models.TextField()
    answer = RichTextField()
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')

    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        translator = Translator()

        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        
        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        cache_key = f"faq_{self.id}_{lang}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data

        translation = getattr(self, f"question_{lang}", self.question)
        cache.set(cache_key, translation, timeout=3600)
        return translation

    def __str__(self):
        return self.question

