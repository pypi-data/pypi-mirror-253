import os
from collections import defaultdict
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
import tokenize
from io import BytesIO
from typing import List, Dict, Tuple


class MarkdownGenerator:
    """Generates markdown content from TODOs and BUGs, including a summary and only including sections with entries."""

    def generate(self, todos: dict[str, dict[str, list[tuple[int, str]]]]) -> str:
        """Generates markdown from todos and bugs.

        Args:
            todos (dict): A dictionary containing todos and bugs information.

        Returns:
            str: The generated markdown content.
        """
        total_todos, total_bugs = 0, 0
        markdown_content = []

        for module, files in todos.items():
            module_content = []
            module_todos, module_bugs = 0, 0

            for file_path, items in files.items():
                file_todos, file_bugs, file_content_lines = self._process_file_items(
                    items
                )

                if file_todos or file_bugs:
                    file_content_str = f"### {file_path}\n" + "\n\n".join(
                        file_content_lines
                    )
                    module_content.append(file_content_str)
                    module_todos += file_todos
                    module_bugs += file_bugs

            if module_todos or module_bugs:
                module_content_str = f"## {module}\n" + "\n".join(module_content)
                markdown_content.append(module_content_str)
                total_todos += module_todos
                total_bugs += module_bugs

        summary = f"\n\n- Total TODOs: {total_todos}\n- Total BUGs: {total_bugs}\n\n"
        markdown_content_str = "\n".join(markdown_content)
        return (
            summary + markdown_content_str
            if markdown_content_str
            else summary + "No TODOs or BUGs found."
        )

    def _process_file_items(
        self, items: list[tuple[int, str]]
    ) -> tuple[int, int, list[str]]:
        """Processes file items to extract TODOs and BUGs.

        Args:
            items (list): A list of tuples containing line numbers and comments.

        Returns:
            tuple: Total number of TODOs and BUGs in the file, along with the formatted content lines.
        """
        file_todos, file_bugs = 0, 0
        file_content = []

        for line_number, comment in items:
            keyword = "TODO" if "TODO:" in comment else "BUG"
            comment_text = comment.split(":", 1)[1].strip()
            file_content.append(
                f"{keyword.upper()}: {comment_text} - [Line {line_number}]"
            )
            if keyword == "TODO":
                file_todos += 1
            else:
                file_bugs += 1

        return file_todos, file_bugs, file_content


class TODOJira(BasePlugin):
    """
    A MkDocs plugin that scans project source files for TODO and BUG comments,
    and generates a markdown page listing all found entries.

    Attributes:
        config_scheme (tuple): Configuration options for the plugin, including
            `source_dir` specifying the directory to scan for source files and
            `exclude_patterns` listing patterns to exclude from scanning.
    """

    config_scheme = (
        ("source_dir", config_options.Type(str, default=".")),
        ("exclude_patterns", config_options.Type(list, default=[])),
        ("page_title", config_options.Type(str, default="TODOs & FIXMEs"))
    )

    def on_page_markdown(self, markdown: str, page, config, files) -> str:
        """
        Hook called by MkDocs to allow the plugin to modify the markdown content of a page.

        Args:
            markdown (str): The original markdown content of the page.
            page: The page object.
            config: The MkDocs config object.
            files: The files object.

        Returns:
            str: Modified markdown content for the page.
        """
        if page.title == "todo-jira":
            markdown = f'# {self.config["page_title"]}\n'
            source_dir = self.config["source_dir"]
            exclude_patterns = self.config["exclude_patterns"]
            todos = self.scan_source_files(source_dir, exclude_patterns)
            markdown_generator = MarkdownGenerator()
            markdown += markdown_generator.generate(todos)
        return markdown

    def scan_source_files(
        self, source_dir: str, exclude_patterns: List[str]
    ) -> Dict[str, Dict[str, List[Tuple[int, str]]]]:
        """
        Scans the specified source directory for files containing TODO and BUG comments,
        excluding files and directories that match any of the given patterns.

        Args:
            source_dir (str): The directory to scan for source files.
            exclude_patterns (List[str]): Patterns for files and directories to exclude from the scan.

        Returns:
            Dict[str, Dict[str, List[Tuple[int, str]]]]: A nested dictionary where the first key is the module/directory,
            the second key is the file path, and the value is a list of tuples containing the line number and comment text.
        """
        todos = defaultdict(lambda: defaultdict(list))
        for root, dirs, files in os.walk(source_dir):
            # Efficiently exclude directories and files
            dirs[:] = (d for d in dirs if not any(pat in d for pat in exclude_patterns))
            files[:] = (
                f
                for f in files
                if f.endswith(".py") and not any(pat in f for pat in exclude_patterns)
            )

            for file in files:
                file_path = os.path.join(root, file)
                self.parse_file_todos(file_path, todos[root])
        return todos

    def parse_file_todos(self, file_path: str, todos_container: dict):
        """
        Parses a single file for TODO and BUG comments, adding found entries to the provided container.

        Args:
            file_path (str): Path to the file to be parsed.
            todos_container (dict): Container to which found TODO and BUG comments are added.
        """
        with open(file_path, "rb") as f:
            content = f.read()
            tokens = tokenize.tokenize(BytesIO(content).readline)

            for token in tokens:
                if token.type == tokenize.COMMENT or (
                    token.type == tokenize.STRING
                    and ('"""' in token.string or "'''" in token.string)
                ):
                    for line in self.extract_relevant_lines(token.string):
                        line_number, comment = line
                        if "FIXME:" in comment:
                            comment = comment.replace(
                                "FIXME:", "BUG:"
                            )  # Convert FIXME to BUG
                        todos_container[file_path].append((line_number, comment))

    def extract_relevant_lines(self, comment_block: str) -> list:
        """
        Extracts lines containing TODO, FIXME, or BUG comments from a block of text.

        Args:
            comment_block (str): A block of text potentially containing comment lines.

        Returns:
            List[Tuple[int, str]]: A list of tuples where each tuple contains a line number and the comment text.
        """
        relevant_lines = []
        start_line = None

        for i, line in enumerate(comment_block.split("\n"), start=1):
            if "TODO:" in line or "FIXME:" in line or "BUG" in line:
                if not start_line:
                    start_line = i
                line = (
                    line.replace("#", "").replace('"""', "").replace("'''", "").strip()
                )
                relevant_lines.append((start_line + i - 1, line))

        return relevant_lines
