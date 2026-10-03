"""Env Merge Files — Merge two .env files with last-wins or first-wins and write a sorted result."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='env_merge_files',
        description='Merge two .env files with last-wins or first-wins and write a sorted result.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Env Merge Files')
    print('A .env.example plus overrides, one file.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
