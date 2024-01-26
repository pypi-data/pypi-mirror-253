import os
import subprocess
import pytest
from s3psync.s3cli import S3CLI
from unittest.mock import patch
from s3psync.s3cli import sync_file


@pytest.fixture
def s3cli():
    return S3CLI(aws_profile="test-profile")


def test_get_total_size(s3cli):
    # Setup: Create a mock file list with known sizes
    file_list = [("dir", "file1.txt"), ("dir", "file2.txt")]
    # Mock the os.path.getsize to return a fixed size for any file
    with patch("os.path.getsize", return_value=100):
        # Call the method under test
        total_size = s3cli.get_total_size("/fake/dir", file_list)
        # Assert the expected result
        assert total_size == 200


def test_sync_file(s3cli):
    # Setup: Create a mock file info and other parameters
    file_info = ("dir", "file1.txt")
    parent_dir = "/fake/dir"
    aws_profile = "test-profile"
    s3_bucket = "test-bucket"

    # Mock the subprocess.run to not actually run the command
    with patch("subprocess.run") as mock_run:
        # Call the method under test
        sync_file(file_info, parent_dir, aws_profile, s3_bucket)

    # Assert that subprocess.run was called with the expected command
    expected_cmd = [
        "aws",
        "s3",
        "sync",
        "--profile",
        aws_profile,
        "--exclude",
        "*",
        "--include",
        f"*{file_info[1]}",
        "--quiet",
        os.path.join(parent_dir, file_info[0]),
        f"s3://{s3_bucket}/{file_info[0]}/",
    ]
    mock_run.assert_called_once_with(expected_cmd, check=True)


def test_get_files(s3cli):
    # Setup: Create a mock directory with files
    parent_dir = "/fake/dir"
    expected_file_list = [
        (".", "file"),
        ("subdir2", "hello_world2"),
        ("subdir1", "hello_world"),
    ]

    # Mock the os.path.isdir to return True
    with patch("os.path.isdir", return_value=True):
        # Mock the os.walk to return a fixed file list for any directory
        # Directory structure
        # /fake/dir
        # ├── file
        # ├── subdir1
        # │   └── hello_world
        # └── subdir2
        #     └── hello_world2
        with patch(
            "os.walk",
            return_value=[
                (parent_dir, ["subdir2", "subdir1"], ["file"]),
                (parent_dir + "/subdir2", [], ["hello_world2"]),
                (parent_dir + "/subdir1", [], ["hello_world"]),
            ],
        ):
            # Call the method under test
            file_list = s3cli.get_files(parent_dir)
            # Assert the expected result
            assert file_list == expected_file_list
