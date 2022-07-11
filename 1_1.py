
from django.db.models import Q, Count


def get_journal_statistics():
    """
    This method uses from Parent model to Child model concept.
    So here we annotate (group by) all the publications and find the count of 
    downloads and views by making use of Count and Filter and select only the 
    "id", "total_views", "total_downloads".
    And then to form the proper structure iterate over the queryset and create the
    dict and return it.
    """
    all_data = Publication.objects.all().prefetch_related('hit_set').annotate(
        total_views=Count('hit_set__action', filter=Q(hit_set__action=Hit.PAGEVIEW)),
        total_downloads=Count('hit_set__action', filter=Q(hit_set__action=Hit.DOWNLOAD))
    ).values("id", "total_views", "total_downloads")

    summary = {}
    for data in all_data:
        summary[data["id"]] = (data["total_views"],data["total_downloads"])
    return summary
