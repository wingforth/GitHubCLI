def run():
    from github_cli.cli import GithubCli

    try:
        GithubCli()
    except KeyboardInterrupt:
        print("The operation has been canceled.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    import sys

    # Import github_cli package
    if not __package__:
        from pathlib import Path

        sys.path[0] = str(Path(sys.path[0]).parent)
        import github_cli  # noqa

        sys.path.pop(0)

    sys.exit(run())
