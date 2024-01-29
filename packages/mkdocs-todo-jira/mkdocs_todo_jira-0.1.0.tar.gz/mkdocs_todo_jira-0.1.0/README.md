
# mkdocs-todo-jira

This MkDocs plugin scans your project's source files for `TODO` and `BUG` comments and generates a markdown page listing all found entries. It's an excellent tool for developers looking to maintain a high level of code quality and documentation.

## Features

- Scans Python source files for `TODO` and `BUG` comments.
- Generates a markdown file summarizing all the tasks and bugs.
- Easy to integrate with your MkDocs project.

## Installation

Install `mkdocs-todo-jira` using pip:

```bash
pip install mkdocs-todo-jira
```

## Configuration

Add `todo-jira` to your `mkdocs.yml` plugin section:

```yaml
plugins:
  - todo-jira
```

Optionally, you can configure the source directory and patterns to exclude:

```yaml
plugins:
  - todo-jira:
      source_dir: 'your/source/directory'
      exclude_patterns: ['**/exclude_dir/**', '**.exclude_file.py']
```

## Usage

Once configured, run `mkdocs build` or `mkdocs serve`, and the plugin will generate a markdown page with all your `TODO` and `BUG` comments.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
