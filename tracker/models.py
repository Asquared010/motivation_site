from django.db import models

# This model represents a single motivation entry submitted by a user.
# Each entry stores the user's name, their motivational message, and the time it was created.
class MotivationEntry(models.Model):
    
    # Stores the name of the user submitting the motivation entry
    name = models.CharField(max_length=100)
    
    # Stores the motivational message or goal written by the user
    message = models.TextField()
    
    # Automatically records the timestamp when the entry is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Returns a readable string representation of the model object
    # Useful for admin panel and debugging purposes
    def __str__(self):
        return f"{self.name} - {self.created_at}"