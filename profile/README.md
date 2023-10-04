# EPICS Containers Organization

The epics-containers GitHub organization holds a collection of tools and documentation
for building, deploying and managing containerized EPICS IOCs in a Kubernetes cluster.

Documentation for the framework is available at
[epics-containers.github.io](https://epics-containers.github.io/).

Please contribute with comments and suggestions in the
[Discussion Forum](https://github.com/epics-containers/epics-containers.github.io/discussions)
or the [Wiki](https://github.com/epics-containers/epics-containers.github.io/wiki).
If you discover issues with the framework please raise them in the
[Issue Tracker](https://github.com/epics-containers/epics-containers.github.io/issues)


Latest News: the framework is in the process of a major overhaul. Consequently
the tutorials are currently out of date. The new approach is greatly simplified
and will have a new tutorial By end of November 2023.

# Current Status

## Epics Containers Framework Repositories

--------------------------------------------------------------
| <div style="width:80px">Repository</div> | <div style="width:200px;">Description</div>| <div style="width:80px">Status</div> | <div style="width:80px">Version</div> | <div style="width:80px">Release Date</div> |
|-------------------------------------------------------------------------------------|-------------|--------|---------|--------------|
|[github.io](https://epics-containers.github.io/)| Documentation and Tutorials |![Status](https://img.shields.io/github/actions/workflow/status/epics-containers/epics-containers.github.io/docs.yml)|![GitHub release (latest by SemVer including pre-releases)](https://img.shields.io/github/release/epics-containers/epics-containers.github.io/all?include_prereleases)|![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/epics-containers/epics-containers.github.io?label=date)
|[ibek](https://github.com/epics-containers/ibek)| IOC Builder for EPICS<br>and Kubernetes|![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/epics-containers/ibek/code.yml)|![PyPI - Version](https://img.shields.io/pypi/v/ibek)|![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/epics-containers/ibek?label=date)
|[ibek-support](https://github.com/epics-containers/ibek-support)|Support module build<br>in container scripts|![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/epics-containers/ibek-support/buiild.yml?style=plastic)|*submodule only*|![GitHub last commit (branch)](https://img.shields.io/github/last-commit/epics-containers/ibek-support/main?label=date)
|[epics-containers-cli](https://github.com/epics-containers/epics-containers-cli)| CLI dev tools<br>for outside container| ![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/epics-containers/epics-containers-cli/code.yml)|![PyPI - Version](https://img.shields.io/pypi/v/epics-containers-cli)|![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/epics-containers/epics-containers-cli?label=date)
|[epics-base](https://github.com/epics-containers/epics-base)| Base image for EPICS IOCs|![itHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/epics-containers/epics-base/buiild.yml)|![GitHub release (latest by SemVer including pre-releases)](https://img.shields.io/github/release/epics-containers/epics-base/all?include_prereleases)|![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/epics-containers/epics-base?label=date)
|[pvi](https://github.com/epics-containers/pvi)| PV Interface to define Devices,<br>generate Device screens|![Status](https://img.shields.io/github/actions/workflow/status/epics-containers/pvi/code.yml)|![GitHub release (latest by SemVer including pre-releases)](https://img.shields.io/github/release/epics-containers/pvi/all?include_prereleases)|![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/epics-containers/pvi?label=date)
|[ioc-template](https://github.com/epics-containers/ioc-template)| Template for Generic<br>EPICS IOCs|![Status](https://img.shields.io/github/actions/workflow/status/epics-containers/ioc-template/buiild.yml)|![GitHub release (latest by SemVer including pre-releases)](https://img.shields.io/github/release/epics-containers/ioc-template/all?include_prereleases)|![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/epics-containers/ioc-template?label=date)
|[blxxi-template](https://github.com/epics-containers/blxxi-template)| Template for Beamline and<br>Accelerator Domain repos|![Status](https://img.shields.io/github/actions/workflow/status/epics-containers/blxxi-template/verify.yml)|![GitHub release (latest by SemVer including pre-releases)](https://img.shields.io/github/release/epics-containers/blxxi-template/all?include_prereleases)|![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/epics-containers/blxxi-template?label=date)

## Reference Implementations

--------------------------------------------------------------
| <div style="width:80px">Repository</div> | <div style="width:200px;">Description</div>| <div style="width:80">Status</div> | <div style="width:80px">Version</div> | <div style="width:80px">Release Date</div> |
|------------|-------------|--------|---------|--------------|
|[bl45p](https://github.com/epics-containers/bl45p)| Example containerised Beamline|![Status](https://img.shields.io/github/actions/workflow/status/epics-containers/bl45p/verify.yml)|![GitHub release (latest by SemVer including pre-releases)](https://img.shields.io/github/release/epics-containers/bl45p/all?include_prereleases)|![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/epics-containers/bl45p?label=date)
|[ioc-adsimdetector](https://github.com/epics-containers/ioc-adsimdetector)| Generic IOC with ADSimDetector|![Status](https://img.shields.io/github/actions/workflow/status/epics-containers/ioc-adsimdetector/buiild.yml)|![GitHub release (latest by SemVer including pre-releases)](https://img.shields.io/github/release/epics-containers/ioc-adsimdetector/all?include_prereleases)|![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/epics-containers/ioc-adsimdetector?label=date)
|[ioc-adaravis](https://github.com/epics-containers/ioc-adaravis)| Generic IOC with ADAravis|![Status](https://img.shields.io/github/actions/workflow/status/epics-containers/ioc-adaravis/buiild.yml)|![GitHub release (latest by SemVer including pre-releases)](https://img.shields.io/github/release/epics-containers/ioc-adaravis/all?include_prereleases)|![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/epics-containers/ioc-adaravis?label=date)