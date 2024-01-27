from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/flow-tracking.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_flow_tracking = resolve('flow_tracking')
    l_0_hardware_offload_protocols = resolve('hardware_offload_protocols')
    try:
        t_1 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_2 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled')):
        pass
        yield '!\nflow tracking sampled\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'sample')):
            pass
            yield '   sample '
            yield str(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'sample'))
            yield '\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'hardware_offload')):
            pass
            l_0_hardware_offload_protocols = []
            context.vars['hardware_offload_protocols'] = l_0_hardware_offload_protocols
            context.exported_vars.add('hardware_offload_protocols')
            if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'hardware_offload'), 'ipv4'), True):
                pass
                context.call(environment.getattr((undefined(name='hardware_offload_protocols') if l_0_hardware_offload_protocols is missing else l_0_hardware_offload_protocols), 'append'), 'ipv4')
            if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'hardware_offload'), 'ipv6'), True):
                pass
                context.call(environment.getattr((undefined(name='hardware_offload_protocols') if l_0_hardware_offload_protocols is missing else l_0_hardware_offload_protocols), 'append'), 'ipv6')
            if (t_2((undefined(name='hardware_offload_protocols') if l_0_hardware_offload_protocols is missing else l_0_hardware_offload_protocols)) > 0):
                pass
                yield '   hardware offload '
                yield str(t_1(context.eval_ctx, (undefined(name='hardware_offload_protocols') if l_0_hardware_offload_protocols is missing else l_0_hardware_offload_protocols), ' '))
                yield '\n'
            if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'hardware_offload'), 'threshold_minimum')):
                pass
                yield '   hardware offload threshold minimum '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'hardware_offload'), 'threshold_minimum'))
                yield ' samples\n'
        for l_1_tracker in environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'trackers'):
            _loop_vars = {}
            pass
            yield '   tracker '
            yield str(environment.getattr(l_1_tracker, 'name'))
            yield '\n'
            if t_3(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_inactive_timeout')):
                pass
                yield '      record export on inactive timeout '
                yield str(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_inactive_timeout'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_interval')):
                pass
                yield '      record export on interval '
                yield str(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_interval'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'mpls'), True):
                pass
                yield '      record export mpls\n'
            if t_3(environment.getattr(l_1_tracker, 'exporters')):
                pass
                for l_2_exporter in environment.getattr(l_1_tracker, 'exporters'):
                    l_2_collector_cli = resolve('collector_cli')
                    _loop_vars = {}
                    pass
                    yield '      exporter '
                    yield str(environment.getattr(l_2_exporter, 'name'))
                    yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'host')):
                        pass
                        l_2_collector_cli = str_join(('collector ', environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'host'), ))
                        _loop_vars['collector_cli'] = l_2_collector_cli
                        if t_3(environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'port')):
                            pass
                            l_2_collector_cli = str_join(((undefined(name='collector_cli') if l_2_collector_cli is missing else l_2_collector_cli), ' port ', environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'port'), ))
                            _loop_vars['collector_cli'] = l_2_collector_cli
                        yield '         '
                        yield str((undefined(name='collector_cli') if l_2_collector_cli is missing else l_2_collector_cli))
                        yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_2_exporter, 'format'), 'ipfix_version')):
                        pass
                        yield '         format ipfix version '
                        yield str(environment.getattr(environment.getattr(l_2_exporter, 'format'), 'ipfix_version'))
                        yield '\n'
                    if t_3(environment.getattr(l_2_exporter, 'local_interface')):
                        pass
                        yield '         local interface '
                        yield str(environment.getattr(l_2_exporter, 'local_interface'))
                        yield '\n'
                    if t_3(environment.getattr(l_2_exporter, 'template_interval')):
                        pass
                        yield '         template interval '
                        yield str(environment.getattr(l_2_exporter, 'template_interval'))
                        yield '\n'
                l_2_exporter = l_2_collector_cli = missing
            if t_3(environment.getattr(l_1_tracker, 'table_size')):
                pass
                yield '      flow table size '
                yield str(environment.getattr(l_1_tracker, 'table_size'))
                yield ' entries\n'
        l_1_tracker = missing
        if t_3(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'sampled'), 'shutdown'), False):
            pass
            yield '   no shutdown\n'
    if t_3(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'hardware')):
        pass
        yield '!\nflow tracking hardware\n'
        for l_1_tracker in environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'hardware'), 'trackers'):
            _loop_vars = {}
            pass
            yield '   tracker '
            yield str(environment.getattr(l_1_tracker, 'name'))
            yield '\n'
            if t_3(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_inactive_timeout')):
                pass
                yield '      record export on inactive timeout '
                yield str(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_inactive_timeout'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_interval')):
                pass
                yield '      record export on interval '
                yield str(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'on_interval'))
                yield '\n'
            if t_3(environment.getattr(environment.getattr(l_1_tracker, 'record_export'), 'mpls'), True):
                pass
                yield '      record export mpls\n'
            if t_3(environment.getattr(l_1_tracker, 'exporters')):
                pass
                for l_2_exporter in environment.getattr(l_1_tracker, 'exporters'):
                    l_2_collector_cli = resolve('collector_cli')
                    _loop_vars = {}
                    pass
                    yield '      exporter '
                    yield str(environment.getattr(l_2_exporter, 'name'))
                    yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'host')):
                        pass
                        l_2_collector_cli = str_join(('collector ', environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'host'), ))
                        _loop_vars['collector_cli'] = l_2_collector_cli
                        if t_3(environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'port')):
                            pass
                            l_2_collector_cli = str_join(((undefined(name='collector_cli') if l_2_collector_cli is missing else l_2_collector_cli), ' port ', environment.getattr(environment.getattr(l_2_exporter, 'collector'), 'port'), ))
                            _loop_vars['collector_cli'] = l_2_collector_cli
                        yield '         '
                        yield str((undefined(name='collector_cli') if l_2_collector_cli is missing else l_2_collector_cli))
                        yield '\n'
                    if t_3(environment.getattr(environment.getattr(l_2_exporter, 'format'), 'ipfix_version')):
                        pass
                        yield '         format ipfix version '
                        yield str(environment.getattr(environment.getattr(l_2_exporter, 'format'), 'ipfix_version'))
                        yield '\n'
                    if t_3(environment.getattr(l_2_exporter, 'local_interface')):
                        pass
                        yield '         local interface '
                        yield str(environment.getattr(l_2_exporter, 'local_interface'))
                        yield '\n'
                    if t_3(environment.getattr(l_2_exporter, 'template_interval')):
                        pass
                        yield '         template interval '
                        yield str(environment.getattr(l_2_exporter, 'template_interval'))
                        yield '\n'
                l_2_exporter = l_2_collector_cli = missing
            if t_3(environment.getattr(l_1_tracker, 'table_size')):
                pass
                yield '      flow table size '
                yield str(environment.getattr(l_1_tracker, 'table_size'))
                yield ' entries\n'
        l_1_tracker = missing
        if t_3(environment.getattr(environment.getattr((undefined(name='flow_tracking') if l_0_flow_tracking is missing else l_0_flow_tracking), 'hardware'), 'shutdown'), False):
            pass
            yield '   no shutdown\n'

blocks = {}
debug_info = '8=31&11=34&12=37&14=39&15=41&16=44&17=46&19=47&20=49&22=50&23=53&25=55&26=58&29=60&30=64&31=66&32=69&34=71&35=74&37=76&40=79&41=81&42=86&43=88&44=90&45=92&46=94&48=97&50=99&51=102&53=104&54=107&56=109&57=112&61=115&62=118&65=121&70=124&73=127&74=131&75=133&76=136&78=138&79=141&81=143&84=146&85=148&86=153&87=155&88=157&89=159&90=161&92=164&94=166&95=169&97=171&98=174&100=176&101=179&105=182&106=185&109=188'