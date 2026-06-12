import json
import os
import collections
import re
from datetime import datetime

claude_history_path = r"C:\Users\bonny_chen\.claude\history.jsonl"
codex_history_path = r"C:\Users\bonny_chen\.codex\history.jsonl"

def process_history(file_path, source_name):
    if not os.path.exists(file_path):
        return []
    
    sessions = collections.defaultdict(list)
    total_messages = 0
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                msg = json.loads(line)
                if 'display' in msg and 'sessionId' in msg:
                    session_id = msg['sessionId']
                    text = msg['display']
                    timestamp = msg.get('timestamp', 0)
                    sessions[session_id].append({'text': text, 'time': timestamp})
                    total_messages += 1
            except json.JSONDecodeError:
                pass
                
    results = []
    for session_id, msgs in sessions.items():
        if not msgs: continue
        msgs.sort(key=lambda x: x['time'])
        
        # Basic keyword extraction (very naive)
        combined_text = " ".join([m['text'] for m in msgs]).lower()
        words = re.findall(r'\b[a-z]{4,}\b', combined_text)
        
        # Stop words
        stop_words = {'this', 'that', 'with', 'from', 'your', 'have', 'what', 'code', 'file', 'error', 'please', 'help', 'make', 'just', 'like', 'about', 'some', 'need', 'using', 'will', 'there', 'when', 'into', 'would', 'also', 'then', 'than', 'could', 'were', 'been', 'which', 'their', 'they', 'them', 'these', 'those'}
        words = [w for w in words if w not in stop_words]
        
        common_words = [word for word, count in collections.Counter(words).most_common(5)]
        
        # Try to find a descriptive first message
        first_msg = msgs[0]['text'][:100].replace('\n', ' ')
        
        results.append({
            'source': source_name,
            'session_id': session_id,
            'msg_count': len(msgs),
            'start_time': datetime.fromtimestamp(msgs[0]['time']/1000).strftime('%Y-%m-%d %H:%M') if msgs[0]['time'] else "Unknown",
            'first_msg': first_msg,
            'keywords': common_words,
            'combined_text': combined_text # Keep for deeper analysis if needed
        })
        
    return results, total_messages

print("Scanning histories...")
claude_sessions, claude_count = process_history(claude_history_path, "Claude")
codex_sessions, codex_count = process_history(codex_history_path, "Codex")

all_sessions = claude_sessions + codex_sessions
all_sessions.sort(key=lambda x: x['msg_count'], reverse=True)

# Generate Markdown Report
report_path = r"C:\Users\bonny_chen\LLM-Wiki\wiki\logs\ai-history-audit-report.md"

with open(report_path, 'w', encoding='utf-8') as f:
    f.write("---\n")
    f.write("type: log\n")
    f.write("status: active\n")
    f.write(f"created: {datetime.now().strftime('%Y-%m-%d')}\n")
    f.write("tags: [log, audit, ingestion]\n")
    f.write("---\n\n")
    f.write("# AI History Audit Report\n\n")
    f.write("## Overview\n")
    f.write(f"- **Claude Messages Processed:** {claude_count}\n")
    f.write(f"- **Codex Messages Processed:** {codex_count}\n")
    f.write(f"- **Total Distinct Sessions:** {len(all_sessions)}\n\n")
    
    f.write("## Top 20 Longest Sessions (High Value Extraction Targets)\n\n")
    for s in all_sessions[:20]:
        f.write(f"### Session `{s['session_id'][:8]}...` ({s['source']})\n")
        f.write(f"- **Date:** {s['start_time']}\n")
        f.write(f"- **Message Count:** {s['msg_count']} messages\n")
        f.write(f"- **Extracted Keywords:** {', '.join(s['keywords'])}\n")
        f.write(f"- **First Message Preview:** `{s['first_msg']}...`\n\n")

print(f"Audit complete. Report saved to {report_path}")
