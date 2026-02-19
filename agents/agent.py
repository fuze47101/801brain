import os
import sys
from datetime import datetime

BRAIN_ROOT = os.path.expanduser("~/801brain")
OPENAI_MODEL = "gpt-4.1-mini"

# ===== ROLE DEFINITIONS =====
ROLES = {
    "cfo": "You think in capital efficiency, runway, EBITDA, ROI, risk-adjusted return, and exit valuation.",
    "cto": "You think in systems, infrastructure, scalability, regulatory engineering, and defensibility.",
    "marketing": "You think in hooks, attention, positioning, messaging, distribution, and demand creation.",
    "ops": "You think in execution, logistics, supply chain, and operational efficiency.",
    "general": "You operate as a high-level strategic advisor."
}

# ===== LOAD STRATEGIC MEMORY =====
def load_memory(project):
    memory = ""
    strategy_path = os.path.join(BRAIN_ROOT, "strategy")

    # Load master
    master_file = os.path.join(strategy_path, "master.md")
    if os.path.exists(master_file):
        with open(master_file, "r") as f:
            memory += f.read() + "\n\n"

    # Load project-specific
    project_file = os.path.join(strategy_path, f"{project}.md")
    if os.path.exists(project_file):
        with open(project_file, "r") as f:
            memory += f.read() + "\n\n"

    return memory

# ===== LOAD ACTIVE TASKS =====
def load_tasks(project):
    project_dir = os.path.join(BRAIN_ROOT, "projects", project)
    os.makedirs(project_dir, exist_ok=True)

    task_file = os.path.join(project_dir, "active_tasks.md")
    if os.path.exists(task_file):
        with open(task_file, "r") as f:
            return f.read()

    return ""

# ===== LOAD RECENT PROJECT LOGS =====
def load_recent_logs(project, lines=200):
    log_file = os.path.join(BRAIN_ROOT, "logs", f"{project}_log.md")

    if not os.path.exists(log_file):
        return ""

    with open(log_file, "r") as f:
        content = f.readlines()

    return "".join(content[-lines:])

# ===== LOGGING =====
def log_execution(project, role, request, response):
    logs_dir = os.path.join(BRAIN_ROOT, "logs")
    os.makedirs(logs_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = (
        f"\n\n## {timestamp}\n"
        f"Project: {project}\n"
        f"Role: {role}\n"
        f"Request: {request}\n\n"
        f"Response:\n{response}\n"
    )

    # Global log
    with open(os.path.join(logs_dir, "global_log.md"), "a") as f:
        f.write(entry)

    # Project log
    with open(os.path.join(logs_dir, f"{project}_log.md"), "a") as f:
        f.write(entry)

# ===== CLOUD EXECUTION =====
def run_cloud(prompt):
    from openai import OpenAI
    client = OpenAI()

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt
    )

    return response.output_text

# ===== LOCAL EXECUTION =====
def run_local(prompt):
    import subprocess

    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True,
        text=True
    )

    return result.stdout

# ===== BUILD RESUME PROMPT =====
def build_resume_prompt(project):
    memory = load_memory(project)
    tasks = load_tasks(project)
    recent_logs = load_recent_logs(project)

    return (
        f"You are resuming work on PROJECT: {project}\n\n"
        f"--- STRATEGIC MEMORY ---\n{memory}\n"
        f"--- ACTIVE TASKS ---\n{tasks}\n"
        f"--- RECENT ACTIVITY ---\n{recent_logs}\n\n"
        "Provide:\n"
        "1) Current strategic position\n"
        "2) What was recently worked on\n"
        "3) Immediate next 5 high-leverage actions\n"
        "4) Biggest current risk\n"
    )

# ===== MAIN =====
def main():
    if len(sys.argv) < 4:
        print("Usage:")
        print("  python agent.py <mode> <project> <role> <prompt>")
        print("  python agent.py <mode> <project> resume")
        print("Mode must be: local or cloud")
        sys.exit(1)

    mode = sys.argv[1]
    project = sys.argv[2]
    third = sys.argv[3]

    if mode not in ["local", "cloud"]:
        print("Mode must be: local or cloud")
        sys.exit(1)

    # ===== RESUME MODE =====
    if third == "resume":
        role = "general"
        prompt = build_resume_prompt(project)

        if mode == "cloud":
            output = run_cloud(prompt)
        else:
            output = run_local(prompt)

        print("\n===== RESPONSE =====\n")
        print(output)
        return

    # ===== ROLE MODE =====
    role = third

    if role not in ROLES:
        print(f"Invalid role. Available roles: {', '.join(ROLES.keys())}")
        sys.exit(1)

    if len(sys.argv) < 5:
        print("Missing prompt.")
        sys.exit(1)

    user_input = " ".join(sys.argv[4:])

    memory = load_memory(project)
    tasks = load_tasks(project)
    recent_logs = load_recent_logs(project)

    prompt = (
        f"You are operating in PROJECT: {project}\n\n"
        f"ROLE MODE:\n{ROLES[role]}\n\n"
        f"--- STRATEGIC MEMORY ---\n{memory}\n"
        f"--- ACTIVE TASKS ---\n{tasks}\n"
        f"--- RECENT ACTIVITY ---\n{recent_logs}\n\n"
        f"--- USER REQUEST ---\n{user_input}\n\n"
        "Respond clearly and with structured thinking."
    )

    if mode == "cloud":
        output = run_cloud(prompt)
    else:
        output = run_local(prompt)

    print("\n===== RESPONSE =====\n")
    print(output)

    log_execution(project, role, user_input, output)

if __name__ == "__main__":
    main()
