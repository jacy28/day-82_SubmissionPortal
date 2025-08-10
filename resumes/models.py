from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_pdf(value):
    max_size=2*1024*1024
    if value.size>max_size:
        raise ValidationError("File size must be under 2MB.")
    if not value.name.endswith('.pdf'):
        raise ValidationError("Only .pdf files are allowed.")
    
class Resume(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    position=models.CharField(max_length=100)
    resume=models.FileField(upload_to='resumes', validators=[validate_pdf])

    def __str__(self):
        return f"{self.name} - {self.position}"