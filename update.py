import sys


def update_vim(user, title, vim_path):
    """ Updates Vim file with new user, title
    """
    # Read lines from file
    with open(vim_path, "r") as f:
        lines = f.readlines()
    # Insert title into file
    lines.insert(-5, f"      \\ ['{title}', '', '@{user}'],\n")
    with open(vim_path, "w") as f:
        f.writelines(lines)


def update_md(user, title, md_path):
    """ Updates Markdown file with new user, title
    """
    with open(md_path, "a") as f:
        f.writelines(f"[@{user}](https://github.com/{user}) | {title}\n")


def main():
    import os
    user, title = str(os.environ['USER']), str(os.environ['TITLE'])
    if all(x.isalpha() or x.isspace() for x in str(title)):
        update_vim(user, title, "fortune.vim")
        update_md(user, title, "MESSAGES.md")


if __name__ == "__main__":
    main()
