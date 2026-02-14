# LORE: Edison V3 MicroPython CLI Tool

<p align="center">
  <img src="edison_v3.png" width="240">
  <img src="lore.png" width="240">
</p>

**LORE** is a command-line utility for interacting with the Edison V3 robot, providing an enhanced development workflow for MicroPython programs. It allows you to build and flash your programs to the Edison V3 directly from your local filesystem.

For more information about the Edison V3 robot, you can visit the official resource page: [Edison V3.0 Robot](https://www.geyerinstructional.com/edison-v3-0-robot-edpack).

## Features

Traditionally, programming the Edison V3 robot often involves using web-based interfaces like [https://www.edpyapp.com/](https://www.edpyapp.com/) or [https://www.edscratchapp.com/](https://www.edscratchapp.com/). These platforms typically rely on remote APIs to compile your code.

LORE enhances the development experience by providing:

*   **Local Development Workflow:** Write MicroPython code in a local editor and manage your projects directly on your machine.
*   **Command-Line Uploads:** Upload code to the robot directly from your terminal, bypassing the need to interact with web interfaces for flashing.
*   **Facilitation of AI-Assisted Coding:** The tight feedback loop, without manual copy-pasting, creates an environment for using AI-assisted coding tools like Gemini, Claude Code, Cortex Code, and Codex to write and iterate on code for the Edison robot.
*   **Offline Compilation:** LORE compiles locally using `mpy-cross`, producing **byte-identical** output to the official remote Edison API. No internet connection required. The local pipeline includes an EdPy validator (rejects unsupported features like floats, strings, and lists), constant inlining, and a qstr remapper that matches the Edison firmware's internal string table. Remote compilation via the Edison API is available with `--remote-compile`.

## Getting Started

To use LORE, follow these steps:

1.  **Activate Virtual Environment**: It is recommended to work within a Python virtual environment. To create one:

    ```bash
    python3 -m venv .venv
    ```

    Then activate it:

    ```bash
    source .venv/bin/activate
    ```

2.  **Install Dependencies**: Install the necessary Python libraries:

    ```bash
    pip install pyusb requests lark
    ```

3.  **Create Your Application**: Place your MicroPython `.py` files within the `apps/<your_app_name>/` directory. For example, `apps/line_following/main.py`.

4.  **Build Your Application**: Before your first build, compile `mpy-cross`:

    ```bash
    make
    ```

    **Note:** `make` will download and build MicroPython 1.27.0 (requires a C compiler).

    Then build your application:

    ```bash
    ./lore build <your_app_name>
    ```
    For example:
    ```bash
    ./lore build nursery_rhymes
    ```

    ### Remote Compilation

    If you prefer to use the official Edison API (requires an internet connection):

    ```bash
    ./lore build <your_app_name> --remote-compile
    ```

5.  **Flash Your Application**: Transfer the compiled `.mpy` application to your Edison V3 robot:

    ```bash
    ./lore flash <your_app_name>
    ```
    For example:
    ```bash
    ./lore flash nursery_rhymes
    ```

## Maintaining the Edison Constant and Qstr Tables

The local compiler relies on two reverse-engineered tables embedded in `lore`:

- **`EDISON_CONSTANTS`** — maps `Ed.CONSTANT_NAME` to integer values (e.g., `Ed.FORWARD` = `1`)
- **`EDISON_QSTR_IDS`** — maps string names to the Edison firmware's static qstr IDs (e.g., `"Drive"` = `11`)

These were discovered by probing the remote Edison compiler API at `https://api.edisonrobotics.net/ep/compile/ep_compile_usb_v3`. If Edison releases new firmware with additional API functions or constants, you can discover their values using the same technique.

### Discovering New Constant Values

To find the integer value of an `Ed.CONSTANT`, compile a program that assigns it to a variable and inspect the bytecode. The remote compiler inlines constants as integer literals:

```python
import requests

API = "https://api.edisonrobotics.net/ep/compile/ep_compile_usb_v3"
code = """import Ed
Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM
x = Ed.NEW_CONSTANT
"""
r = requests.post(API, data=code, headers={"Content-Type": "text/plain"})
j = r.json()
if j.get("compile") == False:
    print("Compile error:", j.get("message"))
else:
    # The constant value will appear as an integer literal in the bytecode.
    # Compare the hex output against a version using a known integer to
    # identify where the value is encoded.
    print("hex:", j["hex"])
```

For small values (0-127), the integer appears directly in the bytecode as a `LOAD_CONST_SMALL_INT` operand. For larger values, use two compilations — one with the constant and one with a known integer — and diff the hex output to locate the encoded value.

### Discovering New Qstr IDs

To find the Edison firmware's qstr ID for a new API name, compile a program that uses it and examine the qstr table in the `.mpy` output:

```python
import requests

API = "https://api.edisonrobotics.net/ep/compile/ep_compile_usb_v3"
code = """import Ed
Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM
Ed.NewFunction()
"""
r = requests.post(API, data=code, headers={"Content-Type": "text/plain"})
j = r.json()
if j.get("compile") == False:
    print("Compile error:", j.get("message"))
else:
    mpy = bytes.fromhex(j["hex"])
    # Skip 4-byte header, read n_qstr varint, then decode qstr entries.
    # Static entries are encoded as (id << 1) | 1; the new function's
    # Edison qstr ID will appear here instead of as a dynamic string.
    print("Raw mpy hex:", j["hex"])
```

The qstr table starts at byte offset 4 in the `.mpy` file. Each entry is either a static reference (varint with low bit set, ID = value >> 1) or a dynamic string (varint with low bit clear, length = value >> 1, followed by the string bytes and a NUL terminator). The remote compiler converts Edison API names to static IDs — any unfamiliar static ID in the output is the Edison firmware's qstr ID for the new name.

For a complete working example, see the `probe_qstrs.py` script used during development in the project history.