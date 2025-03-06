from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.timezone import now, timedelta

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"
    
    def is_expired(self):
        return now() > self.created_at + timedelta(minutes=10)  # Token expires in 10 minutes