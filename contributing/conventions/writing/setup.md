# Setup file conventions

<h2>Table of contents</h2>

- [1. Overview](#1-overview)
- [2. `lab/setup/setup-full.md` — Full setup](#2-labsetupsetup-fullmd--full-setup)
  - [2.1. Key rules for `setup.md`](#21-key-rules-for-setupmd)
- [3. `lab/setup/setup-simple.md` — Lab-specific setup](#3-labsetupsetup-simplemd--lab-specific-setup)
  - [3.1. Key rules for `setup-simple.md`](#31-key-rules-for-setup-simplemd)
- [4. Checklist](#4-checklist)

Use this file when creating or updating lab setup files: `lab/setup/setup-full.md` and `lab/setup/setup-simple.md`.

---

## 1. Overview

Two setup files live in `lab/tasks/`. They serve different audiences.

- `setup.md` — full first-time setup. Written for a student who has never done any lab in this course. Covers every step from scratch: finding a partner, creating a VM, installing programs, forking, cloning, configuring the environment, and starting services. Use `(UPD)` labels to mark steps that must be redone for this specific lab even if done before.
- `setup-simple.md` — lab-specific setup. Written for a returning student who has the base tools from the previous lab. Covers only what is new or changed: cleaning up the previous lab's services, forking the new repo, cloning, configuring environment files, and starting services.

The README links to `setup-simple.md` by default, with a note directing first-timers to `setup.md`.

---

## 2. `lab/setup/setup-full.md` — Full setup

Structure:

```markdown
# Lab setup

- [1. Required steps](#1-required-steps)
  - [1.1. (UPD) Find a partner](#11-upd-find-a-partner)
  - [1.2. <Setup step>](#12-setup-step)
  - ...
- [2. Optional steps](#2-optional-steps)
  - [2.1. <Enhancement>](#21-enhancement)
  - ...

## 1. Required steps

> [!IMPORTANT]
> Some steps have the `(UPD)` label.
>
> These steps must be completed to get the right setup for this lab,
> even if you have completed similar steps in the previous lab.

### 1.1. (UPD) Find a partner

1. Find a partner for this lab.
2. Sit next to them.

> [!IMPORTANT]
> You work on tasks independently from your partner.
>
> You and your partner work together when reviewing each other's work.

### 1.2. <Setup step>
...

---

## 2. Optional steps

These enhancements can make your life easier:

<!-- no toc -->
- [<Enhancement>](#21-enhancement)
- ...
```

### 2.1. Key rules for `setup.md`

- Cover every step from scratch: partner, VM, programs, fork, clone, environment, start services.
- Mark steps that must be redone for this lab with `(UPD)` in the heading. Explain at the top that `(UPD)` steps are required even if done before.
- Partner setup is always step 1 (students review each other's PRs).
- Each step links to wiki docs for the detailed how-to.
- Separate required steps from optional enhancements with `---`.

---

## 3. `lab/setup/setup-simple.md` — Lab-specific setup

Structure:

```markdown
# Lab setup

- [1. Required steps](#1-required-steps)
  - [1.1. Clean up the previous lab](#11-clean-up-the-previous-lab)
  - [1.2. <Setup step>](#12-setup-step)
  - ...

## 1. Required steps

> [!NOTE]
> This lab builds on the same tools and setup from Lab <N>.
> If you completed Lab <N>, most tools are already installed.
> The main changes are: <short list of what's new or changed>.

### 1.1. Clean up the previous lab

...

### 1.2. <Setup step>
...
```

### 3.1. Key rules for `setup-simple.md`

- Target audience: returning students who have the base setup from the previous lab.
- Do NOT include first-time-only steps: installing VS Code, Docker, Git, SSH, configuring Git, setting up the shell, creating a VM (unless the lab specifically requires a fresh VM).
- Start with cleanup of the previous lab's services to free ports and disk space.
- Include: fork setup (new repo per lab), clone, environment files, starting services locally, and deployment if the lab requires it.
- Add a note at the top explaining what changed from the previous lab.
- Do not use `(UPD)` labels — every step in this file is already lab-specific.
- No optional steps section — optional enhancements are covered in `setup.md`.

---

## 4. Checklist

- [ ] `setup.md` covers all first-time steps: partner, VM, programs, fork, clone, environment, start services.
- [ ] `setup-simple.md` covers only lab-specific steps: cleanup, fork, clone, environment, start services.
- [ ] README links to `setup-simple.md` by default with a note directing first-timers to `setup.md`.
- [ ] Partner/collaborator setup is documented.
