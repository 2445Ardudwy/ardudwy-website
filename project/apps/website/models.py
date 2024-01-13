import uuid

from django.db import models

def get_profile_image_filepath(self, filename):
    file_ext = filename.split('.')[-1:]
    new_filename = f"{uuid.uuid4()}.{file_ext}"
    return "staff/" + new_filename

class Contact(models.Model):
    PURPOSE_CHOICES = [
        ('1', 'Intrested in joining as a cadet'),
        ('2', 'Intrested in joining as a staff volunteer'),
        ('3', 'Intrested in joining as a committee volunteer'),
        ('4', 'Parent of a current cadet'),
        ('5', 'Financial support'),
        ('6', 'Report issue/bug on Website'),
        ('7', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=14, blank=True)
    purpose = models.CharField(max_length=1, choices=PURPOSE_CHOICES)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pk} - {self.first_name} {self.last_name}"


class StaffMembers(models.Model):
    POSITION = (
        ("0", "Officer Commanding"),
        ("1", "Adjutant"),
        ("2", "Training Officer"),
        ("3", "SNCO"),
        ("4", "Officer"),
        ("5", "Instructor"),
        ("6", "Padre"),
        ("7", "Chairperson"),
        ("8", "Treasurer"),
        ("9", "Secretary"),
        ("10", "Civilian Committee"),
    )

    RANKS = (
        ("Ms", "Ms"),
        ("Mr", "Mr"),
        ("Mx", "Mx"),
        ("Mrs", "Mrs"),
        ("Miss", "Miss"),
        ("Rev", "Rev"),
        ("CI", "CI"),
        ("Sgt", "Sgt"),
        ("FS", "FS"),
        ("WO", "WO"),
        ("Plt Off", "Plt Off"),
        ("Fg Off", "Fg Off"),
        ("Flt Lt", "Flt Lt"),
        ("Sqn Ldr", "Sqn Ldr"),
        ("Wg Cdr", "Wg Cdr"),
    )


    position = models.CharField(choices=POSITION, max_length=40, null=True, blank=True)
    rank = models.CharField(choices=RANKS, max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, null=True, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, default="staff/default.jpg", null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.rank} {self.first_name} {self.last_name}"