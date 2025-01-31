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
        """ Auto-translate and store translations in cache """
        translator = Translator()

        for lang_code, _ in self.LANGUAGES:
            if lang_code == "en":
                continue  # Skip English (default)

            field_name = f"question_{lang_code}"
            if not getattr(self, field_name):  # Translate only if empty
                translated_text = translator.translate(self.question, src='en', dest=lang_code).text
                setattr(self, field_name, translated_text)

                # Store in cache immediately
                cache_key = f"faq_{self.id}_{lang_code}"
                cache.set(cache_key, translated_text, timeout=86400)  # 24-hour cache

        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        """ Retrieve translation from cache or regenerate if needed """
        cache_key = f"faq_{self.id}_{lang}"
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation

        # Fetch from model fields
        translation = getattr(self, f"question_{lang}", self.question)

        # Store in cache if not already cached
        cache.set(cache_key, translation, timeout=86400)  # 24-hour cache
        return translation

    def __str__(self):
        return self.question
