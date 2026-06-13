# AI Tools Setup Portfolio Project

## Overview

This repository documents the setup process for the required AI development tools and environment.

## Tools Installed

- Cursor IDE
- Claude Code add-on
- Codex add-on
- GitHub

## System Information

- Device: MacBook Air (2022)
- Chip: Apple M2
- Operating System: macOS Tahoe 26.4
- Cursor Version: 3.5.17 (initially), later tested with ARM64 version

## Steps Completed

1. Installed Cursor IDE from the provided link
2. Created a GitHub account and public repository
3. Opened the repository in Cursor
4. Attempted to install Claude Code and Codex through Cursor Marketplace
5. Installed Claude Code through terminal commands after it was not visible in the Marketplace
6. Logged into Claude Code successfully
7. Installed Codex through terminal commands
8. Tested troubleshooting methods for Codex visibility in Cursor
9. Created README.md documentation
10. Committed and pushed repository changes to GitHub

## Issues Encountered and Solutions

### 1. Marketplace / Extensions Panel Difference

The instructions referenced an "Extensions" panel, but in my version of Cursor the interface used a "Marketplace" section instead.

Solution:
- Verified that Marketplace serves the same purpose as Extensions in newer Cursor versions
- Continued installation process through Marketplace and terminal tools

### 2. Claude Code Not Appearing in Marketplace

Claude Code was not visible in the Cursor Marketplace.

Solution:
- Used Cursor AI assistant to troubleshoot
- Opened terminal within Cursor
- Installed Claude Code using terminal commands
- Confirmed that Claude Code became accessible through terminal interface

### 3. Codex Add-on Not Visible in Marketplace

The Codex add-on was also not available through Marketplace search.

Solution:
- Installed Codex through terminal commands
- Investigated Cursor documentation and troubleshooting methods

### 4. Codex Not Appearing in Cursor UI After Installation

After installation, Codex did not appear in the Cursor interface as expected.

Solution attempts included:
- Checking hidden sidebar views
- Resetting Cursor view locations
- Testing extension visibility settings
- Reviewing compatibility between newer Cursor versions and Codex integration
- Testing ARM64-native Cursor installation for Apple Silicon compatibility

Outcome:
- Installation completed successfully, though Codex UI visibility appeared to be affected by current Cursor version behavior and extension compatibility changes

## What I Learned

During this process I became more familiar with:
- AI-assisted development environments
- Terminal-based installation workflows
- GitHub repository management
- Troubleshooting software compatibility issues
- Navigating evolving developer tooling ecosystems

---

## Outbound Sales Research

### What Was Collected

This repository includes a primary research base on outbound sales and GTM, organized under `research/`:

- **10 practitioners** tracked across LinkedIn and YouTube
- **51 LinkedIn posts** collected manually across all 10 experts (`research/linkedin-posts/`)
- **12 YouTube video transcripts** fetched automatically via script (`research/youtube-transcripts/`)

### Collection Method

**YouTube transcripts** were fetched using the `youtube-transcript-api` Python library (no API key required). A script reads a list of video URLs from `research/youtube-transcripts/video-list.txt`, pulls the transcript for each video, and saves it as a markdown file with the video title and URL at the top. Paragraphs are broken at roughly 60-second intervals for readability.

**LinkedIn posts** were collected manually — each post was saved with its publication date, URL, and full text under a heading, following a consistent format across all files.

### Why These Ten Experts

The ten experts were selected to cover the full outbound pipeline end-to-end, not any single discipline. Each was also chosen because they run real outbound — agencies, daily senders, and coaches with live programs.

| Discipline | Experts |
|---|---|
| **Data, targeting & automation** | Eric Nowoslawski, Jordan Crawford |
| **Cold email copywriting** | Will Allred, Florin Tatulea, Kristina Finseth |
| **Cold calling & objection handling** | Jason Bay, Leslie Venetz, Josh Braun |
| **Multichannel systems & sequencing** | Jed Mahrle, Morgan J Ingram |

- **Eric Nowoslawski** (Growth Engine X) — Clay power user, sends millions of cold emails per month; teaches the actual tech stack.
- **Jordan Crawford** (Blueprint GTM) — Signal- and AI-native outbound; known for the "permissionless value prop" approach.
- **Will Allred** (Lavender AI) — Co-founder of an AI email coaching tool; developed the "Above the Line" framework.
- **Florin Tatulea** — Sales leader and LinkedIn Top Voice; cold email frameworks and multichannel copy.
- **Kristina Finseth** — Outbound practitioner focused on tactical personalization at scale.
- **Jason Bay** (Outbound Squad) — Founder; REPLY Method for cold calling and multichannel outreach.
- **Leslie Venetz** (The Sales-Led GTM Agency) — 250,000+ cold calls; enterprise prospecting.
- **Josh Braun** — Independent coach; tonality, lowering resistance, and the "poke the bear" philosophy.
- **Jed Mahrle** (Practical Prospecting) — Built outbound systems for 50+ B2B tech companies.
- **Morgan J Ingram** — Multichannel and video prospecting; sequencing across channels.

Full annotated source list: [`research/sources.md`](research/sources.md)
