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

|<div style="width:90px">Repositories</div>|<div style="width:120px">Description</div>|<div style="width:80px">Status</div>|<div style="width:80px">Version</div>|<div style="width:80px">Release Date</div>|
|------------------------------------------|------------------------------------------|------------------------------------|-------------------------------------|------------------------------------------|
|[github.io](https://github.com/epics-containers/epics-containers.github.io)|epics-containers<br>documentation|[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/epics-containers.github.io/docs.yml)](https://github.com/epics-containers/epics-containers.github.io/actions)|![GitHub version](https://img.shields.io/github/release/epics-containers/epics-containers.github.io/all?include_prereleases;label=tag)|[![GitHub Release Date](https://img.shields.io/github/release-date/epics-containers/epics-containers.github.io?label=release)](https://github.com/epics-containers/epics-containers.github.io/releases)|
|[ibek](https://github.com/epics-containers/ibek)|IOC Builder for EPICS<br>and Kubernetes|[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/ibek/code.yml)](https://github.com/epics-containers/ibek/actions)|[![PyPI - Version](https://img.shields.io/pypi/v/ibek?label=pypiver)](https://pypi.org/project/ibek)|[![GitHub Release Date](https://img.shields.io/github/release-date/epics-containers/ibek?label=release)](https://github.com/epics-containers/ibek/releases)|
|[epics-containers-cli](https://github.com/epics-containers/epics-containers-cli)|CLI dev tools for outside containers|[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/epics-containers-cli/code.yml)](https://github.com/epics-containers/epics-containers-cli/actions)|[![PyPI - Version](https://img.shields.io/pypi/v/epics-containers-cli?label=pypiver)](https://pypi.org/project/epics-containers-cli)|[![GitHub Release Date](https://img.shields.io/github/release-date/epics-containers/epics-containers-cli?label=release)](https://github.com/epics-containers/epics-containers-cli/releases)|
|[epics-base](https://github.com/epics-containers/epics-base)|Base image for Generic IOCs|[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/epics-base/build.yml)](https://github.com/epics-containers/epics-base/actions)|![GitHub version](https://img.shields.io/github/release/epics-containers/epics-base/all?include_prereleases;label=tag)|[![GitHub Release Date](https://img.shields.io/github/release-date/epics-containers/epics-base?label=release)](https://github.com/epics-containers/epics-base/releases)|
|[pvi](https://github.com/epics-containers/pvi)|PV Interface to define<br>Devices and screens|[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/pvi/code.yml)](https://github.com/epics-containers/pvi/actions)|[![PyPI - Version](https://img.shields.io/pypi/v/pvi?label=pypiver)](https://pypi.org/project/pvi)|[![GitHub Release Date](https://img.shields.io/github/release-date/epics-containers/pvi?label=release)](https://github.com/epics-containers/pvi/releases)|
|[ioc-template](https://github.com/epics-containers/ioc-template)|Template for Generic EPICS IOCs|[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/ioc-template/build.yml)](https://github.com/epics-containers/ioc-template/actions)|![GitHub version](https://img.shields.io/github/release/epics-containers/ioc-template/all?include_prereleases;label=tag)|[![GitHub Release Date](https://img.shields.io/github/release-date/epics-containers/ioc-template?label=release)](https://github.com/epics-containers/ioc-template/releases)|
|[blxxi-template](https://github.com/epics-containers/blxxi-template)|Template for  Domain repos|[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/blxxi-template/verify.yml)](https://github.com/epics-containers/blxxi-template/actions)|![GitHub version](https://img.shields.io/github/release/epics-containers/blxxi-template/all?include_prereleases;label=tag)|[![GitHub Release Date](https://img.shields.io/github/release-date/epics-containers/blxxi-template?label=release)](https://github.com/epics-containers/blxxi-template/releases)|
|[ec-helm-charts](https://github.com/epics-containers/ec-helm-charts)|helm charts for PICS Containers|[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/ec-helm-charts/helm_deploy.yml)](https://github.com/epics-containers/ec-helm-charts/actions)|![GitHub version](https://img.shields.io/github/release/epics-containers/ec-helm-charts/all?include_prereleases;label=tag)|[![GitHub Release Date](https://img.shields.io/github/release-date/epics-containers/ec-helm-charts?label=release)](https://github.com/epics-containers/ec-helm-charts/releases)|
|[ibek-support](https://github.com/epics-containers/ibek-support)|build support modules with ibek|[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/ibek-support/build.yml)](https://github.com/epics-containers/ibek-support/actions)|submodule|![GitHub last commit (branch)](https://img.shields.io/github/last-commit/epics-containers/ibek-support/main?label=main)|

## Reference Implementations

|<div style="width:90px">Repositories</div>|<div style="width:120px">Description</div>|<div style="width:80px">Status</div>|<div style="width:80px">Version</div>|<div style="width:80px">Release Date</div>|
|------------------------------------------|------------------------------------------|------------------------------------|-------------------------------------|------------------------------------------|
|[bl47p](https://github.com/epics-containers/bl47p)|Reference Containerized Test Beamline|[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/bl47p/verify.yml)](https://github.com/epics-containers/bl47p/actions)|![GitHub version](https://img.shields.io/github/release/epics-containers/bl47p/all?include_prereleases;label=tag)|[![GitHub Release Date](https://img.shields.io/github/release-date/epics-containers/bl47p?label=release)](https://github.com/epics-containers/bl47p/releases)|
|[ioc-adsimdetector](https://github.com/epics-containers/ioc-adsimdetector)|Generic IOC with ADSimDetector|[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/ioc-adsimdetector/build.yml)](https://github.com/epics-containers/ioc-adsimdetector/actions)|![GitHub version](https://img.shields.io/github/release/epics-containers/ioc-adsimdetector/all?include_prereleases;label=tag)|[![GitHub Release Date](https://img.shields.io/github/release-date/epics-containers/ioc-adsimdetector?label=release)](https://github.com/epics-containers/ioc-adsimdetector/releases)|
|[ioc-adaravis](https://github.com/epics-containers/ioc-adaravis)|Generic IOC with ADAravis|[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/epics-containers/ioc-adaravis/build.yml)](https://github.com/epics-containers/ioc-adaravis/actions)|![GitHub version](https://img.shields.io/github/release/epics-containers/ioc-adaravis/all?include_prereleases;label=tag)|[![GitHub Release Date](https://img.shields.io/github/release-date/epics-containers/ioc-adaravis?label=release)](https://github.com/epics-containers/ioc-adaravis/releases)|

