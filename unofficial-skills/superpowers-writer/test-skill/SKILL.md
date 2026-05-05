---
name: test-skill
description: A test skill that demonstrates multi-agent coordination and script execution
---

# Test Skill

## Overview

This is a demonstration skill that shows how agents can coordinate with other agents and execute external Python scripts. It uses general-agent to get the current time, then executes a companion script in the `scripts/` directory.

**Core principle:** Demonstrate multi-agent coordination and script execution workflow with clear instructions.

**Announce at start:** "I'm using the test-skill to demonstrate script execution with multi-agent coordination."

## What This Skill Does

1. Calls general-agent to get current timestamp
2. Loads and displays the skill instructions
3. Executes a Python script from the `scripts/` directory
4. Reports the complete workflow results

## Step 1: Get Current Time

First, use the general-agent to get the current time:
```
agent_executor(agent_name="general-agent", task="Get the current date and time in a readable format (e.g., 'YYYY-MM-DD HH:MM:SS')")
```

This demonstrates multi-agent coordination and shows how skills can delegate tasks to other agents.

## Step 2: Verify Script Location

Check that the script exists:
- Use: `bash(command="ls -la scripts/hello.py")`
- Expected: Should see the hello.py file listed

## Step 3: Execute the Script with Timestamp

Run the Python script using the bash tool:
```
bash(command="python scripts/hello.py")
```

The script will execute and display its output.

## Step 4: Report Complete Results

After execution:
- Display the current time obtained from general-agent
- Show the script output from hello.py
- Confirm successful execution
- Report the exit code (should be 0 for success)
- Summarize the complete workflow: time retrieval → script execution

## Script Execution Guide

**Why use bash tool for scripts?**
- Executes system commands including Python scripts
- Captures both stdout and stderr
- Returns exit codes for error handling

**Relative Path Note:**
- Scripts are located in `scripts/` relative to the skill directory
- The agent's working directory is set to the skill's root
- Use `scripts/hello.py` not an absolute path

**Multi-Agent Coordination:**
- Use `agent_executor` tool to delegate tasks to specialized agents
- general-agent can handle time/date queries and other general tasks
- Combine results from multiple agents into a unified workflow

**Error Handling:**
If script fails:
- Check if Python is installed: `bash(command="python --version")`
- Verify script permissions: `bash(command="ls -l scripts/hello.py")`
- Check script syntax: `bash(command="python -m py_compile scripts/hello.py")`

## Example Usage

When a user requests to test this skill:
1. Announce the skill activation: "I'm using the test-skill to demonstrate script execution with multi-agent coordination."
2. Call general-agent to get current time
3. Verify the script exists
4. Execute `python scripts/hello.py`
5. Display both the timestamp and script output
6. Confirm successful completion of the entire workflow

## What This Demonstrates

This skill showcases:
- **Multi-Agent Coordination**: Delegating time retrieval to general-agent
- **Script Execution**: Running Python scripts from skill directories
- **Workflow Composition**: Combining multiple steps into a cohesive process
- **Agent Communication**: Using agent_executor tool to coordinate between agents

## Remember

- Use agent_executor to delegate tasks to other agents like general-agent
- Always use relative paths from skill root
- Check script exists before execution
- Report both output and exit codes
- Handle errors gracefully
- Demonstrate multi-agent coordination in your workflow

## Integration

This is a demonstration skill showing how to:
- Structure a skill with companion scripts
- Coordinate multiple agents using agent_executor tool
- Write clear instructions for multi-step workflows
- Handle script execution results in agent workflows
- Combine different agent capabilities into a cohesive process
