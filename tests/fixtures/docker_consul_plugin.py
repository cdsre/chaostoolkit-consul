import os
import subprocess
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    # Define path to your docker-compose.yml
    docker_compose_path = "./tests/fixtures/docker-compose-consul.yml"

    # Start Docker containers
    subprocess.run(["docker", "compose", "-f", docker_compose_path, "up", "-d"])

    # Provide the service some time to start up (adjust as needed)
    subprocess.run(["sleep", "10"])


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    # Define path to your docker-compose.yml
    docker_compose_path = "./tests/fixtures/docker-compose-consul.yml"

    # Teardown: Stop Docker containers
    subprocess.run(["docker", "compose", "-f", docker_compose_path, "down"])