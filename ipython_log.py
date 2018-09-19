# IPython log file

get_ipython().run_line_magic('pinfo', '%gui')
3*8
_2
_i2
get_ipython().run_line_magic('logstart', '')
path = 'usagov_bitly_data.txt'
open(path).readline()
open(path).readline()
import json
records = [json.loads(line) for line in open(path)]
records[0]
records[0]['tz']
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
times_zones[:10]
time_zones[:10]
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] +=1
        else:
            counts[x] = 1
    return counts
counts = get_counts(time_zones)
counts['America/New_York']
len(time_zones)
from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts
counts = get_counts2(time_zones)
counts['America/New_York']
len(time_zones)
def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
top_counts(counts)
from collections import Counter
counts = Counter(time_zones)
counts.most_common(10)
from pandas import DataFrame, Series
import pandas as pd
frame = DataFrame(records)
frame
frame['tz'][:10]
tz_counts = frame['tz'].value_counts()
tz_counts[:10[
]]
tz_counts[:10]
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10]
tz_counts[:10].plot(kind='barh', rot=0)
results = Series([x.split()[0] for x in frame.dropna()])
results[:5]
results.value_counts()[:8]
frame['a'][1]
frame['a'][50]
results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5
]
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
operating_system[:5]
prettyprinting()
ppring()
get_ipython().run_line_magic('pprint', '()')
get_ipython().run_line_magic('pprint', '()')
operating_system[:6]
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
agg_counts{:10]
agg_counts[:10]
indexer = agg_counts.sum(1)/argsort()
indexer = agg_counts.sum(1).argsort()
indexr[:10]
indexer[:10]
indexer = agg_counts.sum(1).argsort()
indexer[:10]
count_subset = agg_counts.take(indexer)[-10:]
count_subset
count_subset.plot(kind='barh', stacked=True)
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
strings = ['foo', 'foobar', 'baz', 'quix', 'python'] *1000
method1 = [x for x in strings if x.startswith('foo')]
get_ipython().run_line_magic('time', 'method1')
