import subprocess
import sys

def clean_commit_history():
    commands = [
        'git checkout --orphan latest_branch',
        'git add -A',
        'git commit -am "Initial commit"',
        'git branch -D main',
        'git branch -m main',
        'git push --set-upstream origin main -f'
    ]

    for cmd in commands:
        process = subprocess.run(cmd, shell=True, check=True)
        if process.returncode != 0:
            print(f'Command failed: {cmd}', file=sys.stderr)
            sys.exit(1)

def main():
    print("Cleaning Git commit history...")
    clean_commit_history()
    print("Done. Git commit history is cleaned.")

if __name__ == '__main__':
    main()
