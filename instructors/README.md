# For the course instructors

<h2>Table of contents</h2>

- [Set up a new lab](#set-up-a-new-lab)
- [Add the `LAB_TOKEN`](#add-the-lab_token)
- [Get meeting transcript](#get-meeting-transcript)
- [Get meeting report](#get-meeting-report)
- [Enter the devshell](#enter-the-devshell)
- [Review a file by conventions](#review-a-file-by-conventions)
- [Lessons learned](#lessons-learned)

## Set up a new lab

1. [Fork](../wiki/github.md#fork-a-repo) the previous lab repo.
2. [Protect the `main` branch](../wiki/github.md#protect-a-branch).

## Add the `LAB_TOKEN`

Need a fine-grained token for:

- the [`lint.yml`](../.github/workflows/lint.yml) workflow.
  - because the workflow uses `actions/checkout` which needs a token to checkout a private repo.

Permissions:

- Contents: read
- Metadata: read

<https://github.com/orgs/community/discussions/160497#discussioncomment-11456365>

Complete these steps:

1. Enable fine-grained tokens for your repo:

   Go to the org page on `GitHub` -> `Settings` ->
`Third-party Access` -> Click `Personal access tokens` -> click `Active tokens` -> click `Fine-grained tokens` -> Enable `Allow access via fine-grained personal access tokens` and `Require administrator approval`

2. Create a fine-grained token.

   Go to `github.com` -> click your profile in the upper-right corner -> click `Settings` -> scroll to `Developer settings` in the left sidebar -> click `Developer settings` -> click `Personal access tokens` -> click `Fine-grained tokens` -> click `Generate new token` -> write `Token name` -> select the `inno-se-toolkit` as the `Resource owner` -> click `Only select repositories` -> select the lab repo -> go to `Permissions` -> click Add permissions -> check `Contents` -> check `Metadata` -> click Generate token.
3. Go to the lab repo -> `Settings` -> `Security` -> `Actions` -> `Repository secrets` -> Click `New repository secret`.
4. Create a secret `LAB_TOKEN` with the value of the token.

## Get meeting transcript

1. Use `AssemblyAI`. They provide free credits that are enough for hundreds of hours of meeting recordings.
2. Open the `Playground`
3. Choose the `Universal 2` model.
4. Set `Language` -> `Automatic Language Detection`.
5. Enable `Code Switching`.
6. Upload the recording.
7. Use `Export sentences` to get a `JSON` file with labelled sentences.
8. Save the file to `meetings/week-<N>/meeting-<M>/meetings/sentences.json`

   Identify which speakers are the same person.
9. In `Claude`, use the skill `/get-meeting-transcript <N> <M>` to get transcript files.

   Merge speakers that are the same person: provide the flag `--merge`.
   Example: `--merge B=C`.

## Get meeting report

1. In `Claude`, use the skill `/get-meeting-report <N> <M>` to get a report at `meetings/week-<N>/meeting-<M>/report.md` following the rules in [`meeting-report.md`](../contributing/conventions/meetings/meeting-report.md).
2. In `Claude`, use the skill `/review-meeting-report` to review the report against the transcript and other files discussed during the meeting.

## Enter the devshell

<!-- TODO link to setup -->

## Review a file by conventions

Use the `Claude` skill `/review-file <filepath>`.

## Lessons learned

- First check a file from the instructional point of view, then work on the formatting (see [review a file](#review-a-file-by-conventions)).
