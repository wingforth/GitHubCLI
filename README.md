# GitHubCLI

A simple and extensible command-line interface (CLI) for interacting with the GitHub REST API. Supports viewing user, repository, issue, pull request, commit, branch, and rate limit information directly from your terminal.

## Features

- List and view GitHub events, users, repositories, issues, pull requests, commits, and branches
- Check API rate limits
- Supports authentication via personal access token
- Extensible command structure for easy addition of new features

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/wingforth/GitHubCLI
   cd GitHubCLI
   ```

2. (Optional) Create a virtual environment:

   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Authentication

Create a file named `.github-token` in the project root or parent directory, and paste your GitHub personal access token inside. Alternatively, you can modify the code to support the `GITHUB_TOKEN` environment variable.

## Usage

Run the CLI:

```sh
python github_cli.py <command> [options]
```

### Example Commands

- List your events:

  ```sh
  python github_cli.py event --user <username>
  ```

- View a repository:

  ```sh
  python github_cli.py repo view <owner>/<repo>
  ```

- List issues in a repository:

  ```sh
  python github_cli.py issue list --repo <owner>/<repo>
  ```

- View your rate limit:

  ```sh
  python github_cli.py ratelimit
  ```

For more options, use `-h` or `--help` after any command.

## Project Structure

- `github_cli.py` - Main CLI entry point and command dispatcher
- `commands.py` - Command and argument definitions
- `github/` - API wrappers and output formatting
- `cache/` - Cached API responses (if enabled)

## Dependencies

- Python 3.10+
- requests

Install all dependencies with:

```sh
pip install -r requirements.txt
```

## FAQ

**Q: How do I get a GitHub personal access token?**  
A: Go to https://github.com/settings/tokens and generate a new token with the required scopes.

**Q: How do I add new commands?**  
A: Edit `commands.py` and follow the existing structure. See the docstrings for guidance.

**Q: How do I clear the cache?**  
A: Delete the `cache/` directory in the project root.

## Contribution

Contributions are welcome! Please open issues or pull requests for bug fixes, new features, or improvements.

## License

This project is licensed under the MIT License.
