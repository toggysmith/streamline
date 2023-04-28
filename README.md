<h1 align="center">Streamline</h1>
<p align="center">A command-line project generation tool for streamlining the creation of new CMake-based C++ projects.</p>

# Overview

**Streamline** is a C++ project generation tool that can be run on the command-line to quickly set up new C++ projects.

It automatically generates new projects according to [The Pitchfork Layout](https://github.com/vector-of-bool/pitchfork) and makes testing and documentation generation easier.

# Run locally

Install [CMake](https://cmake.org/). You will need a version >= 3.24.

Install Python.

Install Doxygen. This is only necessary if you want to generate documentation.

Clone the repository:

```bash
git clone https://github.com/toggysmith/streamline
```

Go to the project directory:

```bash
cd streamline
```

Install the required dependencies:

```bash
pip install requirements.txt
```

Place `streamline.py` wherever you would like to keep it. You can use it without putting it in your path.

Alternatively, with zshrc you could create a PATH alias by adding the following to `~/.zshrc`:

```
alias streamline='python [location]/streamline.py'
```

where `[location]` is the directory where you placed `streamline.py`.

# Usage examples

## Creating new projects

**To create a new project with the same name as the parent directory:**

```bash
streamline init
```

**To create a new project with a specific name:**

```bash
streamline init --name hello-world
```

**To create a new project that uses a specific C++ version (the default is 17):**

```bash
streamline init --edition 14
```

**To create a new project with unit testing via Google Test:**

```bash
streamline init --tests gtest
```

**To create a new project with documentation generation via Doxygen:**

```bash
streamline init --docs doxygen
```

## Building a project

**To build a project in debug mode implicitly:**

```bash
streamline build
```

**To build a project in debug mode explicitly:**

```bash
streamline build --debug
```

**To build a project in release mode:**

```bash
streamline build --release
```

## Running a project

**To run a project (creates a debug build):**

```bash
streamline run
```

## Generating documentation and running tests

**To run tests (provided a testing framework was set up and tests exist):**

```bash
streamline test
```

**To generate HTML documentation (provided a documentation generator was set up):**

```bash
streamline docs
```

**To generate and open HTML documentation in the default browser:**

```bash
streamline docs --open
```

# Demo

https://user-images.githubusercontent.com/61121030/235254835-e15898c8-a5c0-42f2-b4bc-82f583983341.mov

# Motivation

**Streamline** was designed to streamline setting up the following three things:

<picture>
    <source srcset="https://user-images.githubusercontent.com/61121030/235249787-f4990e10-822c-488e-9941-94e0782083d9.png" media="(prefers-color-scheme: dark)" />
    <source srcset="https://user-images.githubusercontent.com/61121030/235249968-86312181-365d-432a-b722-cd8424f68601.png" media="(prefers-color-scheme: light)" />
    <img src="https://user-images.githubusercontent.com/61121030/235249968-86312181-365d-432a-b722-cd8424f68601.png" align="center" />
</picture>

<br />

<a href="https://toggysmith.com">
  <picture>
    <source srcset="https://user-images.githubusercontent.com/61121030/234412163-6027c7f8-ffbe-4ebb-b83b-c8ce1941c5b4.png" media="(prefers-color-scheme: dark)" />
    <source srcset="https://user-images.githubusercontent.com/61121030/234409401-6c9037df-566d-4649-a5cc-12782ada38b5.png" media="(prefers-color-scheme: light)" />
    <img src="https://user-images.githubusercontent.com/61121030/234409401-6c9037df-566d-4649-a5cc-12782ada38b5.png" width="200" align="right" />
  </picture>
</a>
