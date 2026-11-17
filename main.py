import json
from pathlib import Path

def run():
    path = Path(__file__).resolve().parents[1] / "data" / "fhir_bundle.json"
    bundle = json.loads(path.read_text())
    patients, encounters = [], []
    for entry in bundle['entry']:
        resource = entry['resource']
        if resource['resourceType'] == 'Patient':
            patients.append({'patient_key': resource['id'], 'active': resource.get('active', True)})
        elif resource['resourceType'] == 'Encounter':
            encounters.append({'encounter_key': resource['id'], 'patient_key': resource['subject']['reference'].split('/')[-1], 'status': resource['status']})
    valid_keys = {p['patient_key'] for p in patients}
    return {'patients': patients, 'encounters': encounters, 'orphan_encounters': [e for e in encounters if e['patient_key'] not in valid_keys]}

if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
