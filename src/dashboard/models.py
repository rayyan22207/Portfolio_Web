from django.db import models

class Inquiry(models.Model):
    WORK = 'work'
    INDUSTRY_QUESTION = 'industry_question'
    FEEDBACK = 'feedback'

    INQUIRY_TYPES = [
        (WORK, 'Work Inquiry'),
        (INDUSTRY_QUESTION, 'Industry Question'),
        (FEEDBACK, 'Project Feedback'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_TYPES, default=WORK)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_inquiry_type_display()}"

