from django.db.models import Count

from webapp.models import TestSample, TestLabel


def get_data_for_report(filter_params):
    testsample_filtered = TestSample.objects.filter(
        admission_date__range=[filter_params['from_date'], filter_params['to_date']]).all()
    testsample_data = list(
        testsample_filtered.values('type').annotate(dcount=Count('type')).order_by()
    )
    total_testsample = testsample_filtered.count()

    testlabel_filtered = TestLabel.objects.filter(
        is_done=True,
        end_date__range=[filter_params['from_date'], filter_params['to_date']]).all()
    testlabel_data = list(
        testlabel_filtered.values('type').annotate(dcount=Count('type')).order_by()
    )
    total_testlabel = testlabel_filtered.count()

    return [testsample_data, total_testsample, testlabel_data, total_testlabel]


def preprocess_data(data_list):
    """

    @param data_list: A list of tuples (dictionary, labels)
    """
    for data_tuple in data_list:
        # make labels human readable
        for entry in data_tuple[0]:
            key = entry['type']
            for choice in data_tuple[1]:
                if choice[0] == key:
                    entry['type'] = choice[1]
                    break
