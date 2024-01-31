from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bellande_robot_step",
    version="0.3.0",
    description="Robots Step",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="RonaldsonBellande",
    author_email="ronaldsonbellande@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "numpy",
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
    ],
    keywords=["package", "setuptools"],
    python_requires=">=3.0",
    extras_require={
        "dev": ["pytest", "pytest-cov[all]", "mypy", "black"],
    },
    entry_points={
        'console_scripts': [
            'bellande_step_2d = bellande_robot_step.bellande_robot_step_2d:bellande_step_2d',
            'bellande_step_3d = bellande_robot_step.bellande_robot_step_3d:bellande_step_3d',
            'bellande_step_4d = bellande_robot_step.bellande_robot_step_4d:bellande_step_4d',
            'bellande_step_5d = bellande_robot_step.bellande_robot_step_5d:bellande_step_5d',
            'bellande_step_6d = bellande_robot_step.bellande_robot_step_6d:bellande_step_6d',
            'bellande_step_7d = bellande_robot_step.bellande_robot_step_7d:bellande_step_7d',
            'bellande_step_8d = bellande_robot_step.bellande_robot_step_8d:bellande_step_8d',
            'bellande_step_9d = bellande_robot_step.bellande_robot_step_9d:bellande_step_9d',
            'bellande_step_10d = bellande_robot_step.bellande_robot_step_10d:bellande_step_10d',
        ],
    },
    project_urls={
        "Home": "https://github.com/RonaldsonBellande/bellande_robot_step",
        "Homepage": "https://github.com/RonaldsonBellande/bellande_robot_step",
        "documentation": "https://github.com/RonaldsonBellande/bellande_robot_step",
        "repository": "https://github.com/RonaldsonBellande/bellande_robot_step",
    },
)
