# Project Plan & TODOs

This document outlines the development plan and tasks for the `lore` project.

## Phase 1: Core Functionality (Completed)

- [x] Reverse-engineer the Edison V3 WebUSB protocol.
- [x] Create a Python CLI tool (`lore`) for flashing compiled MicroPython code.
- [x] Implement local `mpy-cross` build process via `Makefile`.
- [x] Implement remote compilation via the official EdPy API.
- [x] Refactor `lore` to use `build` and `flash` subcommands.
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

The goal of this phase was to make the `--local-compile` feature robust and reliable.

- [x] **Verify `mpy-cross` Compatibility:**
    - [x] MicroPython 1.27.0 `mpy-cross` produces mpy v6 format with 31-bit small ints — matching the remote compiler's header.
    - [x] Local output is functionally equivalent to remote (same bytecode, different qstr encoding — local embeds full string names, remote uses pre-defined firmware qstr IDs).
    - [x] Added `-s main.py` flag to normalize embedded source filename.
    - [x] All 7 LOGO test apps compile successfully with both remote and local compilers.

- [x] **Define the EdPy Python Subset:**
    - [x] Created `apps/edpy_test_loops` — `for`, `while`, `range()`, nested loops. Pass (both compilers).
    - [x] Created `apps/edpy_test_conditionals` — `if`/`elif`/`else`, comparison operators. Pass (both compilers).
    - [x] Created `apps/edpy_test_functions` — `def`, `return`, parameters, recursion. Pass (both compilers).
    - [x] Created `apps/edpy_test_variables` — assignment, arithmetic, `abs()`. Pass (both compilers).
    - [x] Created `apps/edpy_test_unsupported` — strings, floats, lists, dicts, imports. Remote rejects (e.g., "constant 3.14 must be an integer value"); local mpy-cross accepts (no EdPy-specific validation).

- [x] **Improve Local Compilation Error Handling:**
    - [x] `mpy-cross` reports syntax errors to stderr in `File "path", line N / SyntaxError: message` format.
    - [x] Updated `compile_app()` to capture stderr via `capture_output=True` and display formatted errors.
    - [x] Removed "experimental" label from README.md and CLI help text.

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