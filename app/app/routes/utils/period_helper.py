from datetime import datetime
from utils.date_helper import get_months, get_semesters, get_trimesters, get_weeks, get_days, parse_date, get_day_limit

async def requires_inital_date(params, function, filters = {}, graph = {}):
    attrs = {**filters}
    period = ''
    include_all = False
    helper_func = get_days
    if('include_all' in params):
        include_all = 0 if params['include_all'] == '0' else 1
    if('initial_date' in params and 'final_date' in params):
        attrs['initial_date'] = parse_date(params['initial_date'])
        attrs['final_date'] = parse_date(params['final_date'])
    elif('initial_date' in params):
        initial_date, final_date = get_day_limit(parse_date('initial_date'))
        attrs['initial_date'] = initial_date
        attrs['final_date'] = final_date
    elif('period' in params):
        period = params['period']
    if(period == 'months'):
        helper_func = get_months
    elif(period == 'semesters'):
        helper_func = get_semesters
    elif(period == 'trimesters'):
        helper_func = get_trimesters
    elif(period == 'weeks'):
        helper_func = get_weeks
    if(include_all == True):
        periods = helper_func(should_include_list = True)
        results = []
        for initial_date, final_date in periods:
            attrs['initial_date'] = initial_date
            attrs['final_date'] = final_date
            r = await function(**attrs)
            r['initial_date'] = str(initial_date) 
            r['final_date'] = str(final_date)
            r['graphs'] = graph
            results.append(r)
        return results
    else:
        initial_date, final_date = helper_func()
        attrs['initial_date'] = initial_date
        attrs['final_date'] = final_date
        r = await function(**attrs)
        r['initial_date'] = str(initial_date) 
        r['final_date'] = str(final_date)
        r['graphs'] = graph
        return [r]
