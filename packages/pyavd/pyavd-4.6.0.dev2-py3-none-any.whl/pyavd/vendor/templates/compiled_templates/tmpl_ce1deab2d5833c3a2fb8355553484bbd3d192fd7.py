from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/vlan-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_vlan_interfaces = resolve('vlan_interfaces')
    try:
        t_1 = environment.filters['arista.avd.hide_passwords']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.hide_passwords' found.")
    try:
        t_2 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_3 = environment.filters['indent']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'indent' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    for l_1_vlan_interface in t_2((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), 'name'):
        l_1_interface_ip_nat = resolve('interface_ip_nat')
        l_1_hide_passwords = resolve('hide_passwords')
        l_1_ip_attached_host_route_export_cli = resolve('ip_attached_host_route_export_cli')
        _loop_vars = {}
        pass
        yield '!\ninterface '
        yield str(environment.getattr(l_1_vlan_interface, 'name'))
        yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'description')):
            pass
            yield '   description '
            yield str(environment.getattr(l_1_vlan_interface, 'description'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'shutdown'), True):
            pass
            yield '   shutdown\n'
        elif t_4(environment.getattr(l_1_vlan_interface, 'shutdown'), False):
            pass
            yield '   no shutdown\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'mtu')):
            pass
            yield '   mtu '
            yield str(environment.getattr(l_1_vlan_interface, 'mtu'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'no_autostate'), True):
            pass
            yield '   no autostate\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'vrf')):
            pass
            yield '   vrf '
            yield str(environment.getattr(l_1_vlan_interface, 'vrf'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'arp_aging_timeout')):
            pass
            yield '   arp aging timeout '
            yield str(environment.getattr(l_1_vlan_interface, 'arp_aging_timeout'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'arp_gratuitous_accept'), True):
            pass
            yield '   arp gratuitous accept\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'arp_monitor_mac_address'), True):
            pass
            yield '   arp monitor mac-address\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'arp_cache_dynamic_capacity')):
            pass
            yield '   arp cache dynamic capacity '
            yield str(environment.getattr(l_1_vlan_interface, 'arp_cache_dynamic_capacity'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ip_proxy_arp'), True):
            pass
            yield '   ip proxy-arp\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ip_directed_broadcast'), True):
            pass
            yield '   ip directed-broadcast\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ip_address')):
            pass
            yield '   ip address '
            yield str(environment.getattr(l_1_vlan_interface, 'ip_address'))
            yield '\n'
            if t_4(environment.getattr(l_1_vlan_interface, 'ip_address_secondaries')):
                pass
                for l_2_ip_address_secondary in environment.getattr(l_1_vlan_interface, 'ip_address_secondaries'):
                    _loop_vars = {}
                    pass
                    yield '   ip address '
                    yield str(l_2_ip_address_secondary)
                    yield ' secondary\n'
                l_2_ip_address_secondary = missing
        if t_4(environment.getattr(l_1_vlan_interface, 'ip_verify_unicast_source_reachable_via')):
            pass
            yield '   ip verify unicast source reachable-via '
            yield str(environment.getattr(l_1_vlan_interface, 'ip_verify_unicast_source_reachable_via'))
            yield '\n'
        for l_2_ip_helper in t_2(environment.getattr(l_1_vlan_interface, 'ip_helpers'), 'ip_helper'):
            l_2_ip_helper_cli = missing
            _loop_vars = {}
            pass
            l_2_ip_helper_cli = str_join(('ip helper-address ', environment.getattr(l_2_ip_helper, 'ip_helper'), ))
            _loop_vars['ip_helper_cli'] = l_2_ip_helper_cli
            if t_4(environment.getattr(l_2_ip_helper, 'vrf')):
                pass
                l_2_ip_helper_cli = str_join(((undefined(name='ip_helper_cli') if l_2_ip_helper_cli is missing else l_2_ip_helper_cli), ' vrf ', environment.getattr(l_2_ip_helper, 'vrf'), ))
                _loop_vars['ip_helper_cli'] = l_2_ip_helper_cli
            if t_4(environment.getattr(l_2_ip_helper, 'source_interface')):
                pass
                l_2_ip_helper_cli = str_join(((undefined(name='ip_helper_cli') if l_2_ip_helper_cli is missing else l_2_ip_helper_cli), ' source-interface ', environment.getattr(l_2_ip_helper, 'source_interface'), ))
                _loop_vars['ip_helper_cli'] = l_2_ip_helper_cli
            yield '   '
            yield str((undefined(name='ip_helper_cli') if l_2_ip_helper_cli is missing else l_2_ip_helper_cli))
            yield '\n'
        l_2_ip_helper = l_2_ip_helper_cli = missing
        for l_2_destination in t_2(environment.getattr(l_1_vlan_interface, 'ipv6_dhcp_relay_destinations'), 'address'):
            l_2_destination_cli = missing
            _loop_vars = {}
            pass
            l_2_destination_cli = str_join(('ipv6 dhcp relay destination ', environment.getattr(l_2_destination, 'address'), ))
            _loop_vars['destination_cli'] = l_2_destination_cli
            if t_4(environment.getattr(l_2_destination, 'vrf')):
                pass
                l_2_destination_cli = str_join(((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli), ' vrf ', environment.getattr(l_2_destination, 'vrf'), ))
                _loop_vars['destination_cli'] = l_2_destination_cli
            if t_4(environment.getattr(l_2_destination, 'local_interface')):
                pass
                l_2_destination_cli = str_join(((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli), ' local-interface ', environment.getattr(l_2_destination, 'local_interface'), ))
                _loop_vars['destination_cli'] = l_2_destination_cli
            elif t_4(environment.getattr(l_2_destination, 'source_address')):
                pass
                l_2_destination_cli = str_join(((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli), ' source-address ', environment.getattr(l_2_destination, 'source_address'), ))
                _loop_vars['destination_cli'] = l_2_destination_cli
            if t_4(environment.getattr(l_2_destination, 'link_address')):
                pass
                l_2_destination_cli = str_join(((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli), ' link-address ', environment.getattr(l_2_destination, 'link_address'), ))
                _loop_vars['destination_cli'] = l_2_destination_cli
            yield '   '
            yield str((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli))
            yield '\n'
        l_2_destination = l_2_destination_cli = missing
        if t_4(environment.getattr(l_1_vlan_interface, 'ip_igmp'), True):
            pass
            yield '   ip igmp\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ip_igmp_version')):
            pass
            yield '   ip igmp version '
            yield str(environment.getattr(l_1_vlan_interface, 'ip_igmp_version'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ipv6_enable'), True):
            pass
            yield '   ipv6 enable\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ipv6_address')):
            pass
            yield '   ipv6 address '
            yield str(environment.getattr(l_1_vlan_interface, 'ipv6_address'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ipv6_address_link_local')):
            pass
            yield '   ipv6 address '
            yield str(environment.getattr(l_1_vlan_interface, 'ipv6_address_link_local'))
            yield ' link-local\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ipv6_address_virtual')):
            pass
            yield '   ipv6 address virtual '
            yield str(environment.getattr(l_1_vlan_interface, 'ipv6_address_virtual'))
            yield '\n'
        for l_2_ipv6_address_virtual in t_2(environment.getattr(l_1_vlan_interface, 'ipv6_address_virtuals')):
            _loop_vars = {}
            pass
            yield '   ipv6 address virtual '
            yield str(l_2_ipv6_address_virtual)
            yield '\n'
        l_2_ipv6_address_virtual = missing
        if t_4(environment.getattr(l_1_vlan_interface, 'ipv6_nd_ra_disabled'), True):
            pass
            yield '   ipv6 nd ra disabled\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ipv6_nd_managed_config_flag'), True):
            pass
            yield '   ipv6 nd managed-config-flag\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ipv6_nd_prefixes')):
            pass
            for l_2_prefix in environment.getattr(l_1_vlan_interface, 'ipv6_nd_prefixes'):
                l_2_ipv6_nd_prefix_cli = missing
                _loop_vars = {}
                pass
                l_2_ipv6_nd_prefix_cli = str_join(('ipv6 nd prefix ', environment.getattr(l_2_prefix, 'ipv6_prefix'), ))
                _loop_vars['ipv6_nd_prefix_cli'] = l_2_ipv6_nd_prefix_cli
                if t_4(environment.getattr(l_2_prefix, 'valid_lifetime')):
                    pass
                    l_2_ipv6_nd_prefix_cli = str_join(((undefined(name='ipv6_nd_prefix_cli') if l_2_ipv6_nd_prefix_cli is missing else l_2_ipv6_nd_prefix_cli), ' ', environment.getattr(l_2_prefix, 'valid_lifetime'), ))
                    _loop_vars['ipv6_nd_prefix_cli'] = l_2_ipv6_nd_prefix_cli
                    if t_4(environment.getattr(l_2_prefix, 'preferred_lifetime')):
                        pass
                        l_2_ipv6_nd_prefix_cli = str_join(((undefined(name='ipv6_nd_prefix_cli') if l_2_ipv6_nd_prefix_cli is missing else l_2_ipv6_nd_prefix_cli), ' ', environment.getattr(l_2_prefix, 'preferred_lifetime'), ))
                        _loop_vars['ipv6_nd_prefix_cli'] = l_2_ipv6_nd_prefix_cli
                if t_4(environment.getattr(l_2_prefix, 'no_autoconfig_flag'), True):
                    pass
                    l_2_ipv6_nd_prefix_cli = str_join(((undefined(name='ipv6_nd_prefix_cli') if l_2_ipv6_nd_prefix_cli is missing else l_2_ipv6_nd_prefix_cli), ' no-autoconfig', ))
                    _loop_vars['ipv6_nd_prefix_cli'] = l_2_ipv6_nd_prefix_cli
                yield '   '
                yield str((undefined(name='ipv6_nd_prefix_cli') if l_2_ipv6_nd_prefix_cli is missing else l_2_ipv6_nd_prefix_cli))
                yield '\n'
            l_2_prefix = l_2_ipv6_nd_prefix_cli = missing
        if t_4(environment.getattr(l_1_vlan_interface, 'multicast')):
            pass
            if t_4(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'multicast'), 'ipv4'), 'boundaries')):
                pass
                for l_2_boundary in environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'multicast'), 'ipv4'), 'boundaries'):
                    l_2_boundary_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_boundary_cli = str_join(('multicast ipv4 boundary ', environment.getattr(l_2_boundary, 'boundary'), ))
                    _loop_vars['boundary_cli'] = l_2_boundary_cli
                    if t_4(environment.getattr(l_2_boundary, 'out'), True):
                        pass
                        l_2_boundary_cli = str_join(((undefined(name='boundary_cli') if l_2_boundary_cli is missing else l_2_boundary_cli), ' out', ))
                        _loop_vars['boundary_cli'] = l_2_boundary_cli
                    yield '   '
                    yield str((undefined(name='boundary_cli') if l_2_boundary_cli is missing else l_2_boundary_cli))
                    yield '\n'
                l_2_boundary = l_2_boundary_cli = missing
            if t_4(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'multicast'), 'ipv6'), 'boundaries')):
                pass
                for l_2_boundary in environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'multicast'), 'ipv6'), 'boundaries'):
                    _loop_vars = {}
                    pass
                    yield '   multicast ipv6 boundary '
                    yield str(environment.getattr(l_2_boundary, 'boundary'))
                    yield ' out\n'
                l_2_boundary = missing
            if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'multicast'), 'ipv4'), 'source_route_export'), 'enabled'), True):
                pass
                if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'multicast'), 'ipv4'), 'source_route_export'), 'administrative_distance')):
                    pass
                    yield '   multicast ipv4 source route export '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'multicast'), 'ipv4'), 'source_route_export'), 'administrative_distance'))
                    yield '\n'
                else:
                    pass
                    yield '   multicast ipv4 source route export\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'multicast'), 'ipv6'), 'source_route_export'), 'enabled'), True):
                pass
                if t_4(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'multicast'), 'ipv6'), 'source_route_export'), 'administrative_distance')):
                    pass
                    yield '   multicast ipv6 source route export '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'multicast'), 'ipv6'), 'source_route_export'), 'administrative_distance'))
                    yield '\n'
                else:
                    pass
                    yield '   multicast ipv6 source route export\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'multicast'), 'ipv4'), 'static'), True):
                pass
                yield '   multicast ipv4 static\n'
            if t_4(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'multicast'), 'ipv6'), 'static'), True):
                pass
                yield '   multicast ipv6 static\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ip_nat')):
            pass
            l_1_interface_ip_nat = environment.getattr(l_1_vlan_interface, 'ip_nat')
            _loop_vars['interface_ip_nat'] = l_1_interface_ip_nat
            template = environment.get_template('eos/interface-ip-nat.j2', 'eos/vlan-interfaces.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {'interface_ip_nat': l_1_interface_ip_nat, 'ip_attached_host_route_export_cli': l_1_ip_attached_host_route_export_cli, 'vlan_interface': l_1_vlan_interface})):
                yield event
        if t_4(environment.getattr(l_1_vlan_interface, 'access_group_in')):
            pass
            yield '   ip access-group '
            yield str(environment.getattr(l_1_vlan_interface, 'access_group_in'))
            yield ' in\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'access_group_out')):
            pass
            yield '   ip access-group '
            yield str(environment.getattr(l_1_vlan_interface, 'access_group_out'))
            yield ' out\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ipv6_access_group_in')):
            pass
            yield '   ipv6 access-group '
            yield str(environment.getattr(l_1_vlan_interface, 'ipv6_access_group_in'))
            yield ' in\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ipv6_access_group_out')):
            pass
            yield '   ipv6 access-group '
            yield str(environment.getattr(l_1_vlan_interface, 'ipv6_access_group_out'))
            yield ' out\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ospf_network_point_to_point'), True):
            pass
            yield '   ip ospf network point-to-point\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ospf_area')):
            pass
            yield '   ip ospf area '
            yield str(environment.getattr(l_1_vlan_interface, 'ospf_area'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ospf_cost')):
            pass
            yield '   ip ospf cost '
            yield str(environment.getattr(l_1_vlan_interface, 'ospf_cost'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ospf_authentication')):
            pass
            if (environment.getattr(l_1_vlan_interface, 'ospf_authentication') == 'simple'):
                pass
                yield '   ip ospf authentication\n'
            elif (environment.getattr(l_1_vlan_interface, 'ospf_authentication') == 'message-digest'):
                pass
                yield '   ip ospf authentication message-digest\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ospf_authentication_key')):
            pass
            yield '   ip ospf authentication-key 7 '
            yield str(t_1(environment.getattr(l_1_vlan_interface, 'ospf_authentication_key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
            yield '\n'
        for l_2_ospf_message_digest_key in t_2(environment.getattr(l_1_vlan_interface, 'ospf_message_digest_keys'), 'id'):
            _loop_vars = {}
            pass
            if (t_4(environment.getattr(l_2_ospf_message_digest_key, 'hash_algorithm')) and t_4(environment.getattr(l_2_ospf_message_digest_key, 'key'))):
                pass
                yield '   ip ospf message-digest-key '
                yield str(environment.getattr(l_2_ospf_message_digest_key, 'id'))
                yield ' '
                yield str(environment.getattr(l_2_ospf_message_digest_key, 'hash_algorithm'))
                yield ' 7 '
                yield str(t_1(environment.getattr(l_2_ospf_message_digest_key, 'key'), (undefined(name='hide_passwords') if l_1_hide_passwords is missing else l_1_hide_passwords)))
                yield '\n'
        l_2_ospf_message_digest_key = missing
        if t_4(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'pim'), 'ipv4'), 'sparse_mode'), True):
            pass
            yield '   pim ipv4 sparse-mode\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'pim'), 'ipv4'), 'dr_priority')):
            pass
            yield '   pim ipv4 dr-priority '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'pim'), 'ipv4'), 'dr_priority'))
            yield '\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'pim'), 'ipv4'), 'local_interface')):
            pass
            yield '   pim ipv4 local-interface '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'pim'), 'ipv4'), 'local_interface'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ipv6_virtual_router_address')):
            pass
            yield '   ipv6 virtual-router address '
            yield str(environment.getattr(l_1_vlan_interface, 'ipv6_virtual_router_address'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ipv6_virtual_router_addresses')):
            pass
            for l_2_ipv6_virtual_router_address in environment.getattr(l_1_vlan_interface, 'ipv6_virtual_router_addresses'):
                _loop_vars = {}
                pass
                yield '   ipv6 virtual-router address '
                yield str(l_2_ipv6_virtual_router_address)
                yield '\n'
            l_2_ipv6_virtual_router_address = missing
        if t_4(environment.getattr(l_1_vlan_interface, 'isis_enable')):
            pass
            yield '   isis enable '
            yield str(environment.getattr(l_1_vlan_interface, 'isis_enable'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'isis_passive'), True):
            pass
            yield '   isis passive\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'isis_metric')):
            pass
            yield '   isis metric '
            yield str(environment.getattr(l_1_vlan_interface, 'isis_metric'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'isis_network_point_to_point'), True):
            pass
            yield '   isis network point-to-point\n'
        if t_4(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'virtual_router')):
            pass
            if t_4(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'priority')):
                pass
                yield '   vrrp '
                yield str(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'virtual_router'))
                yield ' priority-level '
                yield str(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'priority'))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'advertisement_interval')):
                pass
                yield '   vrrp '
                yield str(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'virtual_router'))
                yield ' advertisement interval '
                yield str(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'advertisement_interval'))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'preempt_delay_minimum')):
                pass
                yield '   vrrp '
                yield str(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'virtual_router'))
                yield ' preempt delay minimum '
                yield str(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'preempt_delay_minimum'))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'ipv4')):
                pass
                yield '   vrrp '
                yield str(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'virtual_router'))
                yield ' ipv4 '
                yield str(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'ipv4'))
                yield '\n'
            if t_4(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'ipv6')):
                pass
                yield '   vrrp '
                yield str(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'virtual_router'))
                yield ' ipv6 '
                yield str(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'ipv6'))
                yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'vrrp_ids')):
            pass
            def t_5(fiter):
                for l_2_vrid in fiter:
                    if t_4(environment.getattr(l_2_vrid, 'id')):
                        yield l_2_vrid
            for l_2_vrid in t_5(t_2(environment.getattr(l_1_vlan_interface, 'vrrp_ids'), 'id')):
                l_2_delay_cli = resolve('delay_cli')
                _loop_vars = {}
                pass
                if t_4(environment.getattr(l_2_vrid, 'priority_level')):
                    pass
                    yield '   vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' priority-level '
                    yield str(environment.getattr(l_2_vrid, 'priority_level'))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr(l_2_vrid, 'advertisement'), 'interval')):
                    pass
                    yield '   vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' advertisement interval '
                    yield str(environment.getattr(environment.getattr(l_2_vrid, 'advertisement'), 'interval'))
                    yield '\n'
                if (t_4(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'enabled'), True) and (t_4(environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'delay'), 'minimum')) or t_4(environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'delay'), 'reload')))):
                    pass
                    l_2_delay_cli = str_join(('vrrp ', environment.getattr(l_2_vrid, 'id'), ' preempt delay', ))
                    _loop_vars['delay_cli'] = l_2_delay_cli
                    if t_4(environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'delay'), 'minimum')):
                        pass
                        l_2_delay_cli = str_join(((undefined(name='delay_cli') if l_2_delay_cli is missing else l_2_delay_cli), ' minimum ', environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'delay'), 'minimum'), ))
                        _loop_vars['delay_cli'] = l_2_delay_cli
                    if t_4(environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'delay'), 'reload')):
                        pass
                        l_2_delay_cli = str_join(((undefined(name='delay_cli') if l_2_delay_cli is missing else l_2_delay_cli), ' reload ', environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'delay'), 'reload'), ))
                        _loop_vars['delay_cli'] = l_2_delay_cli
                    yield '   '
                    yield str((undefined(name='delay_cli') if l_2_delay_cli is missing else l_2_delay_cli))
                    yield '\n'
                elif t_4(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'enabled'), False):
                    pass
                    yield '   no vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' preempt\n'
                if t_4(environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'timers'), 'delay'), 'reload')):
                    pass
                    yield '   vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' timers delay reload '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_2_vrid, 'timers'), 'delay'), 'reload'))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr(l_2_vrid, 'ipv4'), 'address')):
                    pass
                    yield '   vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' ipv4 '
                    yield str(environment.getattr(environment.getattr(l_2_vrid, 'ipv4'), 'address'))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr(l_2_vrid, 'ipv4'), 'version')):
                    pass
                    yield '   vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' ipv4 version '
                    yield str(environment.getattr(environment.getattr(l_2_vrid, 'ipv4'), 'version'))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr(l_2_vrid, 'ipv6'), 'address')):
                    pass
                    yield '   vrrp '
                    yield str(environment.getattr(l_2_vrid, 'id'))
                    yield ' ipv6 '
                    yield str(environment.getattr(environment.getattr(l_2_vrid, 'ipv6'), 'address'))
                    yield '\n'
                for l_3_tracked_obj in t_2(environment.getattr(l_2_vrid, 'tracked_object'), 'name'):
                    l_3_tracked_obj_cli = resolve('tracked_obj_cli')
                    _loop_vars = {}
                    pass
                    if t_4(environment.getattr(l_3_tracked_obj, 'name')):
                        pass
                        l_3_tracked_obj_cli = str_join(('vrrp ', environment.getattr(l_2_vrid, 'id'), ' tracked-object ', environment.getattr(l_3_tracked_obj, 'name'), ))
                        _loop_vars['tracked_obj_cli'] = l_3_tracked_obj_cli
                        if t_4(environment.getattr(l_3_tracked_obj, 'decrement')):
                            pass
                            l_3_tracked_obj_cli = str_join(((undefined(name='tracked_obj_cli') if l_3_tracked_obj_cli is missing else l_3_tracked_obj_cli), ' decrement ', environment.getattr(l_3_tracked_obj, 'decrement'), ))
                            _loop_vars['tracked_obj_cli'] = l_3_tracked_obj_cli
                        elif t_4(environment.getattr(l_3_tracked_obj, 'shutdown'), True):
                            pass
                            l_3_tracked_obj_cli = str_join(((undefined(name='tracked_obj_cli') if l_3_tracked_obj_cli is missing else l_3_tracked_obj_cli), ' shutdown', ))
                            _loop_vars['tracked_obj_cli'] = l_3_tracked_obj_cli
                        yield '   '
                        yield str((undefined(name='tracked_obj_cli') if l_3_tracked_obj_cli is missing else l_3_tracked_obj_cli))
                        yield '\n'
                l_3_tracked_obj = l_3_tracked_obj_cli = missing
            l_2_vrid = l_2_delay_cli = missing
        if t_4(environment.getattr(environment.getattr(l_1_vlan_interface, 'ip_attached_host_route_export'), 'enabled'), True):
            pass
            l_1_ip_attached_host_route_export_cli = 'ip attached-host route export'
            _loop_vars['ip_attached_host_route_export_cli'] = l_1_ip_attached_host_route_export_cli
            if t_4(environment.getattr(environment.getattr(l_1_vlan_interface, 'ip_attached_host_route_export'), 'distance')):
                pass
                l_1_ip_attached_host_route_export_cli = str_join(((undefined(name='ip_attached_host_route_export_cli') if l_1_ip_attached_host_route_export_cli is missing else l_1_ip_attached_host_route_export_cli), ' ', environment.getattr(environment.getattr(l_1_vlan_interface, 'ip_attached_host_route_export'), 'distance'), ))
                _loop_vars['ip_attached_host_route_export_cli'] = l_1_ip_attached_host_route_export_cli
            yield '   '
            yield str((undefined(name='ip_attached_host_route_export_cli') if l_1_ip_attached_host_route_export_cli is missing else l_1_ip_attached_host_route_export_cli))
            yield '\n'
        if ((t_4(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'interval')) and t_4(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'min_rx'))) and t_4(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'multiplier'))):
            pass
            yield '   bfd interval '
            yield str(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'interval'))
            yield ' min-rx '
            yield str(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'min_rx'))
            yield ' multiplier '
            yield str(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'multiplier'))
            yield '\n'
        if t_4(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'echo'), True):
            pass
            yield '   bfd echo\n'
        elif t_4(environment.getattr(environment.getattr(l_1_vlan_interface, 'bfd'), 'echo'), False):
            pass
            yield '   no bfd echo\n'
        if t_4(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'service_policy'), 'pbr'), 'input')):
            pass
            yield '   service-policy type pbr input '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_vlan_interface, 'service_policy'), 'pbr'), 'input'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'pvlan_mapping')):
            pass
            yield '   pvlan mapping '
            yield str(environment.getattr(l_1_vlan_interface, 'pvlan_mapping'))
            yield '\n'
        if t_4(environment.getattr(l_1_vlan_interface, 'ip_virtual_router_addresses')):
            pass
            for l_2_ip_virtual_router_address in environment.getattr(l_1_vlan_interface, 'ip_virtual_router_addresses'):
                _loop_vars = {}
                pass
                yield '   ip virtual-router address '
                yield str(l_2_ip_virtual_router_address)
                yield '\n'
            l_2_ip_virtual_router_address = missing
        if t_4(environment.getattr(l_1_vlan_interface, 'ip_address_virtual')):
            pass
            yield '   ip address virtual '
            yield str(environment.getattr(l_1_vlan_interface, 'ip_address_virtual'))
            yield '\n'
            if t_4(environment.getattr(l_1_vlan_interface, 'ip_address_virtual_secondaries')):
                pass
                for l_2_ip_address_virtual_secondary in environment.getattr(l_1_vlan_interface, 'ip_address_virtual_secondaries'):
                    _loop_vars = {}
                    pass
                    yield '   ip address virtual '
                    yield str(l_2_ip_address_virtual_secondary)
                    yield ' secondary\n'
                l_2_ip_address_virtual_secondary = missing
        if t_4(environment.getattr(l_1_vlan_interface, 'eos_cli')):
            pass
            yield '   '
            yield str(t_3(environment.getattr(l_1_vlan_interface, 'eos_cli'), 3, False))
            yield '\n'
    l_1_vlan_interface = l_1_interface_ip_nat = l_1_hide_passwords = l_1_ip_attached_host_route_export_cli = missing

blocks = {}
debug_info = '7=36&9=43&10=45&11=48&13=50&15=53&18=56&19=59&21=61&24=64&25=67&27=69&28=72&30=74&33=77&36=80&37=83&39=85&42=88&45=91&46=94&47=96&48=98&49=102&53=105&54=108&56=110&57=114&58=116&59=118&61=120&62=122&64=125&66=128&67=132&68=134&69=136&71=138&72=140&73=142&74=144&76=146&77=148&79=151&81=154&84=157&85=160&87=162&90=165&91=168&93=170&94=173&96=175&97=178&99=180&100=184&102=187&105=190&108=193&109=195&110=199&111=201&112=203&113=205&114=207&117=209&118=211&120=214&123=217&124=219&125=221&126=225&127=227&128=229&130=232&133=235&134=237&135=241&138=244&139=246&140=249&145=254&146=256&147=259&152=264&155=267&159=270&160=272&161=274&163=277&164=280&166=282&167=285&169=287&170=290&172=292&173=295&175=297&178=300&179=303&181=305&182=308&184=310&185=312&187=315&191=318&192=321&194=323&195=326&197=329&200=336&203=339&204=342&206=344&207=347&211=349&212=352&215=354&216=356&217=360&220=363&221=366&223=368&226=371&227=374&229=376&233=379&234=381&235=384&237=388&238=391&240=395&241=398&243=402&244=405&246=409&247=412&251=416&252=418&253=426&254=429&256=433&257=436&259=440&262=442&263=444&264=446&266=448&267=450&269=453&270=455&271=458&273=460&274=463&276=467&277=470&279=474&280=477&282=481&283=484&285=488&286=492&287=494&288=496&289=498&290=500&291=502&293=505&298=509&299=511&300=513&301=515&303=518&305=520&308=523&310=529&312=532&315=535&316=538&318=540&319=543&321=545&322=547&323=551&326=554&327=557&328=559&329=561&330=565&334=568&335=571'