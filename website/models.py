from django.db import models

class Contact(models.Model):
    """
    Model to store contact form submissions from users.
    """

    name = models.CharField(max_length=255)  # User's full name
    email = models.EmailField()              # User's email address
    subject = models.CharField(max_length=255)  # Subject of the message
    message = models.TextField()             # Message content
    created_date = models.DateTimeField(auto_now_add=True)  # Timestamp when message was created
    updated_date = models.DateTimeField(auto_now=True)      # Timestamp when message was last updated

    class Meta:
        ordering = ['created_date']  # Default ordering by creation time (oldest first)

    def __str__(self):
        """
        String representation of the contact object.
        """
        return self.name
