#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${CODEX_HOME:-$HOME/.codex}/skills"

mkdir -p "$TARGET_DIR"
rm -rf "$TARGET_DIR/creative-follow-up-tracker"
cp -R "$ROOT_DIR/skill/creative-follow-up-tracker" "$TARGET_DIR/creative-follow-up-tracker"

echo "Installed creative-follow-up-tracker to $TARGET_DIR/creative-follow-up-tracker"
