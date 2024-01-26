# S3 Parallel Sync

[![CodeQL](https://github.com/fortran01/s3psync/actions/workflows/codeql.yml/badge.svg)](https://github.com/fortran01/s3psync/actions/workflows/codeql.yml)
[![Dependency Review](https://github.com/fortran01/s3psync/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/fortran01/s3psync/actions/workflows/dependency-review.yml)
[![Python package](https://github.com/fortran01/s3psync/actions/workflows/python-package.yml/badge.svg)](https://github.com/fortran01/s3psync/actions/workflows/python-package.yml)
[![PyPI](https://github.com/fortran01/s3psync/actions/workflows/release-pypi.yml/badge.svg)](https://github.com/fortran01/s3psync/actions/workflows/release-pypi.yml)
This script is used to sync files and folders to an S3 bucket in parallel, leveraging the `aws s3 sync` command. The `aws s3 sync` command supports multipart uploads and can utilize up to 10 threads, making it particularly useful when you have a large number of large files to upload. This script allows you to specify the number of parallel instances of `aws s3 sync` to use.

## Requirements

- Python 3.10 or higher
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- AWS profile with the necessary permissions to perform S3 uploads (see [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) for more information on how to set up AWS profiles)
- Make utility ([Make for Windows](https://gnuwin32.sourceforge.net/packages/make.htm), Make for Linux and Mac is usually pre-installed)
  
## Usage

Next, you need to set up the environment using the provided Makefile. Follow these steps:

1. Ensure you have `make` installed on your system. You can check this by running `make --version` in your terminal. Install or update `make` if needed.

2. Install the necessary dependencies by running `make install` or `make all`.

3. Create a Python virtual environment by running `python3 -m venv --prompt s3psync venv`. Activate it by running `source venv/bin/activate`.

4. Verify the installation by running `s3psync --version`. If the tool is installed correctly, it should display the version number.

5. Exit the virtual environment by running `deactivate`.

To sync files and folders to an S3 bucket in parallel, run the following command:

