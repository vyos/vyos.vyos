

# VyOS Collection
[![CI](https://zuul-ci.org/gated.svg)](https://dashboard.zuul.ansible.com/t/ansible/project/github.com/ansible-collections/vyos) <!--[![Codecov](https://img.shields.io/codecov/c/github/ansible-collections/vyos)](https://codecov.io/gh/ansible-collections/vyos)-->

The Ansible VyOS collection includes a variety of Ansible content to help automate the management of VyOS network appliances.

This collection has been tested against VyOS 1.1.8 (helium).


### Supported connections
The VyOS collection supports ``network_cli`` connections.

## Included content

Click the ``Content`` button to see the list of content included in this collection.

## Installing this collection

You can install the VyOS collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install vyos.vyos

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: vyos.vyos
    version: 0.0.2
```
## Using this collection


This collection includes [network resource modules](https://docs.ansible.com/ansible/latest/network/user_guide/network_resource_modules.html).

### Using modules from the VyOS collection in your playbooks

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `vyos.vyos.vyos_static_routes`.
The following example task replaces configuration changes in the existing configuration on a VyOS network device, using the FQCN:

```yaml
---
  - name: Replace device configurations of listed static routes with provided
      configurations
    register: result
    vyos.vyos.vyos_static_routes: &id001
      config:

        - address_families:

            - afi: ipv4
              routes:

                - dest: 192.0.2.32/28
                  blackhole_config:
                    distance: 2
                  next_hops:

                    - forward_router_address: 192.0.2.7

                    - forward_router_address: 192.0.2.8

                    - forward_router_address: 192.0.2.9
      state: replaced
```

Alternately, you can call modules by their short name if you list the `vyos.vyos` collection in the playbook's `collections`, as follows:

```yaml
---
- hosts: vyos01
  gather_facts: false
  connection: network_cli

  collections:
    - vyos.vyos

  tasks:
    - name: Merge the provided configuration with the existing running configuration
      register: result
      vyos_l3_interfaces: &id001
        config:

          - name: eth1
            ipv4:

              - address: 192.0.2.10/24
            ipv6:

              - address: 2001:db8::10/32

          - name: eth2
            ipv4:

              - address: 198.51.100.10/24
            vifs:

              - vlan_id: 101
                ipv4:

                  - address: 198.51.100.130/25
                ipv6:

                  - address: 2001:db8::20/32
        state: merged
```






### See Also:

* [VyOS Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_vyos.html)
* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [VyOS collection repository](https://github.com/ansible-collections/vyos).

You cal also join us on:

- Freenode IRC - ``#ansible-network`` Freenode channel
- Slack - https://ansiblenetwork.slack.com

See the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) for details on contributing to Ansible.


## Changelogs
<!--Add a link to a changelog.md file or an external docsite to cover this information. -->

## Roadmap

<!-- Optional. Include the roadmap for this collection, and the proposed release/versioning strategy so users can anticipate the upgrade/update cycle. -->

## More information

- [Ansible network resources](https://docs.ansible.com/ansible/latest/network/getting_started/network_resources.html)
- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [LICENCE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
