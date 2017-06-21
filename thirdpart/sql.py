def get_setup_data(self, case_data):
    setup_data = []
    if not case_data:
        return setup_data

    for case_index in case_data:
        # ignore empty dict
        if not case_index:
            continue
        for item in case_index.values():
            for t_case in item:
                setup_items = [{item['case_id']: item['setup']} for item in t_case.items() if
                               'setup' in item and 'case_id' in item]
                setup_data.append(setup_items)
    return setup_data
