# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team

# tests directory-specific settings - this file is run automatically by pytest before any tests are run

import sys
import pytest
import os
from os.path import abspath, dirname, join
import torch
import warnings
from unit.ci_promote_marker import *
from unit.xfail_marker import *
from unit.skip_marker import *
from unit.compile_marker import *
from unit.a100_marker import *
from unit.util import get_hpu_dev_version
from deepspeed.accelerator import get_accelerator
from unit.util import hpu_lazy_enabled

# Set this environment variable for the T5 inference unittest(s) (e.g. google/t5-v1_1-small)
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'

# allow having multiple repository checkouts and not needing to remember to rerun
# 'pip install -e .[dev]' when switching between checkouts and running tests.
git_repo_path = abspath(join(dirname(dirname(__file__)), "src"))
sys.path.insert(1, git_repo_path)


def pytest_configure(config):
    config.option.color = "yes"
    config.option.durations = 0
    config.option.durations_min = 1
    config.option.verbose = True


def pytest_addoption(parser):
    parser.addoption("--torch_ver", default=None, type=str)
    parser.addoption("--cuda_ver", default=None, type=str)


def validate_version(expected, found):
    version_depth = expected.count('.') + 1
    found = '.'.join(found.split('.')[:version_depth])
    return found == expected


@pytest.fixture(scope="session", autouse=True)
def check_environment(pytestconfig):
    expected_torch_version = pytestconfig.getoption("torch_ver")
    expected_cuda_version = pytestconfig.getoption("cuda_ver")
    if expected_torch_version is None:
        warnings.warn(
            "Running test without verifying torch version, please provide an expected torch version with --torch_ver")
    elif not validate_version(expected_torch_version, torch.__version__):
        pytest.exit(
            f"expected torch version {expected_torch_version} did not match found torch version {torch.__version__}",
            returncode=2)
    if expected_cuda_version is None:
        warnings.warn(
            "Running test without verifying cuda version, please provide an expected cuda version with --cuda_ver")
    elif not validate_version(expected_cuda_version, torch.version.cuda):
        pytest.exit(
            f"expected cuda version {expected_cuda_version} did not match found cuda version {torch.version.cuda}",
            returncode=2)


# Override of pytest "runtest" for DistributedTest class
# This hook is run before the default pytest_runtest_call
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item):
    # We want to use our own launching function for distributed tests
    if getattr(item.cls, "is_dist_test", False):
        dist_test_class = item.cls()
        dist_test_class(item._request)
        item.runtest = lambda: True  # Dummy function so test is not run twice


def pytest_collection_modifyitems(items, config):
    device = get_accelerator().device_name()
    gaudi_dev = get_hpu_dev_version()
    hpu_lazy_mode = hpu_lazy_enabled()
    # Add comipile, CI and Promote marker
    marker_expression = config.getoption("-m")
    # This is to handle the case where marker is already present and compile marker is added. to avoid running of compile tests in other markers when not specified
    if marker_expression not in ["compile_1c", "compile_4c"]:
        deselected = []
        remaining_items = []
        for item in items:
            if item._nodeid in compile_tests_4c or item._nodeid in compile_tests_1c:
                deselected.append(item)
                continue
            remaining_items.append(item)
        items[:] = remaining_items  # Only tests with 'compile_mode' False remain
        config.hook.pytest_deselected(items=deselected)
    for item in items:
        if item._nodeid in compile_tests_4c:
            item._pyfuncitem.add_marker(pytest.mark.compile_4c)
        if item._nodeid in compile_tests_1c:
            item._pyfuncitem.add_marker(pytest.mark.compile_1c)
        if device != 'hpu':
            if item._nodeid in a100_tests:
                item._pyfuncitem.add_marker(pytest.mark.a100)
        if item._nodeid in hpu_ci_tests:
            item._pyfuncitem.add_marker(pytest.mark.hpu_ci)
        if item._nodeid in hpu_ci_tests_4cards:
            item._pyfuncitem.add_marker(pytest.mark.hpu_ci_4cards)
        if item._nodeid in gpu_ci_tests:
            item._pyfuncitem.add_marker(pytest.mark.gpu_ci)
        if item._nodeid in hpu_promote_tests:
            item._pyfuncitem.add_marker(pytest.mark.hpu_promote)
        if item._nodeid in hpu_promote_tests_4cards:
            item._pyfuncitem.add_marker(pytest.mark.hpu_promote_4cards)
        if item._nodeid in gpu_promote_tests:
            item._pyfuncitem.add_marker(pytest.mark.gpu_promote)

        # Add xfail and SKIP marker
        item.user_properties.append(("module_name", item.module.__name__))
        if device == 'hpu':
            # Lazy Run
            if hpu_lazy_mode:
                if item._nodeid in hpu_lazy_xfail_tests.keys():
                    item._pyfuncitem.add_marker(pytest.mark.xfail(reason=hpu_lazy_xfail_tests[item._nodeid]))
                if item._nodeid in hpu_lazy_skip_tests.keys():
                    item._pyfuncitem.add_marker(pytest.mark.skipif(reason=hpu_lazy_skip_tests[item._nodeid]))
                if gaudi_dev == "Gaudi":
                    if item._nodeid in g1_lazy_xfail_tests.keys():
                        item._pyfuncitem.add_marker(pytest.mark.xfail(reason=g1_lazy_xfail_tests[item._nodeid]))
                    if item._nodeid in g1_lazy_skip_tests.keys():
                        item._pyfuncitem.add_marker(pytest.mark.skip(reason=g1_lazy_skip_tests[item._nodeid]))
                if gaudi_dev == "Gaudi2":
                    if item._nodeid in g2_lazy_xfail_tests.keys():
                        item._pyfuncitem.add_marker(pytest.mark.xfail(reason=g2_lazy_xfail_tests[item._nodeid]))
                    if item._nodeid in g2_lazy_skip_tests.keys():
                        item._pyfuncitem.add_marker(pytest.mark.skip(reason=g2_lazy_skip_tests[item._nodeid]))
                if gaudi_dev == "Gaudi3":
                    if item._nodeid in g3_lazy_xfail_tests.keys():
                        item._pyfuncitem.add_marker(pytest.mark.xfail(reason=g3_lazy_xfail_tests[item._nodeid]))
                    if item._nodeid in g3_lazy_skip_tests.keys():
                        item._pyfuncitem.add_marker(pytest.mark.skip(reason=g3_lazy_skip_tests[item._nodeid]))
            # Eager Run
            else:
                if item._nodeid in hpu_eager_xfail_tests.keys():
                    item._pyfuncitem.add_marker(pytest.mark.xfail(reason=hpu_eager_xfail_tests[item._nodeid]))
                if item._nodeid in hpu_eager_skip_tests.keys():
                    item._pyfuncitem.add_marker(pytest.mark.skipif(reason=hpu_eager_skip_tests[item._nodeid]))
                if gaudi_dev == "Gaudi":
                    if item._nodeid in g1_eager_xfail_tests.keys():
                        item._pyfuncitem.add_marker(pytest.mark.xfail(reason=g1_eager_xfail_tests[item._nodeid]))
                    if item._nodeid in g1_eager_skip_tests.keys():
                        item._pyfuncitem.add_marker(pytest.mark.skip(reason=g1_eager_skip_tests[item._nodeid]))
                if gaudi_dev == "Gaudi2":
                    if item._nodeid in g2_eager_xfail_tests.keys():
                        item._pyfuncitem.add_marker(pytest.mark.xfail(reason=g2_eager_xfail_tests[item._nodeid]))
                    if item._nodeid in g2_eager_skip_tests.keys():
                        item._pyfuncitem.add_marker(pytest.mark.skip(reason=g2_eager_skip_tests[item._nodeid]))
                if gaudi_dev == "Gaudi3":
                    if item._nodeid in g3_eager_xfail_tests.keys():
                        item._pyfuncitem.add_marker(pytest.mark.xfail(reason=g3_eager_xfail_tests[item._nodeid]))
                    if item._nodeid in g3_eager_skip_tests.keys():
                        item._pyfuncitem.add_marker(pytest.mark.skip(reason=g3_eager_skip_tests[item._nodeid]))
        else:
            if item._nodeid in gpu_xfail_tests.keys():
                item._pyfuncitem.add_marker(pytest.mark.xfail(reason=gpu_xfail_tests[item._nodeid]))
            if item._nodeid in gpu_skip_tests.keys():
                item._pyfuncitem.add_marker(pytest.mark.skipif(reason=gpu_skip_tests[item._nodeid]))
        for marker in item.own_markers:
            if marker.name in ['skip', 'xfail']:
                if 'reason' in marker.kwargs:
                    item.user_properties.append(("message", marker.kwargs['reason']))


# We allow DistributedTest to reuse distributed environments. When the last
# test for a class is run, we want to make sure those distributed environments
# are destroyed.
def pytest_runtest_teardown(item, nextitem):
    if getattr(item.cls, "reuse_dist_env", False) and not nextitem:
        dist_test_class = item.cls()
        for num_procs, pool in dist_test_class._pool_cache.items():
            dist_test_class._close_pool(pool, num_procs, force=True)


@pytest.hookimpl(tryfirst=True)
def pytest_fixture_setup(fixturedef, request):
    if getattr(fixturedef.func, "is_dist_fixture", False):
        dist_fixture_class = fixturedef.func()
        dist_fixture_class(request)


def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        if call.excinfo:
            if not (any('message' in prop for prop in item.user_properties)):
                if call.excinfo.value:
                    item.user_properties.append(("message", call.excinfo.value))
