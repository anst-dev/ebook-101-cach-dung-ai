# 101 Cách Dùng AI Miễn Phí — Program

## Goal
Tạo ebook hoàn chỉnh (101 cách, ~50.000 từ, tiếng Việt) → PDF có cover + illustrations.

## Metric
- **Primary**: số chương hoàn thành / 8
- **Quality**: mỗi cách có tool + steps + ví dụ + mẹo
- **Completion**: PDF export thành công

## Constraints
- Deadline: 5 min/experiment
- Tools: NotebookLM (research + content), agy CLI (code), Hermes (orchestration)
- Never stop until: 101 cách viết xong + PDF exported

## Tool assignments
| Tool | Role |
|------|------|
| **NotebookLM** | Research sources, generate content, manage assets |
| **agy CLI** | Write code, automation scripts, PDF pipeline |
| **Hermes/Nexus** | Orchestrate, verify, coordinate |

## Current blockers (resolve first)
1. agy CLI --print mode: output empty (tried 4x) → SEARCH WEB for fix
2. NotebookLM: auth expired → need login

## Experiment log
See: experiments.tsv
