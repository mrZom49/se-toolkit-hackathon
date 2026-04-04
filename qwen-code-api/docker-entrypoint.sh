#!/bin/sh
set -e

# Copy mounted Qwen credentials (read-only) to nonroot-user-owned directory.
MOUNT_DIR="/mnt/qwen-creds"
TARGET_DIR="/home/nonroot/.qwen"

if [ -d "$MOUNT_DIR" ]; then
  cp -a "$MOUNT_DIR"/. "$TARGET_DIR"/
  chown -R nonroot:nonroot "$TARGET_DIR"
fi

# Drop to non-root user and exec the CMD
exec gosu nonroot "$@"
