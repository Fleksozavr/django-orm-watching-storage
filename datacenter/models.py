import django
import pytz
from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime


class Passcard(models.Model):
		is_active = models.BooleanField(default=False)
		created_at = models.DateTimeField(auto_now=True)
		passcode = models.CharField(max_length=200, unique=True)
		owner_name = models.CharField(max_length=255)

		def __str__(self):
				if self.is_active:
						return self.owner_name
				return f'{self.owner_name} (inactive)'


class Visit(models.Model):
		created_at = models.DateTimeField(auto_now=True)
		passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
		entered_at = models.DateTimeField()
		leaved_at = models.DateTimeField(null=True)

	
		def __str__(self):
				return '{user} entered at {entered} {leaved}'.format(
						user=self.passcard.owner_name,
						entered=self.entered_at,
						leaved=(
								f'leaved at {self.leaved_at}'
								if self.leaved_at else 'not leaved'
						)
				)

	
		def get_duration(self):
				entered_at = self.entered_at
				current_time = timezone.now()
				moscow_time = localtime(current_time, timezone=pytz.timezone('Europe/Moscow'))
				leaved_at = self.leaved_at if self.leaved_at else moscow_time
				time_spent = leaved_at - entered_at
				return time_spent

	
		def format_duration(self, duration):
				hours = duration.seconds // 3600
				minutes = (duration.seconds % 3600) // 60
				seconds = duration.seconds % 60

				format_time_spent_str = f"{hours}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

				return format_time_spent_str

	
		def is_visit_long(self, minutes=60):
				if self.leaved_at is None:
						return False
				duration = self.leaved_at - self.entered_at
				return duration.total_seconds() / 60 > minutes