from pathlib import Path

HEADER = '<div style="width:{width}px">{heading}</div>'
REPO = "[{name}](https://github.com/epics-containers/{repo_name})"
DESCRIPTION = "{description}"
STATUS = "[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/{repo_name}/{actions_file})](https://github.com/epics-containers/{repo_name}/actions)"
VERSION = "![GitHub version](https://img.shields.io/github/release/epics-containers/{repo_name}/all?include_prereleases;label=tag)"
DEV_COMMIT = "![GitHub last commit (branch)](https://img.shields.io/github/last-commit/epics-containers/{repo_name}/dev?label=dev)"
RELEASE = "[![GitHub Release Date](https://img.shields.io/github/release-date/epics-containers/{repo_name}?label=rel)](https://github.com/epics-containers/{repo_name}/releases)"
PYPI = "[![PyPI - Version](https://img.shields.io/pypi/v/{repo_name})](https://pypi.org/project/{repo_name}/)"
MAIN_COMMIT = "![GitHub last commit (branch)](https://img.shields.io/github/last-commit/epics-containers/{repo_name}/main?label=main)"

DATES = f"{RELEASE}<br>{DEV_COMMIT}"
CI = f"{STATUS}<br>{RELEASE}"
CIPYPI = f"{STATUS}<br>{PYPI}"


def main():
    header = [
        HEADER.format(width=90, heading="Repositories"),
        HEADER.format(width=120, heading="Description"),
        HEADER.format(width=80, heading="Status"),
        HEADER.format(width=80, heading="Version"),
        HEADER.format(width=80, heading="Release"),
        HEADER.format(width=80, heading="Dev Commit"),
    ]
    divider = ["-" * len(heading) for heading in header]

    frameworks = [
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE, DEV_COMMIT],
            1: {
                "name": "github.io",
                "repo_name": "epics-containers.github.io",
                "actions_file": "docs.yml",
                "description": "epics-containers<br>documentation",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, PYPI, RELEASE, DEV_COMMIT],
            1: {
                "name": "ibek",
                "repo_name": "ibek",
                "actions_file": "code.yml",
                "description": "IOC Builder for EPICS<br>and Kubernetes",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, "*submodule only*", MAIN_COMMIT, DEV_COMMIT],
            1: {
                "name": "ibek-support",
                "repo_name": "ibek-support",
                "actions_file": "build.yml",
                "description": "build support<br>modules with ibek",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, PYPI, RELEASE, DEV_COMMIT],
            1: {
                "name": "epics-containers-cli",
                "repo_name": "epics-containers-cli",
                "actions_file": "code.yml",
                "description": "CLI dev tools for<br>outside containers",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE, DEV_COMMIT],
            1: {
                "name": "epics-base",
                "repo_name": "epics-base",
                "actions_file": "build.yml",
                "description": "Base image for<br>Generic IOCs",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, PYPI, RELEASE, DEV_COMMIT],
            1: {
                "name": "pvi",
                "repo_name": "pvi",
                "actions_file": "code.yml",
                "description": "PV Interface to define<br>Devices and screens",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE, DEV_COMMIT],
            1: {
                "name": "ioc-template",
                "repo_name": "ioc-template",
                "actions_file": "build.yml",
                "description": "Template for Generic<br>EPICS IOCs",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE, DEV_COMMIT],
            1: {
                "name": "blxxi-template",
                "repo_name": "blxxi-template",
                "actions_file": "verify.yml",
                "description": "Template for <br>Domain repos",
            },
        },
    ]
    reference = [
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE, DEV_COMMIT],
            1: {
                "name": "bl38p",
                "repo_name": "bl38p",
                "actions_file": "verify.yml",
                "description": "Reference Containerized Beamline",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE, DEV_COMMIT],
            1: {
                "name": "bl45p",
                "repo_name": "bl45p",
                "actions_file": "verify.yml",
                "description": "Example Containerized Beamline",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE, DEV_COMMIT],
            1: {
                "name": "ioc-adsimdetector",
                "repo_name": "ioc-adsimdetector",
                "actions_file": "build.yml",
                "description": "Generic IOC with ADSimDetector",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE, DEV_COMMIT],
            1: {
                "name": "ioc-adaravis",
                "repo_name": "ioc-adaravis",
                "actions_file": "build.yml",
                "description": "Generic IOC with ADAravis",
            },
        },
    ]

    sections = {}
    for num, section in enumerate([frameworks, reference]):
        rows = []
        for row_def in section:
            row = [pattern.format(**row_def[1]) for pattern in row_def[0]]
            rows.append(row)

        sections[num] = ""
        for line in [header, divider] + rows:
            sections[num] += "|" + "|".join(line) + "|\n"

    file = Path("README.template.md")
    template = file.read_text()
    text = template.format(sections=sections)

    file = Path("README.md")
    file.write_text(text)


if __name__ == "__main__":
    main()
