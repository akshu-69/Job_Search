# Job_search — Java / Full-Stack Opportunities

Private GitHub repository for **[@akshu-69](https://github.com/akshu-69)**. These are job discovery results, not submitted applications.


## Start here

**[Ready-to-apply links: 8 verified roles](ready-to-apply/APPLY_LINKS.md)** — official individual employer application URLs that passed screening during the October 30, 2026 run.

**[All 34 discovered links, categorized](all-collected-links/ALL_LINKS.md)** — includes those eight plus 10 for review, 12 with unknown posting dates, 2 older, 2 unverified. Do not confuse these other categories with verified eligible jobs.

- [`ready-to-apply/jobs.csv`](ready-to-apply/jobs.csv): official verified job details and dates.
- [`all-collected-links/all_discovered_links.csv`](all-collected-links/all_discovered_links.csv): all 34 candidate links with explicit status.
- [`data/master_verified.csv`](data/master_verified.csv): canonical qualifying master (8).
- [`data/review.csv`](data/review.csv), [`data/date_unknown.csv`](data/date_unknown.csv), [`data/older_strong_matches.csv`](data/older_strong_matches.csv), [`data/unverified_leads.csv`](data/unverified_leads.csv): excluded from 300 count.
- [`data/exclusions.csv`](data/exclusions.csv): 11 excluded results (links not guaranteed).
- [`data/seen_requisitions.csv`](data/seen_requisitions.csv): de-duplication ledger for continuation runs.
- [`data/applications_tracker.csv`](data/applications_tracker.csv): personal application tracking, initially empty.
- [`checkpoints/2026-10-30.json`](checkpoints/2026-10-30.json): source coverage and next-run checkpoint.
- [`logs/2026-10-30_search_coverage.csv`](logs/2026-10-30_search_coverage.csv): search coverage.
- [`docs/search_criteria.md`](docs/search_criteria.md): full-time role inclusion/exclusion rules.
- [`docs/resume_matching_notes.md`](docs/resume_matching_notes.md): skills used for matching (no private resume stored).
- [`scripts/deduplicate.py`](scripts/deduplicate.py): check for duplicate job IDs and URLs.

## Progress snapshot

| Category | Count | Counted in 300? |
|---|---:|---|
| Ready to apply / verified qualifying | **8** | Yes |
| Review needed | 10 | No |
| Date unknown | 12 | No |
| Older strong matches | 2 | No |
| Unverified leads | 2 | No |
| Excluded | 11 | No |

**Target:** 300 verified unique eligible full-time jobs/day. **Completed so far:** 8 in the initial batch; only 3 employers represented. No scheduled daily search, no submitted applications, no historical cross-day dedup available without earlier results.

**Recheck all application links before submitting.** The qualification and open-status evidence is as of 2026-10-30, not continuous monitoring. This repository is intended to be private and must not include the user's original resume or personal contact information.