# NerFW

[![Code check](https://github.com/Nergan123/NerFW/actions/workflows/Checks.yml/badge.svg)](https://github.com/Nergan123/NerFW/actions/workflows/Checks.yml)
[![Qodana](https://github.com/Nergan123/NerFW/actions/workflows/qodana_code_quality.yml/badge.svg)](https://github.com/Nergan123/NerFW/actions/workflows/qodana_code_quality.yml)
[![Test Coverage](https://github.com/Nergan123/NerFW/blob/Development_branch/tests/coverage.svg)](https://github.com/Nergan123/NerFW/actions/workflows/test_coverage.yml)

created by Nergan


## Table of contents

1. [Table of contents](#table-of-contents)
2. [About](#about)
3. [Classes and functions](#classes-and-functions)
   1) [NerFW](#nerfw-1)
   2) [Character](#character)


## About

NerFW *(Nergans FrameWork)* is a framework for visual novel creation. This framework
is created in an attempt to make creation of visual novels more convenient for game developers,
and at the same time to make the game harder to pirate. 

NerFW is based on Flask. And is creating a server which hosts the game for you.


## Classes and functions

NerFW is a fully OOP framework and heavily relies on classes.

### NerFW

Main class which creates a server and hosts the game.

| **Name**         | **Description**                           | **Example**                                                        |
|:-----------------|:------------------------------------------|--------------------------------------------------------------------|
| run              | Compiles a game object. Launches a server | run(debug=False)                                                   |
| create_character | Returns a character object                | create_character("Tester", "test_files/test.jpg", (100, 255, 255)) |

### Character

Class which stores character data. Responsible for actions taken by character

| **Name** | **Description**                          | **Example**     |
|:---------|:-----------------------------------------|:----------------|
| say      | Adds a character line to the game script | say("Test 123") |

### Ui

Class for UI creation

| **Name**   | **Description**                 | **Example**                                     |
|:-----------|:--------------------------------|:------------------------------------------------|
| add_button | Creates a new button for the ui | add_button("next", (10, 10), Functions.FORWARD) |
