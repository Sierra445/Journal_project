from django.db import models

class JournalEntry(models.Model):
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date_created} - {self.text[:20]}"
