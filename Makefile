# Makefile for Edison V3 CLI Project

# Variables
MICROPYTHON_VERSION = 1.27.0
MICROPYTHON_TARBALL = micropython-$(MICROPYTHON_VERSION).tar.xz
MICROPYTHON_DIR = micropython-$(MICROPYTHON_VERSION)
MICROPYTHON_URL = https://micropython.org/resources/source/$(MICROPYTHON_TARBALL)
MPY_CROSS = $(MICROPYTHON_DIR)/mpy-cross/build/mpy-cross

# Default target
all: $(MPY_CROSS)

# Target to build mpy-cross
$(MPY_CROSS): $(MICROPYTHON_DIR)/mpy-cross/Makefile
	$(MAKE) -C $(MICROPYTHON_DIR)/mpy-cross

$(MICROPYTHON_DIR)/mpy-cross/Makefile: $(MICROPYTHON_DIR)/Makefile
	@# This is just a dependency, the tarball extraction creates this file.

$(MICROPYTHON_DIR)/Makefile: $(MICROPYTHON_TARBALL)
	tar -xf $(MICROPYTHON_TARBALL)

$(MICROPYTHON_TARBALL):
	curl -L -o $(MICROPYTHON_TARBALL) $(MICROPYTHON_URL)

# Phony targets
.PHONY: all clean

# Target to clean up built files
clean:
	rm -rf $(MICROPYTHON_DIR) $(MICROPYTHON_TARBALL)
	find . -name "*.mpy" -delete
