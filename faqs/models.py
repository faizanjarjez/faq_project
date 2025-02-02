from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    LANGUAGES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ]

    question = models.TextField()
    answer = RichTextField()  # WYSIWYG Editor
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
    answer_hi = RichTextField(blank=True, null=True)  # Hindi translation
    answer_bn = RichTextField(blank=True, null=True)  # Bengali translation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def translate_text(self, text, dest_lang):
        """
        Translates text to the specified language using Google Translate.
        If translation fails, returns the original text.
        """
        translator = Translator()
        try:
            translation = translator.translate(text, dest=dest_lang)
            return translation.text
        except Exception as e:
            print(f"Translation failed: {e}")  # Log the error for debugging
            return text  # Fallback to original text if translation fails

    def save(self, *args, **kwargs):
        """
        Automatically translates question and answer during creation.
        """
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, 'bn')
        if not self.answer_hi:
            self.answer_hi = self.translate_text(self.answer, 'hi')
        if not self.answer_bn:
            self.answer_bn = self.translate_text(self.answer, 'bn')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question