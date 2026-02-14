# lore: Edison V3 MicroPython CLI Tool

<p align="center">
  <img src="edison_v3.png" width="240">
  <img src="lore.png" width="240">
</p>

**lore** is a command-line utility for interacting with the Edison V3 robot, providing an enhanced development workflow for MicroPython programs. It allows you to build and flash your programs to the Edison V3 directly from your local filesystem.

For more information about the Edison V3 robot, you can visit the official resource page: [Edison V3.0 Robot](https://www.geyerinstructional.com/edison-v3-0-robot-edpack).

## Features

Traditionally, programming the Edison V3 robot often involves using web-based interfaces like [https://www.edpyapp.com/](https://www.edpyapp.com/) or [https://www.edscratchapp.com/](https://www.edscratchapp.com/). These platforms typically rely on remote APIs to compile your code.

`lore` enhances the development experience by providing:

*   **Local Development Workflow:** Write MicroPython code in a local editor and manage your projects directly on your machine.
*   **Command-Line Uploads:** Upload code to the robot directly from your terminal, bypassing the need to interact with web interfaces for flashing.
*   **Facilitation of AI-Assisted Coding:** The tight feedback loop, without manual copy-pasting, creates an environment for using AI-assisted coding tools like Gemini, Claude Code, Cortex Code, and Codex to write and iterate on code for the Edison robot.
*   **Choice of Compilation Method:** `lore` defaults to using the official remote Edison API for compilation (which requires an internet connection). It also offers an **experimental** `--local-compile` option for offline compilation using `mpy-cross`.

## Future Work

A LOGO to EdPy transpiler is in development. It will translate programs written in the LOGO language into EdPy (MicroPython) for execution on the Edison robot.

## Getting Started

To use `lore`, follow these steps:

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

4.  **Build Your Application**: By default, `lore` uses the official remote Edison API for compilation. This requires an internet connection.

    ```bash
    ./lore build <your_app_name>
    ```
    For example:
    ```bash
    ./lore build nursery_rhymes
    ```

    ### Experimental Local Compilation

    Local compilation using `mpy-cross` is an **experimental** feature. The locally compiled `.mpy` files use a different qstr encoding than the remote compiler (full string names vs. pre-defined firmware qstr IDs), and have not yet been validated on robot hardware.

    `lore` includes a local EdPy validator that checks for unsupported features (floats, strings, lists, dicts, tuples, non-Ed imports, try/except, classes) before compilation, matching the remote compiler's restrictions.

    To use local compilation, you must first build `mpy-cross`:

    ```bash
    make
    ```

    **Note:** `make` will download and build MicroPython 1.27.0 (requires a C compiler).

    Then compile locally:

    ```bash
    ./lore build <your_app_name> --local-compile
    ```

5.  **Flash Your Application**: Transfer the compiled `.mpy` application to your Edison V3 robot:

    ```bash
    ./lore flash <your_app_name>
    ```
    For example:
    ```bash
    ./lore flash nursery_rhymes
    ```