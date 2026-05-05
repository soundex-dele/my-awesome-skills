---
name: writing-execution
description: Use when you have a written writing plan to execute with review checkpoints
---

# Writing Execution

## Overview

Load plan, review critically, present execution plan for confirmation, then execute writing section-by-section with immediate file writes and report for review between sections.

**Core principle:** Plan confirmation first, then section-by-section execution with immediate file writes and review checkpoints.

**Two-phase workflow:**
1. **Plan Phase:** Present execution plan → Get user confirmation → Start writing
2. **Execution Phase:** Write section → Write to file immediately → Present for review → Next section

**Announce at start:** "I'm using the writing-execution skill to write this content."

## The Process

### Step 1: Load and Review Plan

1. Read plan file
2. Review critically - identify any questions or concerns about the plan
3. If concerns: Raise them with your human partner before starting
4. If no concerns: Proceed to Step 1.5

### Step 1.5: Present and Confirm Execution Plan

**CRITICAL:** Before starting any writing, you MUST present the execution plan and get explicit user confirmation.

Present an execution plan to the user:

```markdown
## Writing Execution Plan

I will write **[N]** sections in the following order:

**Sections:**
1. [Section 1 Title] - [estimated word count]
2. [Section 2 Title] - [estimated word count]
3. [Section 3 Title] - [estimated word count]
...

**Process:**
1. Present this plan for confirmation first
2. Write one section at a time
3. **Write each section to file immediately** after completion
4. Present each section for review before proceeding
5. Continue until all sections complete

**Total estimated word count:** [sum of all sections]
**Output file:** [filename.md]
```

**Ask user:** "Does this execution plan look good? Should I proceed with writing the first section?"

**MANDATORY:** Wait for explicit user confirmation before proceeding to Step 2. Do not start writing until the user approves the plan.

### Step 2: Execute Section and Write to File

**Default: Work on sections sequentially**

For each section:
1. Mark as in_progress
2. Complete research if needed
3. Draft content following plan guidelines
4. Review against style and voice guidelines
5. Verify word count targets
6. **IMMEDIATELY write the section to the output file** using Write tool
7. Mark as completed

**IMPORTANT:** Write each section to the file immediately after completing it. Do not wait until the end to write all sections at once. The file should be updated incrementally as you complete each section.

### Step 3: Report and Present

After writing the section to file:
- Show the drafted content you just wrote
- Note word count vs target
- Confirm the file has been updated
- Highlight any questions or areas needing feedback
- Say: "Section [N] has been written to [filename.md]. Ready for feedback on this section."

### Step 4: Continue

Based on feedback:
- Apply revisions if needed
- Move to next section
- Repeat until complete

### Step 5: Final Review

After all sections complete:
- Review entire piece for flow and coherence
- Check transitions between sections
- Verify overall word count
- Ensure consistency in tone and voice
- Present final draft for approval

## When to Stop and Ask for Help

**STOP writing immediately when:**
- Hit a blocker (missing information, unclear guidance, stuck on phrasing)
- Plan has critical gaps preventing progress
- You don't understand a section requirement
- Research doesn't support the planned points
- Word count is significantly off target

**Ask for clarification rather than guessing.**

## When to Revisit Earlier Steps

**Return to Review (Step 1) when:**
- Partner updates the plan based on your feedback
- Fundamental approach needs rethinking
- Outline needs adjustment based on content evolution

**Don't force through blockers** - stop and ask.

## Writing Best Practices

**During drafting:**

- **Write first, edit later** - Get ideas down, then refine
- **Follow plan structure** - Don't reorganize without approval
- **Match the planned tone** - Stay consistent with voice guidelines
- **Use research effectively** - Incorporate evidence naturally
- **Transitions matter** - Connect ideas within and between sections

**When reviewing each section:**

- **Read aloud in your head** - Check rhythm and flow
- **Verify key points** - Did you cover what the plan specified?
- **Check word count** - Are you significantly over or under?
- **Tone check** - Does this match the intended voice?
- **Transition check** - Does this lead naturally to the next section?

**Common issues to watch for:**

- **Passive voice overload** - Active voice is more engaging
- **Sentence variety** - Mix short and long sentences
- **Paragraph length** - Break up long blocks of text
- **Jargon overload** - Explain or avoid domain-specific terms
- **Weak transitions** - Ensure smooth flow between ideas

## Remember

**Critical workflow:**
1. **Plan confirmation first** - Present execution plan and get explicit approval before writing anything
2. **Write to file immediately** - Each section must be written to the output file as soon as it's completed
3. **Review plan critically** - Identify concerns before starting
4. **Follow plan structure exactly** - Don't reorganize without approval
5. **Between sections: present work and wait for feedback** - Show what you just wrote to the file
6. **Stop when blocked, don't guess** - Ask for clarification
7. **File is updated incrementally** - The output file grows section by section, not all at once at the end

## Integration

**Required workflow skills:**
- **superpowers-writer:writing-brainstorming** - Creates the outline that feeds into the plan
- **superpowers-writer:writing-plans** - Creates the plan this skill executes
- **superpowers-writer:writing-review** - Review and refine completed content

**Alternative approaches:**
- **Guided execution (this skill)** - Section-by-section with checkpoints
- **Independent execution** - Full draft with single review at end (use this skill but batch all sections)
