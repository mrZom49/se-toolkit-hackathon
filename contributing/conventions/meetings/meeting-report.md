# Meeting report conventions

<h2>Table of contents</h2>

- [1. File locations](#1-file-locations)
- [2. Instructions](#2-instructions)
  - [2.1. Line-by-line pass](#21-line-by-line-pass)
  - [2.2. Coverage check](#22-coverage-check)
- [3. General rules](#3-general-rules)
  - [3.1. Language](#31-language)
  - [3.2. Output format](#32-output-format)
  - [3.3. Speaker references](#33-speaker-references)
  - [3.4. No personal information](#34-no-personal-information)
  - [3.5. Attendance](#35-attendance)
  - [3.6. Skip noise](#36-skip-noise)
  - [3.7. Unclear content](#37-unclear-content)
  - [3.8. Do not infer decisions](#38-do-not-infer-decisions)
  - [3.9. Superseded decisions](#39-superseded-decisions)
  - [3.10. Cross-references](#310-cross-references)
  - [3.11. Items as subsections](#311-items-as-subsections)
  - [3.12. Clean headings](#312-clean-headings)
  - [3.13. Anchor links](#313-anchor-links)
  - [3.14. Timestamps](#314-timestamps)
  - [3.15. Direct quotes vs paraphrasing](#315-direct-quotes-vs-paraphrasing)
  - [3.16. Depth calibration](#316-depth-calibration)
  - [3.17. Off-topic digressions](#317-off-topic-digressions)
  - [3.18. Recurring meetings](#318-recurring-meetings)
- [4. Sections](#4-sections)
  - [4.1. Table of contents](#41-table-of-contents)
  - [4.2. Metadata](#42-metadata)
  - [4.3. Executive summary](#43-executive-summary)
  - [4.4. Action points](#44-action-points)
  - [4.5. Key dates](#45-key-dates)
  - [4.6. Deadlines](#46-deadlines)
  - [4.7. Decisions](#47-decisions)
    - [4.7.1. Example format](#471-example-format)
  - [4.8. Open questions](#48-open-questions)
  - [4.9. Status updates](#49-status-updates)
  - [4.10. Questions and answers](#410-questions-and-answers)
  - [4.11. Discussions](#411-discussions)
  - [4.12. Glossary](#412-glossary)
- [5. Review](#5-review)
  - [5.1. Transcript coverage](#51-transcript-coverage)
  - [5.2. Accuracy](#52-accuracy)
  - [5.3. Files discussed](#53-files-discussed)
  - [5.4. Format compliance](#54-format-compliance)
  - [5.5. Internal consistency](#55-internal-consistency)

## 1. File locations

- **Transcript**: `instructors/meetings/week-N/meeting-M/transcripts/transcript-by-speaker.txt`
- **Report**: `instructors/meetings/week-N/meeting-M/report.md`

Substitute actual week and meeting numbers for N and M.

## 2. Instructions

Write a comprehensive meeting report based on the provided transcript.

### 2.1. Line-by-line pass

Go through the transcript **line by line for substantive content** and make sure every point, detail, example, quote, and discussion is captured in the appropriate section. In the [Decisions](#47-decisions), [Q&A](#410-questions-and-answers), and [Discussions](#411-discussions) sections, do not summarize — expand. Include specific examples, analogies, and arguments that speakers used. If speakers disagreed or evolved their position during the discussion, capture that progression. If speakers outright contradicted each other without resolution, note the disagreement explicitly.

### 2.2. Coverage check

After completing the report, review the transcript one more time and verify:

- Every speaker who contributed substantively is referenced at least once
- Every topic transition in the transcript is accounted for in a section
- No decisions were inferred — all are explicitly stated or agreed upon
- Proposals and hypotheticals are in [Open questions](#48-open-questions), not [Decisions](#47-decisions)

If any gaps are found, go back and fill them in. Do not include this checklist in the final report.

## 3. General rules

### 3.1. Language

Always write the report in English.
Use a neutral, professional tone.
Translate quotes and terminology as needed.
For domain-specific terms, keep the original alongside the English translation in parentheses (e.g., "sprint review (ревью спринта)") to avoid ambiguity.

### 3.2. Output format

Write the report in Markdown using the heading structure defined below.
Write each sentence on its own line (see [Instructions wording](../writing/common.md#41-instructions-wording)).

### 3.3. Speaker references

Use speaker labels from the transcript (e.g., Speaker A, Speaker B).
If the transcript uses real names instead of labels, replace them with Speaker A/B/C in order of first appearance.

### 3.4. No personal information

Never include real names, email addresses, phone numbers, physical addresses, social media handles, company names, project code names, client names, or any other personally identifiable information (PII) in the report.
Redact or replace all such references with generic labels (e.g., "Speaker A," "the client," "the external tool," "Company X").
If a speaker mentions a specific person outside the meeting, refer to them by role (e.g., "the team lead," "the vendor contact").

### 3.5. Attendance

Note if any speaker joined late, left early, or was silent throughout the meeting.

### 3.6. Skip noise

Ignore connection issues, screen sharing problems, audio glitches, crosstalk, filler words, and other non-substantive artifacts.
Focus only on meaningful content.

### 3.7. Unclear content

If something in the transcript is inaudible or the meaning is ambiguous, flag it with [unclear] rather than guessing.

### 3.8. Do not infer decisions

Only record decisions that were explicitly stated or clearly agreed upon.
Do not infer consensus from silence.
Proposals, hypotheticals, and "what if" suggestions that were not concluded belong in [Open questions](#48-open-questions), not [Decisions](#47-decisions).

### 3.9. Superseded decisions

If a later discussion in the same meeting overrides an earlier agreement, only include the final version in Decisions.
Note the evolution briefly (e.g., "Initially agreed on X, later revised to Y because...").

### 3.10. Cross-references

When a decision leads to an action point, or an open question relates to a decision, reference it using an anchor link (see [Anchor links](#313-anchor-links)).
This applies across all sections.

### 3.11. Items as subsections

Write each distinct item within a section — decisions, open questions, action points, status update items, glossary terms, Q&A pairs, and discussions — as a Markdown subsection with a heading rather than a bullet list entry or blockquote.
Write the content beneath the heading as prose paragraphs.
This makes each item individually linkable via a Markdown anchor.
Never use bold text to label items within a section.
Each heading must use the format `### S.N. Label N: Title` — where `S.N.` is the two-level section number (e.g., `5.2.`), `Label` is the section label (`Decision`, `Open question`, `Action point`, `Key date`, `Deadline`, `Question and answer`, or `Discussion`), and `N` is the item number within that section (omitted for `Decision`, `Key date`, `Deadline`, `Question and answer`, and `Discussion`).

### 3.12. Clean headings

Headings must contain only the item title — no dates, consensus levels, priorities, severity tags, speaker labels, timestamps, or any other metadata.
Metadata in headings breaks automatic table-of-contents generation and anchor links.
Place all contextual metadata — speaker attribution, timestamp ranges, owners, priority, consensus level, and similar details — at the beginning of the first paragraph beneath the heading, highlighted with **bold**.
Never append metadata to the heading or place it on a separate line before the paragraph.

### 3.13. Anchor links

When cross-referencing a specific item in the report, link to its subsection anchor rather than using plain text (e.g., `[Decision: Use PostgreSQL for the primary data store](#51-decision-use-postgresql-for-the-primary-data-store)` instead of "See Decision: Use PostgreSQL").
The anchor is derived from the full heading by lowercasing, removing punctuation, and replacing spaces with hyphens — so `### 5.1. Decision: Use PostgreSQL` becomes `#51-decision-use-postgresql`.

### 3.14. Timestamps

If the transcript includes timestamps, reference them at key moments so readers can locate the corresponding point in a recording.
Always wrap timestamps in square brackets — single points as `[14:32]` and ranges as `[01:10:15–01:12:08]`.
Square brackets are reserved for transcript-navigation timestamps only.
Deadlines, scheduled dates, and other future times mentioned by speakers should be written as plain text (e.g., "by March 15", "next Monday at 10:00").

### 3.15. Direct quotes vs paraphrasing

Use direct quotes when the speaker's exact wording carries meaning — strong opinions, definitions, commitments, or memorable phrasing.
Paraphrase for routine discussion.

### 3.16. Depth calibration

Scale the report's depth proportionally to the meeting's length and substance.
A 15-minute standup should not produce the same volume as a 2-hour planning session.

### 3.17. Off-topic digressions

Off-topic digressions (tools, mentoring, industry news, etc.) should still be captured in the relevant section (usually [Discussions](#411-discussions)).

### 3.18. Recurring meetings

If the transcript references a prior meeting or is clearly part of a series, note that context in the [Executive summary](#43-executive-summary).

## 4. Sections

Each section below describes what belongs in it and how detailed it should be. Use these exact headings in the report.

### 4.1. Table of contents

Immediately after the report title, include a table of contents listing every section heading below as a Markdown link. This gives readers a quick overview and lets them jump to the relevant part. Use an HTML heading (`<h2>Table of contents</h2>`) instead of a Markdown `##` heading so the TOC entry does not appear inside its own list. The TOC list itself must be in Markdown format (bullet list with `- [Link](#anchor)` syntax).

### 4.2. Metadata

A structured block at the top of the report:

- **Date & time**: Meeting date and time in `DD.MM.YYYY, HH:MM - HH:MM` format (from transcript if available, otherwise `DD.MM.YYYY, HH:MM - HH:MM`)
- **Duration**: Approximate length of the meeting
- **Participants**: Number of speakers and their labels (e.g., "4 participants: Speaker A, B, C, D")
- **Recording**: Link to the meeting recording (if provided, otherwise `<link to the recording>`)
- **Transcript**: Link to `transcript-by-speaker.txt` in the `transcripts/` subdirectory
- **Files discussed**: List of files that were explicitly mentioned, reviewed, or discussed during the meeting (by file name or path as referenced in the transcript). Omit if no specific files were discussed.

### 4.3. Executive summary

3-5 bullet points covering the most important outcomes of the meeting. This is for readers who will not read the full report. Focus on key decisions, blockers, and deadlines.

### 4.4. Action points

Concrete next steps with owners (by speaker label) and deadlines (if mentioned). Write each action point as a subsection heading in the format `### S.N. Action point N: Title` followed by a prose paragraph that states the owner, priority (**[blocking]**, **[high]**, **[medium]**, or **[low]**), scheduling details, and any relevant context. If a task was mentioned but no owner was assigned, say so in the prose. Do not place owner or priority on a separate bold-label line before the paragraph. Every action point originates from a decision, discussion, or open question — cross-reference the source item using an anchor link (e.g., `"Stems from [Decision: Use PostgreSQL for the primary data store](#52-decision-use-postgresql-for-the-primary-data-store)"`). If a single decision spawns multiple action points, each one should link back independently.

### 4.5. Key dates

Dates and milestones mentioned during the meeting, even in passing. Write each distinct date as a subsection heading in the format `### S.N. Key date: Title` followed by a prose paragraph describing what the date refers to, who mentioned it, and any relevant context. Do not use a bullet list with bold labels.

### 4.6. Deadlines

Deadlines mentioned during the meeting, even in passing. Write each deadline as a subsection heading in the format `### S.N. Deadline: Title` followed by a prose paragraph describing what the deadline refers to, who mentioned it, and any relevant context. Do not use a bullet list with bold labels.

### 4.7. Decisions

**This is the largest section.** Every conclusion, agreement, or direction discussed should be its own item — even small ones. Write each decision as a subsection heading in the format `### S.N. Decision: Title`. Group decisions by topic, not by chronological order. For each decision, include:

- What was decided
- **Consensus level**: State **unanimous**, **majority**, or **contentious** (note dissenters by speaker label) at the start of the paragraph body, not in the heading
- The reasoning or discussion behind it (which speaker said what, what alternatives were considered)
- Specific examples, quotes, or analogies used (translated to English if needed)
- If a decision evolved during the meeting, show the progression
- Cross-references to related action points or open questions

Be exhaustive — capture every distinct decision, no matter how small. Cover all topics raised: naming, data model, scope, task structure, implementation approach, security, testing, deployment, tooling, terminology, ordering, scheduling, and anything else discussed.

**Important**: Only include conclusions that were explicitly agreed upon. Proposals and hypotheticals that were not resolved belong in [Open questions](#48-open-questions).

#### 4.7.1. Example format

```markdown
### 5.1. Decision: Use PostgreSQL for the primary data store

**Consensus: unanimous.**
Speaker A proposed PostgreSQL, citing its JSON support for flexible schemas. Speaker B initially suggested MongoDB but agreed after Speaker A demonstrated that PostgreSQL's JSONB columns would cover the same use case without adding a second database. Speaker C noted: "We already have operational expertise with Postgres, so this keeps the ops burden low." *(See [Action point 3](#73-action-point-3-deploy-database-migrations))*
```

### 4.8. Open questions

Things that were raised but not resolved — including proposals, hypotheticals, and "what if" suggestions that did not reach a conclusion. Write each open question as a subsection heading in the format `### S.N. Open question N: Title`. Include context on why they remain open, any preliminary opinions expressed, and any disagreements that prevented resolution. Cross-reference related decision items where applicable.

### 4.9. Status updates

What is already done, built, deployed, or available before this meeting. Include specifics: which artifacts exist (documents, prototypes, deployed services, repos), what tools were used or demonstrated during the meeting, and any issues encountered. Write each distinct status item as a subsection heading followed by prose — do not use bold labels in a bullet list.

### 4.10. Questions and answers

Questions that came up during the meeting and were answered on the spot. Write each Q&A pair as a subsection heading in the format `### S.N. Question and answer: Question text` (e.g., `### 10.1. Question and answer: What mechanism can we use to...`) followed by prose paragraphs. The heading contains only the label and the question — do not use bold `**Q:**` labels, and do not append speaker attribution or timestamps to the heading. State who asked, who answered, and the relevant timestamp range in the opening sentence of the paragraph instead. Include:

- Which speaker asked and which speaker answered
- The full answer with examples and analogies

When a speaker presents slides, gives a demo, or shares a screen for an extended monologue, write it as a `### S.N. Demo: Title` or `### S.N. Presentation: Title` subsection: summarize the content presented, then capture the discussion that followed in full detail.

### 4.11. Discussions

Extended conversations, off-topic digressions (tools, mentoring experiences, industry news), and other substantive exchanges that are not direct Q&A pairs. Write each distinct discussion as a subsection heading in the format `### S.N. Discussion: Topic` (e.g., `### 11.1. Discussion: Deployment strategy trade-offs`) followed by prose paragraphs. The heading contains only the label and the topic — do not use bold `**Discussion:**` labels, and do not append speaker attribution or timestamps to the heading. State who participated and the relevant timestamp range in the opening sentence of the paragraph instead.

### 4.12. Glossary

If the meeting introduced, defined, or clarified any terms, acronyms, or project-specific jargon, include them here. Omit this section if no new terminology was introduced. Write each term as a subsection heading (e.g., `### Sprint Review`) followed by a prose paragraph with the definition. This makes each term individually referenceable via a Markdown anchor.

## 5. Review

Before considering a report final, review it against the following categories. For each finding, cite the relevant transcript line or report line number.

### 5.1. Transcript coverage

Go through the transcript **line by line**. Flag each substantive point, decision, question, disagreement, example, or topic that appears in the transcript but is **missing or under-represented** in the report. Ignore filler, greetings, and non-substantive noise.

### 5.2. Accuracy

Flag each claim in the report that **contradicts** the transcript — wrong speaker attribution, incorrect timestamp, misquoted text, a decision recorded as unanimous when there was dissent, etc.

### 5.3. Files discussed

For every file listed under **Metadata → Files discussed**, verify that the report's references to that file's content (task names, structure, terminology, etc.) are **consistent** with the actual file content.
Flag each reference in the report that does not match what the file actually says.
If no files are listed, skip this check.

### 5.4. Format compliance

Check the report against the rules in [Section 3 (General rules)](#3-general-rules) and [Section 4 (Sections)](#4-sections).
Flag violations — missing sections, items written as bullet lists instead of subsections, bold labels used instead of headings, PII leaks, missing cross-references, etc.

### 5.5. Internal consistency

Check for contradictions **within** the report itself — e.g., a decision that conflicts with an open question, an action point referencing a non-existent decision, broken anchor links, duplicate numbering, etc.
