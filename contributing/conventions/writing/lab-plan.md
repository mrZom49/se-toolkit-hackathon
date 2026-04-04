# Lab plan conventions — applies to `instructors/lab-plan.md` only

<h2>Table of contents</h2>

- [1. Purpose](#1-purpose)
- [2. File location](#2-file-location)
- [3. Document structure](#3-document-structure)
- [4. Header and metadata](#4-header-and-metadata)
- [5. Main goals](#5-main-goals)
- [6. Learning outcomes](#6-learning-outcomes)
  - [6.1. Bloom's taxonomy mapping](#61-blooms-taxonomy-mapping)
  - [6.2. "In simple words" restatement](#62-in-simple-words-restatement)
- [7. Lab story](#7-lab-story)
- [8. Task descriptions](#8-task-descriptions)
  - [8.1. Required tasks](#81-required-tasks)
  - [8.2. Optional tasks](#82-optional-tasks)
  - [8.3. Purpose statement](#83-purpose-statement)
  - [8.4. Summary](#84-summary)
  - [8.5. Acceptance criteria](#85-acceptance-criteria)
- [9. Formatting](#9-formatting)
- [10. Review dimensions](#10-review-dimensions)
  - [10.1. D1. Learning outcome quality](#101-d1-learning-outcome-quality)
  - [10.2. D2. Bloom's taxonomy coverage](#102-d2-blooms-taxonomy-coverage)
  - [10.3. D3. Lab story coherence](#103-d3-lab-story-coherence)
  - [10.4. D4. Task sequencing and dependencies](#104-d4-task-sequencing-and-dependencies)
  - [10.5. D5. Acceptance criteria quality](#105-d5-acceptance-criteria-quality)
  - [10.6. D6. Outcome-to-task alignment](#106-d6-outcome-to-task-alignment)
  - [10.7. D7. Structural compliance](#107-d7-structural-compliance)
  - [10.8. D8. Practical feasibility](#108-d8-practical-feasibility)
  - [10.9. D9. Student experience level fit](#109-d9-student-experience-level-fit)
  - [10.10. D10. Main goals clarity](#1010-d10-main-goals-clarity)
- [11. Checklist](#11-checklist)

Use this file when creating or reviewing a lab plan (`instructors/lab-plan.md`).

For lab creation conventions (README, git workflow, narrative), see [lab.md](lab.md).
For task design conventions, see [tasks.md](tasks.md).

---

## 1. Purpose

A lab plan is an internal design document that outlines the learning outcomes, narrative, and task structure for a new lab. It is written before task files and serves as the blueprint for the lab's content.

Lab plans are not student-facing. They live under `instructors/` and are used by lab authors and reviewers.

---

## 2. File location

The lab plan is a single file at `instructors/lab-plan.md`.

---

## 3. Document structure

```markdown
# Lab plan — <Title>

**Topic:** <topic>
**Date:** <YYYY-MM-DD>

## Main goals

- <Goal 1>
- <Goal 2>

## Learning outcomes

By the end of this lab, students should be able to:

- [<Bloom's level>] <Outcome 1>
- [<Bloom's level>] <Outcome 2>
- ...

In simple words:

> 1. <First-person statement 1>
> 2. <First-person statement 2>
> ...

## Lab story

<Narrative paragraph — 2 to 4 sentences>

A senior engineer explains the assignment:

> 1. <High-level description of required task 1>
> 2. <High-level description of required task 2>
> 3. <High-level description of required task 3>

## Required tasks

### Task 1 — <Title>

**Purpose:**

<one sentence>

**Summary:**

<two to four paragraphs, five to ten sentences total>

**Acceptance criteria:**

- <criterion 1>
- <criterion 2>
- ...

---

### Task 2 — <Title>

**Purpose:**

<one sentence>

**Summary:**

<two to four paragraphs>

**Acceptance criteria:**

- ...

---

### Task 3 — <Title>

**Purpose:**

<one sentence>

**Summary:**

<two to four paragraphs>

**Acceptance criteria:**

- ...

---

## Optional task

### Task 1 — <Title>

**Purpose:**

<one sentence>

**Summary:**

<two to four paragraphs>

**Acceptance criteria:**

- ...
```

---

## 4. Header and metadata

- The H1 title follows the format `# Lab plan — <Title>`.
- `**Topic:**` is a short phrase describing the subject area (e.g., "REST API testing", "container security").
- `**Date:**` is the creation date in ISO format (`YYYY-MM-DD`).

---

## 5. Main goals

The `## Main goals` section appears immediately after the metadata and before learning outcomes. It contains a bullet list of two to three high-level goals that describe the instructor's intent — what the lab should convey or demystify for students.

Goals are informal and aspirational. They are not the same as learning outcomes — they capture the motivating "why" behind the lab, not measurable student abilities.

---

## 6. Learning outcomes

List four to six outcomes under the heading `## Learning outcomes`.

Each outcome must be concrete and observable — it describes something the student can demonstrably do, not something they "understand" in an unverifiable way.

### 6.1. Bloom's taxonomy mapping

Prefix each outcome with its Bloom's taxonomy level in square brackets. Valid levels:

- `[Remember]` — recall facts and basic concepts (identify, list, name, define)
- `[Understand]` — explain ideas or concepts (explain, describe, summarize, classify)
- `[Apply]` — use information in new situations (implement, execute, use, solve)
- `[Analyze]` — draw connections among ideas (compare, contrast, differentiate, examine)
- `[Evaluate]` — justify a decision or course of action (assess, argue, defend, judge)
- `[Create]` — produce new or original work (design, construct, develop, formulate)

Rules:

- Start each outcome with an action verb matching the Bloom's level.
- The outcomes must cover at least two distinct Bloom's levels.
- At least one outcome must be at `[Apply]` level or above.

### 6.2. "In simple words" restatement

After the outcomes list, include an `In simple words:` line followed by a blockquote with a numbered list. Each item restates one outcome as a first-person sentence (e.g., "I can deploy a containerised service.").

The numbered items must match the outcomes one-to-one in the same order.

---

## 7. Lab story

The lab story is a realistic workplace scenario of two to four sentences. Frame it as a task a student encounters after joining a team, company, or project.

After the narrative paragraph, include:

```markdown
A senior engineer explains the assignment:

> 1. <High-level description of required task 1>
> 2. <High-level description of required task 2>
> 3. <High-level description of required task 3>
```

The senior engineer's numbered list must mirror the three required tasks — one item per task, in order.

For lab story conventions shared with the README (tone, blockquote style, cross-lab continuity), see [Lab story and narrative](lab.md#3-lab-story-and-narrative).

---

## 8. Task descriptions

The lab plan contains exactly three required tasks and one optional task. Each task has three titled sections — `**Purpose:**`, `**Summary:**`, and `**Acceptance criteria:**` — each on its own line with the content starting on the next line.

### 8.1. Required tasks

Required tasks appear under `## Required tasks` as `### Task 1 — <Title>` through `### Task 3 — <Title>`.

Required tasks must build on each other sequentially — task 2 depends on the output or knowledge from task 1, and task 3 depends on task 2.

Separate each task with a horizontal rule (`---`).

### 8.2. Optional tasks

One optional task appears under `## Optional task` (singular heading) as `### Task 1 — <Title>`.

Optional tasks must be independent — completable without depending on other optional tasks.

### 8.3. Purpose statement

Each task includes a `**Purpose:**` section heading followed by exactly one sentence on the next line that explains why the task matters — what the student will learn or achieve.

### 8.4. Summary

Each task includes a `**Summary:**` section heading followed by five to ten sentences split across two to four short paragraphs describing what the student does. Break on natural topic boundaries — for example, put setup and exploration in one paragraph and implementation details in the next. The summary should be specific enough to guide task file creation but not so detailed that it prescribes every step.

### 8.5. Acceptance criteria

Each task includes an `**Acceptance criteria:**` section with three to five bullet items. Criteria must be concrete and verifiable — a reviewer or autochecker can determine pass/fail without subjective judgment.

Do not use checkbox format (`- [ ]`) in lab plans. Checkboxes are reserved for task files where reviewers check items during PR review. Lab plans use plain bullet lists (`-`).

Do not invent specific technology choices, file paths, or implementation details beyond what is needed to illustrate the plan.

---

## 9. Formatting

- Use `---` horizontal rules between tasks within a section.
- All sentences end with `.`.
- Each sentence is on its own line.
- Do not use Markdown tables.
- Do not include a table of contents in the lab plan document — it is short enough to navigate without one.

---

## 10. Review dimensions

Use these dimensions when reviewing a lab plan for conceptual and structural problems. For each finding, record: the dimension, the section or line number(s), a short description, severity (`[High]`, `[Medium]`, or `[Low]`), and a suggested fix.

Severity guide:

- **High** — the plan has a structural gap that would lead to a flawed lab (missing outcomes, misaligned tasks, unverifiable criteria).
- **Medium** — the plan has an issue that would cause confusion during lab creation (vague purpose, weak criteria, unclear sequencing).
- **Low** — minor improvement that would make the plan clearer but does not affect lab quality.

### 10.1. D1. Learning outcome quality

- Is each outcome concrete and observable, starting with an action verb?
- Does each outcome describe something the student can demonstrably do?
- Are there vague outcomes like "understand X" or "learn about X" without a measurable verb?

### 10.2. D2. Bloom's taxonomy coverage

- Does each outcome have a valid Bloom's level prefix (`[Remember]`, `[Understand]`, `[Apply]`, `[Analyze]`, `[Evaluate]`, or `[Create]`)?
- Does the action verb match the declared level?
- Are at least two distinct Bloom's levels used?
- Is at least one outcome at `[Apply]` level or above?

### 10.3. D3. Lab story coherence

- Does the narrative frame a realistic workplace scenario?
- Does the senior engineer's numbered list mirror the three required tasks?
- Is the story connected to the lab's domain and topic?

### 10.4. D4. Task sequencing and dependencies

- Do required tasks build on each other sequentially (task 2 depends on task 1, task 3 depends on task 2)?
- Is the optional task independent of other optional tasks?
- Does complexity increase across required tasks (observe → build → extend)?

### 10.5. D5. Acceptance criteria quality

- Does each task have three to five acceptance criteria?
- Is each criterion concrete and verifiable (pass/fail without subjective judgment)?
- Are there open-ended or vague criteria (e.g., "student understands X", "code is clean")?
- Do criteria avoid inventing unnecessary implementation details?

### 10.6. D6. Outcome-to-task alignment

- Do the three required tasks collectively cover all listed learning outcomes?
- Are there outcomes that no task addresses?
- Are there tasks that do not contribute to any listed outcome?

### 10.7. D7. Structural compliance

- Does the document follow the template in [Document structure](#3-document-structure)?
- Is the header format correct (`# Lab plan — <Title>`, `**Topic:**`, `**Date:**`)?
- Is the `## Main goals` section present with two to three bullet items?
- Are there four to six learning outcomes?
- Does the "In simple words" list match outcomes one-to-one?
- Are purpose statements exactly one sentence?
- Are summaries five to ten sentences split across two to four paragraphs?
- Are `---` rules present between tasks?

### 10.8. D8. Practical feasibility

- Can each task be completed within a single lab session (roughly two to three hours for all required tasks combined)?
- Are the required tools, services, and environments realistically available to students (no paid accounts, no complex infrastructure)?
- Are there tasks that depend on external services with rate limits, approval queues, or uptime risks?
- Is the scope of each task well-bounded, or could it expand unpredictably during implementation?

### 10.9. D9. Student experience level fit

- Can a student with basic programming knowledge and limited prior exposure to the topic complete the required tasks?
- Does task 1 provide enough scaffolding (examples, reference commands, expected output) to onboard students who are new to the domain?
- Are there tasks that assume advanced knowledge without introducing it first (e.g., complex CLI flags, non-trivial configuration formats, unfamiliar protocols)?
- Is the cognitive jump between consecutive tasks manageable, or does difficulty spike abruptly?
- Does the optional task clearly signal that it targets students who want a deeper challenge?

### 10.10. D10. Main goals clarity

- Does the `## Main goals` section exist between the metadata and learning outcomes?
- Are there two to three goals?
- Does each goal describe the instructor's intent — what the lab should convey — rather than a measurable student ability?
- Are goals distinct from the learning outcomes (aspirational "why" vs. observable "what")?

---

## 11. Checklist

- [ ] Title follows the format `# Lab plan — <Title>`.
- [ ] `**Topic:**` and `**Date:**` metadata are present.
- [ ] `## Main goals` section contains two to three bullet items describing instructor intent.
- [ ] Four to six learning outcomes are listed.
- [ ] Each outcome has a `[<Bloom's level>]` prefix with a matching action verb.
- [ ] At least two distinct Bloom's levels are used.
- [ ] At least one outcome is at `[Apply]` level or above.
- [ ] "In simple words" list has one item per outcome in the same order.
- [ ] Lab story is two to four sentences with a realistic workplace scenario.
- [ ] Senior engineer's numbered list mirrors the three required tasks.
- [ ] Exactly three required tasks and one optional task are present.
- [ ] Required tasks build on each other sequentially.
- [ ] The optional task is independent.
- [ ] Each task has a one-sentence `**Purpose:**`.
- [ ] Each task has a summary of five to ten sentences split across two to four paragraphs.
- [ ] Each task has three to five concrete, verifiable acceptance criteria.
- [ ] Acceptance criteria use plain bullets (`-`), not checkboxes (`- [ ]`).
- [ ] `---` rules separate tasks within a section.
- [ ] All sentences end with `.`.
- [ ] Each sentence is on its own line.
- [ ] All required tasks are completable within a single lab session.
- [ ] No task depends on paid services, complex infrastructure, or unreliable external resources.
- [ ] Task 1 is approachable for students with limited prior exposure to the topic.
- [ ] Difficulty increases gradually across required tasks without abrupt spikes.
