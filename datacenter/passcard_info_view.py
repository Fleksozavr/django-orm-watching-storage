from datacenter.models import Visit, Passcard
from django.shortcuts import render, get_object_or_404
import pytz


def passcard_info_view(request, passcode):
		passcard = get_object_or_404(Passcard, passcode=passcode)
		visits = Visit.objects.filter(passcard=passcard)
		this_passcard_visits = []

		for visit in visits:
				duration = visit.get_duration()
				is_strange = visit.is_visit_long()
				entered_at = visit.entered_at.strftime('%d-%m-%Y %H:%M')

				this_passcard_visits.append({
						'entered_at': entered_at,
						'duration': duration,
						'is_strange': is_strange
				})

		context = {
				'passcard': passcard,
				'this_passcard_visits': this_passcard_visits
		}
		return render(request, 'passcard_info.html', context)