#!/usr/bin/env bash
# Casa Soda — team machine setup
# Installs/updates all Casa Soda Claude Code skills as symlinks and makes sure
# nvm + the Node versions our projects need are available.
# Safe to re-run any time — it's idempotent and only touches the skills it manages.
#
# Usage:
#   bash setup.sh          # install/update everything
#   bash setup.sh --help   # print the quick-reference help and exit

set -u

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$HOME/.claude/skills"
COMMANDS_DIR="$HOME/.claude/commands"

# name-in-claude → file-in-repo
MANAGED_SKILLS=(
  "soda-front:prompting-guide.md"
  "soda-finsera:soda-finsera.md"
  "soda-yardzen:soda-yardzen.md"
  "soda-fawnroad:soda-fawnroad.md"
  "soda-help:soda-help.md"
  "soda-quote:soda-quote.md"
  "soda-ops:soda-ops.md"
  "screens:screens.md"
)

print_help() {
  cat <<'EOF'
Casa Soda — quick reference

  Skills (type these in Claude Code):
    /soda-front      Dan's Frontend Bible — load in EVERY session
    /soda-finsera    Finsera project guide (dashboard, thematic-baskets)
    /soda-yardzen    Yardzen project guide (build-marketplace, sandboxes)
    /soda-fawnroad   Fawnroad project guide (apps/web)
    /soda-help       This quick reference, inside Claude Code
    /screens         Screenshot QA at fixed viewports
    /soda-quote      Client quotes and pricing

  Dev servers:
    Finsera            nvm use 20.19.6 && yarn start          → localhost:3000 / 3002
    Yardzen            nvm use 24.0.0  && npx nx serve build-marketplace  → localhost:4200
    Fawnroad           nvm use 24.0.0  && cd apps/web && npm run dev:start → localhost:8888

  Update everything:
    cd ~/projects/soda/skills && git pull && bash setup.sh

  Stuck? Copy the red error text and paste it into Claude. Still stuck? Ask Dan.
EOF
}

if [ "${1:-}" = "--help" ] || [ "${1:-}" = "-h" ]; then
  print_help
  exit 0
fi

echo "Casa Soda setup — $REPO_DIR"
echo

# ── 1. Self-update ────────────────────────────────────────────────────────────
if git -C "$REPO_DIR" pull --ff-only >/dev/null 2>&1; then
  echo "✓ Skills repo up to date"
else
  echo "⚠ Could not pull latest skills (offline or local changes) — continuing with what's here"
fi

# ── 2. Symlink all managed skills ─────────────────────────────────────────────
mkdir -p "$SKILLS_DIR" "$COMMANDS_DIR"
linked=0
for entry in "${MANAGED_SKILLS[@]}"; do
  name="${entry%%:*}"
  file="${entry#*:}"
  target="$REPO_DIR/$file"
  if [ ! -f "$target" ]; then
    echo "⚠ Skipping $name — $file not found in repo"
    continue
  fi
  for dir in "$SKILLS_DIR" "$COMMANDS_DIR"; do
    link="$dir/$name.md"
    # Replace plain files and stale/old symlinks alike (this migrates old setups)
    if [ -e "$link" ] || [ -L "$link" ]; then
      rm -f "$link"
    fi
    ln -s "$target" "$link"
  done
  linked=$((linked + 1))
done
echo "✓ Linked $linked skills into ~/.claude/skills and ~/.claude/commands"

# ── 3. nvm + Node versions ────────────────────────────────────────────────────
export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
if [ ! -s "$NVM_DIR/nvm.sh" ]; then
  echo "Installing nvm..."
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
  export NVM_DIR="$HOME/.nvm"
fi

if [ -s "$NVM_DIR/nvm.sh" ]; then
  # shellcheck disable=SC1091
  . "$NVM_DIR/nvm.sh"
  for version in 24.0.0 20.19.6; do
    if nvm ls "$version" >/dev/null 2>&1; then
      echo "✓ Node $version already installed"
    else
      echo "Installing Node $version..."
      nvm install "$version" >/dev/null
      echo "✓ Node $version installed"
    fi
  done
  nvm alias default 24.0.0 >/dev/null 2>&1 && echo "✓ Default Node: 24.0.0 (Finsera uses 20.19.6 — nvm use 20.19.6)"
else
  echo "⚠ nvm not available — install it manually: https://github.com/nvm-sh/nvm"
fi

echo
echo "Done. Open Claude Code in any project and type /soda-front to start."
echo "Run 'bash setup.sh --help' any time for the quick reference."
