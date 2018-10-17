"""Setup for configurable_lti_consumer XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, __, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='configurable_lti_consumer-xblock',
    version='0.1',
    description="This Xblock inherit fom edX's lti_consumer to provide configurability via Django settings",
    packages=[
        'configurable_lti_consumer',
    ],
    install_requires=[
        'lxml',
        'bleach',
        'oauthlib',
        'mako',
        'XBlock',
        'xblock-utils>=v1.0.0',
    ],
    dependency_links=[
        '',
    ],
    entry_points={
        'xblock.v1': [
            'lti_consumer = configurable_lti_consumer:ConfigurableLtiConsumerXBlock',
        ]
    },
    package_data=package_data("configurable_lti_consumer", ["static", "templates", "public", "translations"]),
)
