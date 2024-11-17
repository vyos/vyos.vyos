<!-- All PR should follow this template to allow a clean and transparent review -->
<!-- Text placed between these delimiters is considered a comment and is not rendered -->

## Change Summary
<!--- Provide a general summary of your changes in the Title above -->

## Types of changes
<!---
What types of changes does your code introduce? Put an 'x' in all the boxes that apply.
NOTE: Markdown requires no leading or trailing whitespace inside the [ ] for checking
the box, please use [x]
-->
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Code style update (formatting, renaming)
- [ ] Refactoring (no functional changes)
- [ ] Migration from an old Vyatta component to vyos-1x, please link to related PR inside obsoleted component
- [ ] Other (please describe):

## Related Task(s)
<!-- optional: Link to related other tasks on Phabricator. -->
<!-- * https://vyos.dev/Txxxx -->

## Related PR(s)
<!-- Link here any PRs in other repositories that are required by this PR -->

## Component(s) name
<!-- A rather incomplete list of components: ethernet, wireguard, bgp, mpls, ldp, l2tp, dhcp ... -->

## Proposed changes
<!--- Describe your changes in detail -->

## How to test
<!---
Please describe in detail how you tested your changes. Include details of your testing
environment, and the tests you ran. When pasting configs, logs, shell output, backtraces,
and other large chunks of text, surround this text with triple backtics
```
like this
```
-->

## Test results
<!--
Provide the output of the unit tests and confirmation of the sanity tests
along with a description of which versions of VyOS you have tested against.

Tests will be run before the PR is accepted, but do not run automatically
on forks, so please run all of the tests with each modification of your PR
to ensure they will pass.

Unit test information can be found in the [Ansible Unit Tests](https://docs.ansible.com/ansible/latest/dev_guide/testing_units.html#testing-units)
section of the documentation.

Sanity test information can be found in the [Ansible Sanity Tests](https://docs.ansible.com/ansible/latest/dev_guide/testing_sanity.html#testing-sanity)
section of the Ansible documentation.

```
Example:

$ ansible-tests units
============================= test session starts ==============================
platform linux -- Python 3.12.2, pytest-8.1.1, pluggy-1.4.0
rootdir: /root/ansible_collections/vyos/vyos
configfile: ../../../ansible/test/lib/ansible_test/_data/pytest/config/default.ini
plugins: xdist-3.5.0, mock-3.14.0
created: 24/24 workers
24 workers [244 items]

........................................................................ [ 29%]
........................................................................ [ 59%]
........................................................................ [ 88%]
............................                                             [100%]
- generated xml file: /root/ansible_collections/vyos/vyos/tests/output/junit/python3.12-controller-units.xml -
============================= 244 passed in 1.55s ==============================

Describe the versions of VyOS that you have tested your changes
against.

```
-->
- [ ] Sanity tests passed
- [ ] Unit tests passed

Tested against VyOS versions:
<!-- examples, add or delete as appropriate; if using rolling versions, please specify
    fully
-->
- 1.3.8
- 1.4-rolling-202201010100


## Checklist:
<!--- Go over all the following points, and put an `x` in all the boxes that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're here to help! -->
<!--- The entire development process is outlined here: https://docs.vyos.io/en/latest/contributing/development.html -->
- [ ] I have read the [**CONTRIBUTING**](https://github.com/vyos/vyos-1x/blob/current/CONTRIBUTING.md) document
- [ ] I have linked this PR to one or more Phabricator Task(s)
- [ ] I have run the ansible sanity and unit tests
- [ ] My commit headlines contain a valid Task id
- [ ] My change requires a change to the documentation
- [ ] I have updated the documentation accordingly
- [ ] I have added unit tests to cover my changes
- [ ] I have added a file to `changelogs/fragments` to describe the changes

