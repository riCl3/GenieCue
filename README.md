# MovieRecommendation
# GenieCue: A Versatile Cue Management System

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

**GenieCue** is a Python-based cue management system designed to simplify and streamline the process of handling cues, particularly in live performance settings like theater, presentations, and events. It provides a simple, extensible framework for defining, managing, and executing cues with ease.

## Introduction

Managing cues during a live performance can be challenging. GenieCue aims to alleviate this burden by offering a structured and flexible approach. Whether you're a seasoned professional or a beginner, GenieCue's intuitive design makes it easy to integrate into your workflow.

This project is built with simplicity and extensibility in mind. You can define various types of cues, manage their execution, and even extend the system with custom cue types to suit your specific needs.

## Features

* **Simple Cue Definition:** Easily define cues with clear parameters and actions.
* **Extensible Architecture:** Add custom cue types to handle unique requirements.
* **Sequential Execution:** Execute cues in a predefined order.
* **Flexible Timing:** Implement delays and other timing-based actions.
* **Clear Logging:** Provides feedback and logging for debugging and monitoring.
* **Beginner Friendly:** Designed to be easy to understand and use.

## Getting Started

### Prerequisites

* Python 3.7 or later

### Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/riCl3/GenieCue.git](https://www.google.com/search?q=https://github.com/riCl3/GenieCue.git)
    cd GenieCue
    ```

2.  (Optional) Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install dependencies (if any, as this project is very simple currently):

    ```bash
    # If there are any dependencies listed in a requirements.txt file, install them with:
    # pip install -r requirements.txt
    ```

### Basic Usage

1.  **Define Cues:** Create cue definitions in your Python script. For example, you might create cues to print messages, control external devices, or execute other actions.
2.  **Manage Cues:** Use the provided cue management functions to add, modify, and execute cues.
3.  **Run Cues:** Execute the cues in your desired sequence.# geniecue.py
import time
from typing import Callable, List

class Cue:
    """
    Represents a single cue with an action to execute.
    """
    def __init__(self, action: Callable[[], None]):
        self.action = action

    def execute(self):
        """
        Executes the cue's action.
        """
        self.action()

class CueManager:
    """
    Manages a sequence of cues and executes them.
    """
    def __init__(self):
        self.cues: List[Cue] = []

    def add_cue(self, cue: Cue):
        """
        Adds a cue to the cue manager.
        """
        self.cues.append(cue)

    def run_cues(self):
        """
        Executes all cues in the order they were added.
        """
        for cue in self.cues:
            cue.execute()

# custom_cue.py (example of extending)
class DelayedMessageCue(Cue):
    def __init__(self, message, delay):
        super().__init__(action=self.delayed_print)
        self.message = message
        self.delay = delay

    def delayed_print(self):
        time.sleep(self.delay)
        print(self.message)

# example_usage.py (example of usage)
def print_message(message):
    print(message)

cue1 = Cue(action=lambda: print_message("Cue 1: Hello!"))
cue2 = Cue(action=lambda: print_message("Cue 2: This is a test."))

manager = CueManager()
manager.add_cue(cue1)
manager.add_cue(cue2)

manager.run_cues()

# example of custom cue usage
manager_custom = CueManager()
delayed_cue = DelayedMessageCue("Delayed message!", 2)
manager_custom.add_cue(delayed_cue)
manager_custom.run_cues()

### Example

Here's a basic example to illustrate how to use GenieCue:

```python
# example_usage.py
from geniecue import Cue, CueManager

def print_message(message):
    print(message)

cue1 = Cue(action=lambda: print_message("Cue 1: Hello!"))
cue2 = Cue(action=lambda: print_message("Cue 2: This is a test."))

manager = CueManager()
manager.add_cue(cue1)
manager.add_cue(cue2)

manager.run_cues()
