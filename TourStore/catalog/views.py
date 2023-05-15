import datetime
from django.db.models import Q
from django.shortcuts import render
from django.utils.timezone import make_aware
from django.views import generic
from .models import Tours, TravelCompanies


def index(request):
    return render(
        request,
        'index.html',
    )


def contacts(request):
    return render(
        request,
        'contacts.html',
    )


class ToursListlView(generic.ListView):
    model = Tours
    template_name = 'tours_list.html'

    def get_queryset(self):
        query_search = self.request.GET.get('search', '')
        query_price_from = self.request.GET.get('price_from', '')
        query_price_to = self.request.GET.get('price_to', '')
        query_date_from = self.request.GET.get('date_from', '')
        query_date_to = self.request.GET.get('date_to', '')
        query_country = self.request.GET.get('country', '')
        query_city = self.request.GET.get('city', '')
        query_company = self.request.GET.get('company', '')
        if query_price_from != '' and query_price_from.isdigit():
            query_price_from = float(query_price_from)
        else:
            query_price_from = 0
        if query_price_to != '' and query_price_to.isdigit():
            query_price_to = float(query_price_to)
        else:
            query_price_to = 1000000
        if query_date_from != '':
            query_date_from = make_aware(datetime.datetime.fromisoformat(query_date_from))
        else:
            query_date_from = make_aware(datetime.datetime(2000, 1, 1))
        if query_date_to != '':
            query_date_to = make_aware(datetime.datetime.fromisoformat(query_date_to))
        else:
            query_date_to = make_aware(datetime.datetime(3000, 1, 1))
        if query_country == 'Любая':
            query_country = ''
        if query_city == 'Любая':
            query_city = ''
        if query_company == 'Любая':
            query_company = ''

        object_list = Tours.objects.filter(Q(Q(name__icontains=query_search) | Q(description__icontains=query_search)) &
                                           Q(start_date__range=[query_date_from, query_date_to]) &
                                           Q(price__range=[query_price_from, query_price_to]))
        return object_list


class TravelCompaniesListlView(generic.ListView):
    model = TravelCompanies
    template_name = 'travelcompanies_list.html'

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        object_list = TravelCompanies.objects.filter(name__icontains=query)
        return object_list


class TravelCompaniesDetailView(generic.DetailView):
    model = TravelCompanies


class TourDetailView(generic.DetailView):
    model = Tours
    slug_field = 'url'
    slug_url_kwarg = 'url'
