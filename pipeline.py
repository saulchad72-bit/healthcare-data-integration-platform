import csv,json
from pathlib import Path

def run(source,destination):
    valid=[]; rejected=[]; seen=set()
    for row in csv.DictReader(open(source,newline='')):
        errors=[]
        if not row['claim_id']:errors.append('missing_claim_id')
        if row['claim_id'] in seen:errors.append('duplicate_claim_id')
        if row['status'] not in {'paid','denied','pending'}:errors.append('invalid_status')
        try:
            amount=float(row['billed_amount'])
            if amount<0:errors.append('negative_amount')
        except ValueError:errors.append('invalid_amount');amount=0
        if errors:rejected.append({'row':row,'errors':errors})
        else: valid.append({'claim_id':row['claim_id'],'member_id':row['member_id'],'status':row['status'],'billed_amount':amount});seen.add(row['claim_id'])
    result={'valid':valid,'rejected':rejected,'note':'Synthetic data only; not HIPAA certification'}
    Path(destination).write_text(json.dumps(result,indent=2));return result
