# Contributing to DevVault

Thanks for your interest in contributing! DevVault is a local search engine
for developer repositories and documentation.

## Getting started

1. Fork this repository and clone your fork:
```bash
   git clone https://github.com/YOUR_USERNAME/devvault.git
   cd devvault
```

2. Create a virtual environment and install dependencies:
```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev]"
```

3. Run the test suite to make sure everything works:
```bash
   pytest
```

## Making a change

1. Create a branch for your change:
```bash
   git checkout -b feature/your-feature-name
```

2. Make your changes, and add or update tests as needed.

3. Run tests locally before pushing:
```bash
   pytest
```

4. Commit with a clear message and push:
```bash
   git commit -m "feat: describe your change"
   git push origin feature/your-feature-name
```

5. Open a Pull Request against `main`. GitHub Actions will automatically
   run the test suite on your PR.

## Code style

- Keep functions small and focused.
- Add a test for any new behavior.
- Prefer clear naming over clever code.

## Project structure