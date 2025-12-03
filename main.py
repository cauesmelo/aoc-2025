#!/usr/bin/env python
"""Run and watch Advent of Code solutions."""

import argparse
import subprocess
import sys
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class RerunHandler(FileSystemEventHandler):
    """Handler that reruns the solution on file changes."""

    def __init__(self, day: int):
        self.day = day
        self.last_run = 0
        self.debounce = 0.5  # seconds

    def on_any_event(self, event):
        if event.is_directory:
            return

        # Debounce rapid events
        now = time.time()
        if now - self.last_run < self.debounce:
            return
        self.last_run = now

        print("\n" + "=" * 50)
        print(f"Change detected: {event.src_path}")
        print("=" * 50 + "\n")
        run_day(self.day)


def run_day(day: int):
    """Run the solution for a given day."""
    module_name = f"aoc.day{day:02d}.solution"
    try:
        subprocess.run(
            [sys.executable, "-m", module_name],
            cwd=Path(__file__).parent,
        )
    except Exception as e:
        print(f"Error running day {day}: {e}")


def watch_day(day: int):
    """Watch for changes and rerun the solution."""
    day_path = Path(__file__).parent / "aoc" / f"day{day:02d}"
    utils_path = Path(__file__).parent / "aoc" / "utils.py"

    if not day_path.exists():
        print(f"Error: {day_path} does not exist")
        sys.exit(1)

    print(f"Watching day {day:02d} for changes...")
    print(f"  {day_path}")
    print(f"  {utils_path}")
    print("\nPress Ctrl+C to stop.\n")
    print("=" * 50 + "\n")

    # Initial run
    run_day(day)

    # Set up observer
    handler = RerunHandler(day)
    observer = Observer()
    observer.schedule(handler, str(day_path), recursive=True)
    observer.schedule(handler, str(utils_path.parent), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopped watching.")
    observer.join()


def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions")
    parser.add_argument(
        "-d", "--day", type=int, required=True, help="Day number (1-12)"
    )
    parser.add_argument(
        "-w", "--watch", action="store_true", help="Watch for changes and rerun"
    )
    args = parser.parse_args()

    if not 1 <= args.day <= 12:
        print("Error: Day must be between 1 and 12")
        sys.exit(1)

    if args.watch:
        watch_day(args.day)
    else:
        run_day(args.day)


if __name__ == "__main__":
    main()
