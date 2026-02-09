# Project Plan & TODOs

This document outlines the development plan and tasks for the `lore` project.

## Phase 1: Core Functionality (Completed)

- [x] Reverse-engineer the Edison V3 WebUSB protocol.
- [x] Create a Python CLI tool (`lore`) for flashing compiled MicroPython code.
- [x] Implement local `mpy-cross` build process via `Makefile`.
- [x] Implement remote compilation via the official EdPy API.
- [x] Refactor `lore` to use `build` and `flash` subcommands.
- [x] Structure applications into an `apps/` directory.

## Phase 2: LOGO to EdPy Transpiler

The goal of this phase is to enhance the `build` command to automatically transpile a `.logo` file into a functional `main.py` file if one is present in the application directory.

- [ ] **Transpiler Scaffolding:**
    - [ ] Modify the `build` command's logic to detect `main.logo` and trigger a transpilation step.
    - [ ] Implement the basic file I/O for reading a `.logo` file and writing a `.py` file.

- [ ] **Implement Basic "Turtle" Graphics Commands:**
    - [ ] Implement parsing for `FORWARD <value>` and `BACK <value>`, translating them to `Ed.Drive(Ed.FORWARD, Ed.SPEED_5, <value>)` and `Ed.Drive(Ed.BACKWARD, Ed.SPEED_5, <value>)` respectively.
    - [ ] Implement parsing for `LEFT <degrees>` and `RIGHT <degrees>`, translating them to `Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, <degrees>)` and `Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, <degrees>)` respectively.

- [ ] **Implement `REPEAT` Loop:**
    - [ ] Implement parsing for the `REPEAT <count> [ <commands> ]` syntax.
    - [ ] Translate this into a `for i in range(<count>):` loop in the generated Python code, with the inner `<commands>` correctly indented.

- [ ] **Implement Function Definition (`TO...END`):**
    - [ ] Implement parsing for the `TO <function_name> ... END` block structure.
    - [ ] Translate this into a Python function definition: `def <function_name>():`.
    - [ ] Ensure that calls to the defined LOGO function are correctly translated into Python function calls.
    - [ ] Consider support for arguments in LOGO functions.

## Phase 3: Make Local Compilation Reliable

The goal of this phase is to make the experimental `--local-compile` feature robust and reliable, providing the same level of correctness and feedback as the remote API.

- [ ] **Acquire Compatible `mpy-cross` Version:**
    - [ ] Research MicroPython release history to find a version corresponding to `mpy-cross` v1.2.0.
    - [ ] If found, update the `Makefile` to download and build this specific version.
    - [ ] Test the output of the acquired `mpy-cross` version against the remote API to confirm byte-for-byte compatibility.

- [ ] **Define the EdPy Python Subset:**
    - [ ] Create a suite of small test programs, each exercising a specific Python feature (e.g., list comprehensions, dictionary literals, different loop types, string formatting).
    - [ ] Run each test program against the remote API compiler.
    - [ ] Document which features are supported and which are not, creating a clear "EdPy Language Specification" in the project documentation.

- [ ] **Improve Local Compilation Error Handling:**
    - [ ] Investigate how `mpy-cross` reports syntax errors.
    - [ ] Modify the `compile_app` function in `lore` to capture and parse `stderr` from the `mpy-cross` subprocess.
    - [ ] Format the local compilation errors to be as clear and informative as the JSON-formatted errors from the remote API.

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