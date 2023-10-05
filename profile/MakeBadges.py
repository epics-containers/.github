HEADER = '<div style="width:{width}px">{heading}</div>'
REPO = "[{name}](https://github.com/epics-containers/{repo_name})"
DESCRIPTION = "{description}"
STATUS = "[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/{repo_name}/{actions_file})](https://github.com/epics-containers/{repo_name}/actions)"
VERSION = "![GitHub version](https://img.shields.io/github/release/epics-containers/{repo_name}/all?include_prereleases)"
RELEASE = "![GitHub Release Date](https://img.shields.io/github/release-date/epics-containers/{repo_name}?label=date)"
PYPI="![PyPI - Version](https://img.shields.io/pypi/v/{repo_name})"

def main():
    header = [
        HEADER.format(width=90, heading="Repositories"),
        HEADER.format(width=120, heading="Description"),
        HEADER.format(width=80, heading="Status"),
        HEADER.format(width=80, heading="Version"),
        HEADER.format(width=80, heading="Release"),
    ]
    divider = ["-" * len(heading) for heading in header]

    row_defs = [
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE],
            1: {
                "name": "github.io",
                "repo_name": "epics-containers.github.io",
                "actions_file": "code.yml",
                "description": "epics-containers documentation",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, PYPI, RELEASE],
            1: {
                "name": "ibek",
                "url": "https://epics-containers/ibek",
                "repo_name": "ibek",
                "actions_file": "code.yml",
                "description": "IOC Builder for EPICS and Kubernetes",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, "*submodule only*", RELEASE],
            1: {
                "name": "ibek-support",
                "repo_name": "ibek-support",
                "actions_file": "build.yml",
                "description": "scripts for building support modules with ibek",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE],
            1: {
                "name": "epics-containers-cli",
                "repo_name": "epics-containers-cli",
                "actions_file": "code.yml",
                "description": "CLI dev tools for outside containers",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE],
            1: {
                "name": "epics-base",
                "repo_name": "epics-base",
                "actions_file": "build.yml",
                "description": "Base image for Generic IOCs",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, PYPI, RELEASE],
            1: {
                "name": "pvi",
                "repo_name": "pvi",
                "actions_file": "code.yml",
                "description": "PV Interface to define Devices, generate Device screens",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE],
            1: {
                "name": "ioc-template",
                "repo_name": "ioc-template",
                "actions_file": "build.yml",
                "description": "Template for Generic EPICS IOCs",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE],
            1: {
                "name": "blxxi-template",
                "repo_name": "blxxi-template",
                "actions_file": "verify.yml",
                "description": "Template for Beamline and Accelerator Domain repos",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE],
            1: {
                "name": "bl45p",
                "repo_name": "bl45p",
                "actions_file": "verify.yml",
                "description": "Example Containerized Beamline",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE],
            1: {
                "name": "ioc-adsimdetector",
                "repo_name": "ioc-adsimdetector",
                "actions_file": "buiild.yml",
                "description": "Generic IOC with ADSimDetector",
            },
        },
        {
            0: [REPO, DESCRIPTION, STATUS, VERSION, RELEASE],
            1: {
                "name": "ioc-adaravis",
                "repo_name": "ioc-adaravis",
                "actions_file": "buiild.yml",
                "description": "Generic IOC with ADAravis",
            },
        },
    ]

    rows = []
    for row_def in row_defs:
        row = [pattern.format(**row_def[1]) for pattern in row_def[0]]
        rows.append(row)

    for line in [header, divider] + rows:
        print("|" + "|".join(line) + "|")


if __name__ == "__main__":
    main()
