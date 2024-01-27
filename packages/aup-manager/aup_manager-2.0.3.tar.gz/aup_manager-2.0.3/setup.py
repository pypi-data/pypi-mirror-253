from subprocess import check_call
import setuptools
from setuptools.command.install import install


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        check_call(
            "cd aup_manager/static && npm install && npm run compile_sass", shell=True
        )
        install.run(self)


setuptools.setup(
    name="aup_manager",
    python_requires=">=3.9",
    url="https://gitlab.ics.muni.cz/perun/perun-proxyidp/aup-manager.git",
    description="app for management of acceptable use policies with API for approving them",
    include_package_data=True,
    package_data={"": ["openapi-specification.yaml"]},
    packages=setuptools.find_packages(),
    install_requires=[
        "setuptools",
        "pymongo>=3.13.0,<5",  # for compatibility with proxyidp-gui
        "jsonpatch~=1.22",
        "connexion[swagger-ui]~=2.14",
        "markdown2~=2.4",
        "Flask-pyoidc~=3.11",
        "jwcrypto~=1.5.0",
    ],
    extras_require={
        "perun": ["perun.connector~=3.3"],
    },
    cmdclass={
        "install": PostInstallCommand,
    },
)
