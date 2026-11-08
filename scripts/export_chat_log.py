"""Export only user/public assistant messages from one explicitly selected session."""
import argparse
import json
import os
import re
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / ".git" / "chat-log"
VN = timezone(timedelta(hours=7))


def write_changed(path, text):
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(text, encoding="utf-8", newline="\n")
    temp.replace(path)


def read_messages(source):
    records = []
    session_id = None
    lines = source.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            if index == len(lines) - 1:
                break  # The active app may still be writing its final line.
            raise
        payload = row.get("payload", {})
        if row.get("type") == "session_meta":
            session_id = payload["id"]
        if row.get("type") != "response_item" or payload.get("type") != "message":
            continue
        role = payload.get("role")
        if role not in ("user", "assistant"):
            continue
        if payload.get("channel") not in (None, "final", "commentary"):
            continue
        parts = payload.get("content", [])
        texts = [p["text"] for p in parts if p.get("type") in ("input_text", "output_text", "text")]
        if not texts:
            continue
        stamp = row["timestamp"]
        text = "\n".join(texts)
        context = role == "user" and text.startswith(("<environment_context>", "<external_codex_apps_"))
        records.append({"session_id": session_id, "source_line": index + 1,
                        "timestamp_utc": stamp,
                        "timestamp_vn": datetime.fromisoformat(stamp.replace("Z", "+00:00")).astimezone(VN).isoformat(),
                        "role": role, "kind": "app_context" if context else "chat",
                        "tool": "OpenAI Codex", "text": text,
                        "non_text_content_types": [p.get("type") for p in parts if "text" not in p]})
    if not session_id:
        raise ValueError("Selected file has no session ID")
    return session_id, records


def fenced(text):
    longest = max((len(m.group()) for m in re.finditer(r"`+", text)), default=0)
    fence = "`" * max(3, longest + 1)
    return fence + "text\n" + text + "\n" + fence


def sync(source):
    session_id, current = read_messages(source)
    raw_path = STATE / "messages.jsonl"
    previous = [json.loads(line) for line in raw_path.read_text(encoding="utf-8").splitlines()] if raw_path.exists() else []
    # Keep other explicitly imported sessions; replace this session with its actual source.
    records = [r for r in previous if r["session_id"] != session_id] + current
    records.sort(key=lambda r: (r["timestamp_utc"], r["session_id"], r["source_line"]))
    write_changed(raw_path, "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records))
    interactions = []
    for r in records:
        if r["kind"] == "app_context":
            continue
        if r["role"] == "user":
            interactions.append({"prompt": r, "outputs": []})
        elif interactions:
            interactions[-1]["outputs"].append(r["text"])
    output = ["# Prompt log\n"]
    for number, interaction in enumerate(interactions, 1):
        prompt = interaction["prompt"]
        stamp = datetime.fromisoformat(prompt["timestamp_vn"]).strftime("%d/%m/%Y %H:%M:%S")
        output.append(f"## {number}\n\nTool: {prompt['tool']}\n\nThời gian: {stamp} (UTC+07:00)\n\n"
                      "### Prompt\n\n" + fenced(prompt["text"]) + "\n\n"
                      "### Output\n\n" + fenced("\n\n".join(interaction["outputs"])) + "\n")
    rendered = "\n".join(output)
    write_changed(ROOT / "prompt_log.md", rendered)
    return rendered


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--session", type=Path)
    parser.add_argument("--follow", action="store_true")
    parser.add_argument("--idle-seconds", type=int, default=1800)
    args = parser.parse_args()
    STATE.mkdir(parents=True, exist_ok=True)
    config = STATE / "chat_log.json"
    if args.session:
        source = args.session.resolve(strict=True)
        config.write_text(json.dumps({"session": str(source)}, ensure_ascii=False), encoding="utf-8")
    elif config.exists():
        source = Path(json.loads(config.read_text(encoding="utf-8"))["session"])
        active = os.environ.get("CODEX_THREAD_ID")
        if active and active not in source.name:
            parser.error("Current chat differs from saved session; pass --session for this chat.")
    else:
        parser.error("First export requires --session pointing to this chat's JSONL file.")
    if not args.follow:
        sync(source)
        print("Exported chat messages.")
        return
    pid_file = STATE / "chat_logger.pid"
    # Exclusive lock prevents concurrent exporters in this repo.
    try:
        pid_file.open("x", encoding="utf-8").write(str(os.getpid()))
    except FileExistsError:
        parser.error("Logger PID file exists; verify the process before removing a stale PID file.")
    try:
        last = None
        changed = time.monotonic()
        while not (STATE / "stop-chat-log").exists():
            rendered = sync(source)
            if rendered != last:
                last = rendered
                changed = time.monotonic()
            if time.monotonic() - changed >= args.idle_seconds:
                break
            time.sleep(2)
    finally:
        pid_file.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
