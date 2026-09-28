"""Free local lookup tools for Fable. No API, network, key, or model calls."""
import argparse
from collections import Counter
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def read(name):
    with (HERE/name).open(encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', choices=['inventory', 'search', 'group', 'evidence', 'communities', 'disagreements', 'control-signals'])
    p.add_argument('--text', default='')
    p.add_argument('--community', default='')
    p.add_argument('--id', default='')
    p.add_argument('--limit', type=int, default=10)
    args = p.parse_args()
    limit = min(max(args.limit, 1), 50)
    if args.action == 'inventory':
        print((HERE/'05_COVERAGE_AND_QA.json').read_text(encoding='utf-8'))
        return
    if args.action in ['disagreements', 'control-signals']:
        filename = '02_BLIND_LABEL_CHECK.jsonl' if args.action == 'disagreements' else '03_CONTROL_ENRICHMENT.jsonl'
        rows = read(filename)
        selected = [r for r in rows if not r['exact_set_agreement']] if args.action == 'disagreements' else [r for r in rows if r['unexpected_live_signal']]
        print(json.dumps({'total_matching': len(selected), 'returned': selected[:limit]}, ensure_ascii=False, indent=2))
        return
    source = read('04_SOURCE_EVIDENCE_AND_EXISTING_LABELS.jsonl')
    if args.action == 'communities':
        counts = Counter()
        for r in source:
            if r['excluded_event']:
                continue
            for label in set(x.strip() for x in r['existing_labels']['flash_community'].split(';') if x.strip()):
                counts[(label, r['tab'])] += 1
        print(json.dumps({'warning': 'Existing AI labels, not validated communities. Multi-label rows appear in multiple categories. Counts are unique evidence IDs within tab, not people.',
            'counts': [{'label': k[0], 'tab': k[1], 'rows': v} for k,v in sorted(counts.items())]}, ensure_ascii=False, indent=2))
    elif args.action == 'evidence':
        print(json.dumps([r for r in source if r['evidence_id'] == args.id], ensure_ascii=False, indent=2))
    elif args.action == 'group':
        digests = read('01_CONVERSATION_DIGESTS.jsonl')
        matches = [d for d in digests if args.id in [d['group_id'], d['job_id']]]
        ids = {i for d in matches for i in d['source_evidence_ids']}
        print(json.dumps({'digests': matches, 'source_rows': [r for r in source if r['evidence_id'] in ids]}, ensure_ascii=False, indent=2))
    else:
        selected = []
        for r in source:
            labels = r['existing_labels']['flash_community']
            if args.community and args.community.casefold() not in labels.casefold():
                continue
            content = json.dumps(r['source'], ensure_ascii=False)
            if args.text.casefold() not in content.casefold():
                continue
            selected.append({'evidence_id': r['evidence_id'], 'tab': r['tab'], 'group_id': r['group_id'],
                'existing_community': labels, 'date_status': r['date_status'], 'source_excerpt': content[:500]})
        print(json.dumps({'total_matching': len(selected), 'returned': selected[:limit],
            'warning': 'Search matches source fields only. Community filtering uses fallible previous AI labels.'}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
