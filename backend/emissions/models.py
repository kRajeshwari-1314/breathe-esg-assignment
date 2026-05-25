from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DataSource(models.Model):
    SOURCE_CHOICES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'UTILITY'),
        ('TRAVEL', 'TRAVEL'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    source_type = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    file_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_type} - {self.file_name}"


class EmissionRecord(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
    ]

    SCOPE_CHOICES = [
        ('SCOPE_1', 'SCOPE_1'),
        ('SCOPE_2', 'SCOPE_2'),
        ('SCOPE_3', 'SCOPE_3'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE)

    scope = models.CharField(max_length=20, choices=SCOPE_CHOICES)

    category = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)

    raw_value = models.FloatField()
    raw_unit = models.CharField(max_length=50)

    normalized_value = models.FloatField()
    normalized_unit = models.CharField(max_length=50)

    occurred_at = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    is_suspicious = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.activity_type}"


class AuditLog(models.Model):
    emission_record = models.ForeignKey(
        EmissionRecord,
        on_delete=models.CASCADE
    )

    field_name = models.CharField(max_length=100)

    old_value = models.TextField()
    new_value = models.TextField()

    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Audit - {self.field_name}"