from django.db import models

class HarassmentReport(models.Model):
    HARASSMENT_TYPE_CHOICES = [
    ('verbal', 'Verbal'),
    ('physical', 'Physical'),
    ('cyber', 'Cyber'),
    ('sexual', 'Sexual'),
    ('emotional', 'Emotional or Psychological'),
    ('stalking', 'Stalking'),
    ('workplace', 'Workplace'),
    ('public', 'Public'),
    ('intimidation', 'Intimidation'),
    ('discrimination', 'Discrimination'),
    ('invasive', 'Invasive Questions'),
    ('gossip', 'Gossip and Rumors'),
    ('other', 'Other'),
]
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    harassment_type = models.CharField(max_length=100, choices=HARASSMENT_TYPE_CHOICES)
    REPORTER_TYPE_CHOICES = [
        ('victim', 'Victim'),
        ('eyewitness', 'Eyewitness'),
    ]
    reported_by = models.CharField(max_length=50, choices=REPORTER_TYPE_CHOICES, default='victim')
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=True, blank=True)  # New field for latitude
    longitude = models.FloatField(null=True, blank=True)  # New field for longitude

    def __str__(self):
        return f"{self.location} - {self.harassment_type}"
