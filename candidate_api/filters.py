
import django_filters
from django.db.models import Q, Case, When, IntegerField, Value
from .models import Candidate

class CandidateFilter(django_filters.FilterSet):
    # This creates the text input field in the browsable API UI.
    # The `method` argument tells django-filter to call our custom search function.
    q = django_filters.CharFilter(method='search_by_relevance', label='Search by Name')

    class Meta:
        model = Candidate
        fields = ['q']

    def search_by_relevance(self, queryset, name, value):
        query_words = value.strip().split()
        if not query_words:
            return queryset.none() # Return an empty queryset if search is empty

        # Build a Q object to filter candidates whose name contains ANY of the query words.
        filter_condition = Q()
        for word in query_words:
            filter_condition |= Q(name__icontains=word)
        relevance_score = Value(0, output_field=IntegerField())
        for word in query_words:
            # For each word, add a Case expression to the score.
            # This adds 1 to the score if the word is found, otherwise adds 0.
            relevance_score += Case(
                When(name__icontains=word, then=1),
                default=Value(0),
                output_field=IntegerField()
            )

        # Filter, annotate with the score, and order the results.
        return queryset.filter(filter_condition).annotate(
            relevance=relevance_score
        ).order_by('-relevance', 'name')
