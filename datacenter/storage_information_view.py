from datacenter.models import Passcard, Visit
from django.shortcuts import render


def storage_information_view(request):
	non_closed_visitors = Visit.objects.filter(leaved_at__isnull=True)
	non_closed_visits = []

	for visit in non_closed_visitors:
		entered_at = visit.entered_at.strftime('%d-%m-%Y %H:%M')
		duration = visit.format_duration(visit.get_duration())

		non_closed_visits.append({
			'who_entered': visit.passcard.owner_name,
			'entered_at': entered_at,
			'duration': duration,
		})

	context = {
		'non_closed_visits': non_closed_visits,
	}
	return render(request, 'storage_information.html', context)