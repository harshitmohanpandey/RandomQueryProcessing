from django.db.models import F, Q, Sum

from UseCaseApp.models import Dataset


def use_case_one(groupby,date,sortby):
    """
    Method to generate results for usecase one
    """
    output_entries = Dataset.objects.values(*groupby) \
        .annotate(impressions=Sum('impressions_field'),clicks =Sum('clicks_field')) \
            .filter(date_field__lte=date) \
                .order_by(sortby)
    return output_entries

def use_case_two(groupby,datefrom,dateto,os,sortby):
    """
    Method to generate results for usecase two
    """
    output_entries = Dataset.objects.values(*groupby) \
            .annotate(installs=Sum('installs_field'),clicks =Sum('clicks_field')) \
                .filter(Q(date_field__gte=datefrom)&Q(date_field__lte=dateto)&Q(os_field=os)) \
                    .order_by(sortby)
    return output_entries

def use_case_three(groupby,date,country,sortby):
    """
    Method to generate results for usecase three
    """
    output_entries = Dataset.objects.values(*groupby) \
        .annotate(revenue=Sum('revenue_field')) \
            .filter(Q(date_field=date)&Q(country_field=country)) \
                .order_by(sortby)
    return output_entries

def use_case_four(groupby,country,sortby):   
    """
    Method to generate results for usecase four
    """
    output_entries = Dataset.objects.values(*groupby) \
            .annotate(spendon=Sum('spend_field'),CPI =F('spend_field') / F('installs_field')) \
                .filter(country_field=country) \
                    .order_by(sortby)
    return output_entries
