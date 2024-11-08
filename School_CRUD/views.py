from Component.models import Requrement
from django.shortcuts import render
from django.http import Http404

def detailPage (request, detail_id):
  detailPage = Requrement.objects.get(pk=detail_id)
  if detailPage is not None:

    context = {
      'detailPage' : detailPage
    }
    
    return render (request, 'Include/detail.html', context)
  else:
    raise Http404 ('Not Worked!')