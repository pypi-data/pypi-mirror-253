import pytest
from s3psync.s3cli import S3CLI
from unittest.mock import patch

@pytest.fixture
def s3cli():
    return S3CLI(aws_profile='test-profile')

def test_get_total_size(s3cli):
    # Setup: Create a mock file list with known sizes
    file_list = [('dir', 'file1.txt'), ('dir', 'file2.txt')]
    # Mock the os.path.getsize to return a fixed size for any file
    with patch('os.path.getsize', return_value=100):
        # Call the method under test
        total_size = s3cli.get_total_size('/fake/dir', file_list)
        # Assert the expected result
        assert total_size == 200
