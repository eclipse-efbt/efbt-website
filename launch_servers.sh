#!/bin/bash

# Script to launch HTTP servers for each theme worktree on different ports

# Base port number
BASE_PORT=8000

# Array of theme directories
THEMES=(
    "theme-monokai"
    "theme-nord"
    "theme-ocean"
    "theme-solarized"
)

# Function to cleanup background processes on script exit
cleanup() {
    echo ""
    echo "Stopping all servers..."
    jobs -p | xargs -r kill
    exit 0
}

# Set trap to cleanup on Ctrl+C
trap cleanup SIGINT SIGTERM

echo "Starting HTTP servers for each theme worktree..."
echo "======================================"

# Start server for each theme
for i in "${!THEMES[@]}"; do
    theme="${THEMES[$i]}"
    port=$((BASE_PORT + i))

    if [ -d "worktrees/$theme" ]; then
        echo "Starting server for $theme on port $port"
        echo "URL: http://localhost:$port"

        # Start Python HTTP server in background
        (cd "worktrees/$theme" && python3 -m http.server $port) > /dev/null 2>&1 &

        # Store the PID for later cleanup
        echo "Server PID: $!"

        echo "--------------------"
    else
        echo "Warning: Directory worktrees/$theme not found"
    fi
done

echo ""
echo "All servers started. URLs:"
for i in "${!THEMES[@]}"; do
    theme="${THEMES[$i]}"
    port=$((BASE_PORT + i))
    echo "  $theme: http://localhost:$port"
done

echo ""
echo "Press Ctrl+C to stop all servers"

# Keep script running
wait
