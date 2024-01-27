import os

from pycleancodecli.cleaner import clean


TEST_DATA_DIR = "test_data"
if not os.path.exists(TEST_DATA_DIR):
    os.makedirs(TEST_DATA_DIR)


def test_single_line_comments():
    test_file_path = os.path.join(TEST_DATA_DIR, "test_single_line.py")
    with open(test_file_path, "w", encoding="UTF-8") as f:
        f.write("# This is a single line comment\n")
        f.write("print('Hello, world!')  # Another comment\n")

    clean(test_file_path, dry_run=False)

    with open(test_file_path, "r", encoding="UTF-8") as f:
        content = f.read()
        assert "# This is a single line comment" not in content
        assert "print('Hello, world!')" in content

    os.remove(test_file_path)


def test_block_comments():
    test_file_path = os.path.join(TEST_DATA_DIR, "test_block_comments.py")
    with open(test_file_path, "w", encoding="UTF-8") as f:
        f.write('"""This is a block comment"""\n')
        f.write("print('Hello, world!')\n")
        f.write('"""Another\n')
        f.write('block comment"""\n')

    clean(test_file_path, dry_run=False)

    with open(test_file_path, "r", encoding="UTF-8") as f:
        content = f.read()
        assert '"""This is a block comment"""\n' not in content
        assert "print('Hello, world!')\n" in content
        assert '"""Another\n' not in content
        assert 'block comment"""\n' not in content

    os.remove(test_file_path)


def test_edge_cases():
    test_file_path = os.path.join(TEST_DATA_DIR, "test_edge_cases.py")
    with open(test_file_path, "w", encoding="UTF-8") as f:
        f.write("print('# this is not a comment')\n")
        f.write("print('Hello, world!') # valid comment\n")
        f.write("url = 'http://example.com?param=1#anchor'\n")  # URL with a hash

    clean(test_file_path, dry_run=False)

    with open(test_file_path, "r", encoding="UTF-8") as f:
        content = f.read()
        assert "print('# this is not a comment')\n" in content
        assert "print('Hello, world!') \n" in content
        assert "url = 'http://example.com?param=1#anchor'\n" in content
        assert "# valid comment" not in content

    os.remove(test_file_path)


def test_mixed_comments_and_code():
    test_file_path = os.path.join(TEST_DATA_DIR, "test_mixed_comments_and_code.py")
    with open(test_file_path, "w", encoding="UTF-8") as f:
        f.write("# Comment before code\nprint('Hello')\n# Comment after code\n")

    clean(test_file_path, dry_run=False)

    with open(test_file_path, "r", encoding="UTF-8") as f:
        content = f.read()
        assert "# Comment before code" not in content
        assert "print('Hello')\n" in content
        assert "# Comment after code" not in content

    os.remove(test_file_path)


def test_nested_block_comments():
    test_file_path = os.path.join(TEST_DATA_DIR, "test_nested_block_comments.py")
    with open(test_file_path, "w", encoding="UTF-8") as f:
        f.write("'''Outer block comment\n")
        f.write("'''Inner block comment'''\n")
        f.write("Outer block comment end'''\n")
        f.write("print('Hello')\n")

    clean(test_file_path, dry_run=False)

    with open(test_file_path, "r", encoding="UTF-8") as f:
        content = f.read()
        assert "'''Outer block comment" not in content
        assert "print('Hello')\n" in content

    os.remove(test_file_path)


def test_comments_with_special_characters():
    test_file_path = os.path.join(
        TEST_DATA_DIR, "test_comments_with_special_characters.py"
    )
    with open(test_file_path, "w", encoding="UTF-8") as f:
        f.write("# Comment with !@#$%^&*()\n")
        f.write("print('Hello') # Comment with !@#$%^&*()\n")

    clean(test_file_path, dry_run=False)

    with open(test_file_path, "r", encoding="UTF-8") as f:
        content = f.read()
        assert "# Comment with !@#$%^&*()" not in content
        assert "print('Hello') \n" in content

    os.remove(test_file_path)


def test_code_with_hash_symbols():
    test_file_path = os.path.join(TEST_DATA_DIR, "test_code_with_hash_symbols.py")
    with open(test_file_path, "w", encoding="UTF-8") as f:
        f.write("hash_value = 'abc#123'\n")
        f.write("print(hash_value)  # Print hash\n")

    clean(test_file_path, dry_run=False)

    with open(test_file_path, "r", encoding="UTF-8") as f:
        content = f.read()
        assert "hash_value = 'abc#123'\n" in content
        assert "# Print hash" not in content

    os.remove(test_file_path)


def test_empty_lines_and_whitespace():
    test_file_path = os.path.join(TEST_DATA_DIR, "test_empty_lines_and_whitespace.py")
    with open(test_file_path, "w", encoding="UTF-8") as f:
        f.write("\n    # Indented comment\n\n")
        f.write("print('Hello')  # Comment with spaces\n   \n")

    clean(test_file_path, dry_run=False)

    with open(test_file_path, "r", encoding="UTF-8") as f:
        content = f.read()
        assert "# Indented comment" not in content
        assert "print('Hello')  \n" in content
        assert "   \n" in content  # Preserves empty lines and whitespace

    os.remove(test_file_path)
