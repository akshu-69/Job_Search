"""Print duplicate employer/requisition (or URL) records across nonexclusion CSVs."""
import csv
from pathlib import Path
base=Path(__file__).resolve().parents[1]/'data'
files=['master_verified.csv','review.csv','date_unknown.csv','older_strong_matches.csv','unverified_leads.csv']
seen={}
for file in files:
    with (base/file).open(encoding='utf-8-sig', newline='') as f:
        for x in csv.DictReader(f):
            k=(x['employer'].strip().lower(),x['requisition_id'].strip() or x['direct_job_url'].split('?')[0])
            if k in seen:print('POSSIBLE DUPLICATE:',file,'vs',seen[k],k)
            else:seen[k]=file
print('unique candidate records:',len(seen))
