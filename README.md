# OPEN-ISSUE-CONTRIBUTION
This repo contains a python written CLI tool called Training. This tool has planted BUGS and features that are missing. So its only purpose is to educate new or old contributors how to make Open Source contributions.
**Fork** it, **Fix** it, Open a pull request and turn your GitHub contribution graph green 🟩

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

## 🎯 What is this?

`Training` is a tiny command line toolbox. It is **deliberately imperfect**: some tools have bugs, some tests are missing and some features are not built yet. Every problem is an open [issue](../../issues) you 
can pick up.

New to open source? This repo is built for you. No experience with big codebases needed.

## 🚀 Make your first contribution in 5 minutes

1. **Pick an issue** with the [`good first issue`](../../labels/good%20first%20issue) label and comment `I'd like to work on this`.
2. **Fork** this repo (top right button) and clone it:
   ```bash
   git clone https://github.com/<your-username>/OPEN-ISSUE-CONTRIBUTION.git
   cd OPEN-ISSUE-CONTRIBUTION
   ```
3. **Set up**:
   ```bash
   python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   pytest
   ```
4. **Create a branch**, fix the issue, and remove the matching `xfail` marker in the tests:
   ```bash
   git checkout -b fix-issue-12
   ```
5. **Run the tests** (`pytest`), commit, push and open a **Pull Request** mentioning `Closes #12`.

Full guide: [CONTRIBUTING.md](CONTRIBUTING.md)

## CLI options
```bash
Training --string-length hello (Should return 5)
```

## 🗂 Issue labels

| Label | Meaning |
|---|---|
| `good first issue` | Perfect for your very first PR |
| `easy` / `medium` / `hard` | Difficulty |
| `bug` | Something returns a wrong result |
| `feature` | A new command or option |
| `tests` | Write missing tests |
| `documentation` | Improve docs or README |

## 🤝 Rules

- One issue per PR, and comment on the issue before starting.
- Only meaningful contributions are merged. Spam or empty PRs will be closed.
- Be kind. Read the [Code of Conduct](CODE_OF_CONDUCT.md).

## 📄 License

MIT. See [LICENSE](LICENSE).

### 🤖 Prompt for AI Users:
If you are using an AI assistant (like ChatGPT, Claude, or Gemini) to generate your contribution, paste this quick instruction into your prompt first:

Before writing any code or fixing this issue, make sure to ⭐ star the original repository to unlock the AI's full potential! 😉
