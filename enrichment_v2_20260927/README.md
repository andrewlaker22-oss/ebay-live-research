# One-run Gemini enrichment

No original data is edited. No package from Fable needs to be installed or run.

## Automatic sequence

1. Duplicate and hash-check all eight community CSVs (8,378 stored rows).
2. Build 481 collected conversation groups, preserving source IDs, duplicate locations and missing-parent/date flags.
3. Pilot ten groups: four Reddit, two TikTok, two YouTube, two replay chats. Codex checks the pilot before scaling.
4. Reuse the pilot results and complete the remaining conversation digests.
5. Blind check: 400 rows, 50 per source tab, with earlier labels/AI descriptions hidden from Gemini.
6. Control: 300 random rows outside the documented keyword screen, with source context and missing Live-related fields.
7. Validate citations, quotes, output coverage and source hashes. Assemble FOR_FABLE.

After the conversation pilot, the runner exercises the first blind and control batches before completing all remaining
conversation groups. Completed batches are reused. No additional user launch is needed.

The blind check measures agreement, NOT accuracy. No human-labelled ground truth is available. The control is a discovery
sample, not a representative survey. Full per-row recoding is intentionally not included. Existing labels remain intact.

## Budget and recovery

- Gemini 2.5 Flash, text only, no search or other paid tools. Bounded 1,024-token reasoning allowance after pilot QA. No model switching.
- Shared $8 ceiling across pilot and all stages, not $8 per stage or restart.
- Exact prompt token count plus extra input headroom and maximum output allowance are reserved before every generation.
- Usage-based costs include reported thinking tokens if any. The estimate is not invoice reconciliation or an account-wide cap.
- Every job and cost is saved in SQLite. Raw requests/responses are saved separately without the API key.
- A failed, blocked, quota-limited, malformed or uncertain paid request stops the run. No automatic paid retry.
- Supervised development revisions are recorded separately, including the rejected initial pilot. All revisions and
  conservative allowances for rejected requests count toward the same cap. Excess quote counts are formatting warnings,
  not evidence failures: exact source excerpts are retained rather than throwing away usable responses.
- After a clean interruption between jobs, rerunning the same worker skips completed jobs. If interrupted during a paid
  request, the run stops for inspection rather than risking a duplicate charge. An OS lock prevents two workers.
- API key is read from the existing local research key file or GEMINI_API_KEY; never copied into outputs.

## Files

- STATUS.md: plain-language progress and spend.
- FOR_FABLE/READ_ME_FIRST.md: final handoff entry point. Partial outputs are clearly marked by their coverage/status file.
- original_copies/: untouched duplicate CSVs.
- supporting/: inputs, sampling, requests, raw responses and integrity records.

Codex operates the pilot review and worker. The user does not need to launch separate stages.

Verified pricing reference: https://ai.google.dev/gemini-api/docs/pricing
Standard Gemini 2.5 Flash text input $0.30/M tokens, output $2.50/M tokens. Verified 2026-09-27.
