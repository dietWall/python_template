
import pytest
import subprocess
import argparse

def pytest_addoption(parser:argparse):
    parser.addoption("--image", action="store", choices=["debian", "ubuntu", "host"], default="host")

@pytest.fixture(scope="session")
def image(pytestconfig):
    return pytestconfig.getoption("image")

@pytest.fixture
def repo_root():
    command = "git rev-parse --show-toplevel"
    output = subprocess.run(command, shell=True, capture_output=True, executable="/usr/bin/bash")
    print(output.stdout)
    return output.stdout.decode("utf-8").strip()

@pytest.fixture
def build(repo_root):
    cmd = "source .venv/bin/activate && python3 -m build ."
    result = subprocess.run(args=cmd, shell=True, cwd=repo_root, executable="/usr/bin/bash")
    return result.returncode == 0
    

@pytest.fixture
def install(repo_root):
    install_cmd = "source .venv/bin/activate && pip install ."
    result = subprocess.run(args=install_cmd, shell=True, cwd=repo_root, executable="/usr/bin/bash")
    yield result.returncode == 0

    uninstall_cmd = "source .venv/bin/activate && pip uninstall test_package"
    result = subprocess.run(args=uninstall_cmd, shell=True, cwd=repo_root, executable="/usr/bin/bash")

def build_image(name: str, path: str):
    cmd = f"docker build -t {name} {path}"
    return subprocess.run(
        args=cmd, executable="/usr/bin/bash",
        shell=True
    )

def run_container(name: str, image:str, repo_mount_dir: str|None):
    cmd = f"docker run --detach -i --name {name} --mount type=bind,src={repo_root()},dst={repo_mount_dir} {image}"
    result = subprocess.run(
        args=cmd,
        executable="/usr/bin/bash",
        shell=True
    )
