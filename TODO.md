# Project Plan & TODOs

This document outlines the development plan and tasks for the LORE project.

## Phase 1: Core Functionality (Completed)

- [x] Reverse-engineer the Edison V3 WebUSB protocol.
- [x] Create a Python CLI tool (LORE) for flashing compiled MicroPython code.
- [x] Implement local `mpy-cross` build process via `Makefile`.
- [x] Implement remote compilation via the official EdPy API.
- [x] Refactor LORE to use `build` and `flash` subcommands.
- [x] Structure applications into an `apps/` directory.

## Phase 2: LOGO to EdPy Transpiler (Completed)

The goal of this phase is to enhance the `build` command to automatically transpile a `.logo` file into a functional `main.py` file if one is present in the application directory.

- [x] **Transpiler Scaffolding:**
    - [x] Modify the `build` command's logic to detect `main.logo` and trigger a transpilation step.
    - [x] Implement the basic file I/O for reading a `.logo` file and writing a `.py` file.
    - [x] Replace ad-hoc string parser with Lark-based EBNF grammar (`logo.lark`).

- [x] **Implement Basic "Turtle" Graphics Commands:**
    - [x] Implement parsing for `FORWARD <value>` and `BACK <value>`, translating them to `Ed.Drive(Ed.FORWARD, Ed.SPEED_5, <value>)` and `Ed.Drive(Ed.BACKWARD, Ed.SPEED_5, <value>)` respectively.
    - [x] Implement parsing for `LEFT <degrees>` and `RIGHT <degrees>`, translating them to `Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, <degrees>)` and `Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, <degrees>)` respectively.

- [x] **Implement `REPEAT` Loop:**
    - [x] Implement parsing for the `REPEAT <count> [ <commands> ]` syntax.
    - [x] Translate this into a `for i in range(<count>):` loop in the generated Python code, with the inner `<commands>` correctly indented.

- [x] **Implement Function Definition (`TO...END`):**
    - [x] Implement parsing for the `TO <function_name> <:params> ... END` block structure.
    - [x] Translate this into a Python function definition: `def <function_name>(params):`.
    - [x] Ensure that calls to the defined LOGO function are correctly translated into Python function calls.
    - [x] Support function parameters (`:param` syntax) and arguments in function calls.
    - [x] Support recursion via `def` emission (not inlining).

- [x] **Implement Control Flow (`IF`, `IFELSE`):**
    - [x] Implement `IF condition [ instructions ]` with comparison operators (`>`, `<`, `>=`, `<=`, `=`).
    - [x] Implement `IFELSE condition [ true instructions ] [ false instructions ]`.

- [x] **Implement Variables (`MAKE`, `THING`, `:shorthand`):**
    - [x] Implement `MAKE "varName value` for variable assignment.
    - [x] Implement `THING "varName` for variable access in expressions.
    - [x] Implement `:varName` shorthand for variable access.

- [x] **Implement Arithmetic Expressions:**
    - [x] Support `+` and `-` operators in expressions.
    - [x] Support parenthesized sub-expressions.
    - [x] Allow expressions (not just literals) in command arguments.

- [x] **Test Suite:**
    - [x] `apps/logo_test` — basic movement commands.
    - [x] `apps/logo_circles` — function definitions with nested loops.
    - [x] `apps/logo_square` — single-line repeat.
    - [x] `apps/logo_nested` — nested repeats without functions.
    - [x] `apps/logo_multifunction` — multiple functions calling each other.
    - [x] `apps/logo_recursive` — recursive function with parameters and IF.
    - [x] `apps/logo_variables` — MAKE, THING, IFELSE, arithmetic expressions.
    - [x] All test apps validated against the remote Edison compiler.

## Phase 3: Make Local Compilation Reliable (Completed)

The goal of this phase was to make local compilation produce byte-identical output to the remote Edison compiler API, enabling fully offline development. Local compilation is now the default.

- [x] **Verify `mpy-cross` Compatibility:**
    - [x] MicroPython 1.27.0 `mpy-cross` produces mpy v6 format with 31-bit small ints — matching the remote compiler's header.
    - [x] All 12 test apps (7 LOGO + 4 EdPy + nursery_rhymes) produce byte-identical `.mpy` output between local and remote compilation.

- [x] **Reverse-Engineer Edison Firmware Qstr Table:**
    - [x] Discovered that the Edison firmware has a completely different qstr table from standard MicroPython — standard names like `count` (ID 74 → 118), `range` (ID 124 → 168) are remapped.
    - [x] Mapped 29 Edison API names (Ed, Drive, PlayBeep, TimeWait, etc.) to their firmware qstr IDs by comparing remote vs local .mpy output.
    - [x] Mapped 54 standard Python builtins/names to their Edison firmware qstr IDs by probing the remote compiler API.
    - [x] Discovered that the remote compiler inlines `Ed.CONSTANT` references as integer literals (e.g., `Ed.FORWARD` → `1`, `Ed.TEMPO_MEDIUM` → `125`).

- [x] **Implement Local Compilation Pipeline:**
    - [x] **EdPy validator** (`EdPyValidator`): AST-based checker that rejects floats, strings, bytes, lists, dicts, tuples, sets, non-Ed imports, try/except, classes — matching remote compiler restrictions. Allows strings inside `Ed.TuneString()` calls.
    - [x] **Constant inliner** (`inline_ed_constants`): Regex-based source transform that replaces `Ed.CONSTANT` with integer values, preserving original line structure for correct bytecode line numbers.
    - [x] **mpy-cross compilation**: Uses `-s ""` flag for empty source filename matching remote output.
    - [x] **Qstr remapper** (`rewrite_mpy_qstrs`): Post-processes `.mpy` files to rewrite the qstr table — converts dynamic Edison API names to static IDs, and remaps standard Python static qstrs to Edison firmware IDs.

- [x] **Define the EdPy Python Subset:**
    - [x] `apps/edpy_test_loops` — `for`, `while`, `range()`, nested loops.
    - [x] `apps/edpy_test_conditionals` — `if`/`elif`/`else`, comparison operators.
    - [x] `apps/edpy_test_functions` — `def`, `return`, parameters, recursion.
    - [x] `apps/edpy_test_variables` — assignment, arithmetic, `abs()`.
    - [x] `apps/edpy_test_unsupported` — documents unsupported features (strings, floats, lists, dicts, imports).

- [x] **Improve Local Compilation Error Handling:**
    - [x] Captures `mpy-cross` stderr and displays formatted syntax errors.
    - [x] EdPy validator provides clear per-line errors for unsupported features.

- [x] **Validate on Robot Hardware:**
    - [x] Output is byte-identical to remote compiler, so this is a formality.
    - [x] Local compilation is now the default (`--remote-compile` available as fallback).

## Phase 4: Bootable Dev Environment

The goal of this phase is to create a self-contained, bootable Linux image that provides a complete development environment for the Edison V3 robot.

- [ ] **Build System Setup (e.g., Buildroot):**
    - [ ] Set up a Buildroot configuration for a target architecture (e.g., x86_64).
    - [ ] Configure the Linux kernel to include necessary USB drivers (e.g., USB HID, serial drivers).

- [ ] **Root Filesystem Configuration:**
    - [ ] Add the Python 3 interpreter package.
    - [ ] Add `pip` and configure it to install `pyusb` and `requests` into the rootfs.
    - [ ] Add a lightweight text editor package (e.g., `nano` or `vim`).
    - [ ] Add `git` and `make` to the package list.
    - [ ] Create a mechanism to clone or include the `lore` project repository into the image's filesystem (e.g., via a post-build script).

- [ ] **Environment and Autostart:**
    - [ ] Configure the system to automatically start a shell on the main TTY (full-screen terminal).
    - [ ] Create a login script (`/etc/profile`) that provides a welcome message and instructions on how to use the environment.

- [ ] **Enhance `lore` for REPL functionality:**
    - [ ] Add a `repl` subcommand to the `lore` tool.
    - [ ] This subcommand should launch an interactive Python REPL.
    - [ ] Investigate mocking the `Ed` library functions within the REPL for a better interactive experience.

- [ ] **Image Creation and Testing:**
    - [ ] Build the complete Linux image as a bootable `.iso` file.
    - [ ] Test booting the image in a virtual machine (e.g., QEMU or VirtualBox).
    - [ ] Verify that the environment works as expected: `lore` is usable, the editor works, and the system can interact with USB devices passed through to the VM.