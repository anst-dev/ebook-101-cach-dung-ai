#!/usr/bin/env python3
"""
agy_wrapper.py — Wrapper for Antigravity CLI on Windows/MSYS
agy --print mode doesn't output to stdout. This wrapper:
1. Runs agy --print with a prompt
2. Reads the latest conversation transcript JSONL
3. Extracts the MODEL response
Usage: python agy_wrapper.py "your prompt here"
"""
import subprocess
import sys
import os
import json
import glob
import time
from pathlib import Path

AGY = r"C:\Users\Administrator\AppData\Local\agy\bin\agy.exe"
BRAIN_DIR = Path.home() / ".gemini" / "antigravity-cli" / "brain"

def get_latest_transcript():
    """Find the most recently modified transcript_full.jsonl"""
    transcripts = list(BRAIN_DIR.glob("*/.system_generated/logs/transcript_full.jsonl"))
    if not transcripts:
        return None
    return max(transcripts, key=lambda p: p.stat().st_mtime)

def run_agy(prompt):
    """Run agy --print and extract response from transcript"""
    # Snapshot transcripts before
    before = set(BRAIN_DIR.glob("*/.system_generated/logs/transcript_full.jsonl"))
    before_lines = {}
    for t in before:
        try:
            before_lines[str(t)] = len(t.read_text(encoding='utf-8', errors='ignore').strip().split('\n'))
        except:
            before_lines[str(t)] = 0

    # Run agy
    cmd = [AGY, "--print", "--dangerously-skip-permissions", prompt]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120, 
                          env={**os.environ, 'TERM': 'dumb', 'COLUMNS': '200', 'LINES': '50'})
    
    # Wait a moment for filesystem to sync
    time.sleep(2)
    
    # Find the transcript with new lines
    after = set(BRAIN_DIR.glob("*/.system_generated/logs/transcript_full.jsonl"))
    latest = get_latest_transcript()
    
    if not latest:
        return f"ERROR: No transcript found. stdout={proc.stdout}, stderr={proc.stderr}"
    
    # Read the latest transcript and find MODEL responses
    try:
        lines = latest.read_text(encoding='utf-8', errors='ignore').strip().split('\n')
        model_responses = []
        for line in lines:
            try:
                entry = json.loads(line)
                if entry.get('source') == 'MODEL' and entry.get('type') == 'PLANNER_RESPONSE':
                    content = entry.get('content', '')
                    if content:
                        model_responses.append(content)
            except json.JSONDecodeError:
                continue
        
        if model_responses:
            return model_responses[-1]  # Return the last MODEL response
        else:
            return f"ERROR: No MODEL response in transcript. Checked {len(lines)} lines."
    except Exception as e:
        return f"ERROR reading transcript: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python agy_wrapper.py 'your prompt'")
        sys.exit(1)
    
    prompt = sys.argv[1]
    result = run_agy(prompt)
    print(result)
