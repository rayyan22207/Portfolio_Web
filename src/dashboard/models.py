from django.db import models

class Inquiry(models.Model):
    WORK = 'work'
    INDUSTRY_QUESTION = 'industry_question'
    COLLABORATION = 'collaboration'
    CONSULTATION = 'consultation'
    OTHER = 'other'

    INQUIRY_TYPES = [
        (WORK, 'Work Inquiry'),
        (INDUSTRY_QUESTION, 'Industry Question'),
        (COLLABORATION, 'Collaboration Request'),
        (CONSULTATION, '1-on-1 Consultation'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    inquiry_type = models.CharField(max_length=30, choices=INQUIRY_TYPES, default=WORK)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_inquiry_type_display()}"

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    what_they_liked = models.TextField("What did you like?")
    what_they_disliked = models.TextField("What could be better?", blank=True, null=True)
    honest_review = models.TextField("Your honest thoughts")
    
    STARS = [(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)]
    rating = models.IntegerField(choices=STARS)

    allow_publishing = models.BooleanField(
        default=False,
        help_text="Are you okay with this being published on the site?"
    )

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} ({self.rating}★)"


class Project(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    technologies = models.CharField(max_length=500, null=True, blank=True)  # Store as comma-separated values
    github_url = models.URLField(null=True, blank=True)
    live_demo_url = models.URLField(null=True, blank=True)
    # image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title if self.title else "Untitled Project"