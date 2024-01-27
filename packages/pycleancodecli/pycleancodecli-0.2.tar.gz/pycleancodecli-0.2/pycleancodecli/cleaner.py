def clean(file_path, dry_run=False):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned_lines = process_lines(lines)

    code = "".join(cleaned_lines)

    if dry_run:
        print(code)
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)


def process_lines(lines):
    """Processes lines of code, removing comments and unnecessary empty lines."""
    cleaned_lines = []
    in_comment_block = False

    for line in lines:
        original_line_empty = not line.strip()
        line, in_comment_block = handle_block_comments(line, in_comment_block)

        if line is not None:
            cleaned_line = remove_line_comments(line)
            if cleaned_line.strip() or original_line_empty:
                cleaned_lines.append(cleaned_line)

    return cleaned_lines


def handle_block_comments(line, in_comment_block):
    """Handles block comments, returning None if the line is within a block comment."""
    if '"""' in line or "'''" in line:
        if line.count('"""') == 2 or line.count("'''") == 2:
            return None, in_comment_block  # Entire line is a block comment
        else:
            in_comment_block = not in_comment_block
            return None, in_comment_block  # Line starts/ends a block comment

    if in_comment_block:
        return None, in_comment_block  # Line is within a block comment

    return line, in_comment_block  # Line is code or has inline comments


def remove_line_comments(line):
    """Removes inline comments from a line of code."""
    in_string = False
    escape = False
    for i, char in enumerate(line):
        if char in "\"'" and not escape:
            in_string = not in_string
        elif char == "#" and not in_string:
            return line[:i] + "\n"
        escape = char == "\\" and not escape
    return line
