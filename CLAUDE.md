# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LeetCode-style interview practice problems in Python. Solutions are written as standalone functions in `main.py` with a `main()` entry point that runs test cases.

## Setup & Running

- **Python version:** 3.13 (managed by `uv`)
- **Package manager:** [uv](https://docs.astral.sh/uv/) — uses `pyproject.toml` and `uv.lock`
- **Run:** `uv run python main.py`
- **No test framework or linter configured**

## Conventions

- Solutions are self-contained functions in `main.py` with test inputs hardcoded in `main()`.
- Functions are standalone (not class methods) — do not use `self` parameters.
