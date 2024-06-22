from django.db import models
from accounts.views import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_receiver')
    content = models.TextField()
    language = models.CharField(max_length=2, choices=[('en', 'English'), ('hi', 'Hindi'), ('fr', 'French')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content[:20]}'
