from .stopwatch import Stopwatch
from .gauge import Gauge
from .calculation import Calculation
from .rate import Rate
from .metric import Metric
from is_numeric import is_numeric

_registry = {}


class Statman():

    def __init__(self):
        pass

    @staticmethod
    def reset():
        '''Clears all metrics from the registry.'''
        _registry.clear()

    @staticmethod
    def count() -> int:
        '''Returns a count of the registered metrics.'''
        return len(Statman.metric_registry().keys())

    @staticmethod
    def stopwatch(name: str = None, autostart: bool = False, initial_delta: float = None, enable_history=False) -> Stopwatch:
        ''' Returns a stopwatch instance.  If there is a registered stopwatch with this name, return it.  If there is no registered stopwatch with this name, create a new instance, register it, and return it. '''
        sw = Statman.metric_registry().get(name)

        if not sw:
            sw = Stopwatch(name=name, autostart=autostart, initial_delta=initial_delta, enable_history=enable_history)

        if not name is None:
            Statman.register(name, sw)

        return sw

    @staticmethod
    def gauge(name: str = None, value: float = 0) -> Gauge:
        ''' Returns a stopwatch instance.  If there is a registered stopwatch with this name, return it.  If there is no registered stopwatch with this name, create a new instance, register it, and return it. '''
        g = Statman.get(name)

        if not g:
            g = Gauge(name=name, value=value)

        if not name is None:
            Statman.register(name, g)

        return g

    @staticmethod
    def calculation(name: str = None, function=None) -> Calculation:
        ''' Returns a numeric calculation instance.  If there is a registered calculation with this name, return it.  If there is no registered calculation with this name, create a new instance, register it, and return it. '''
        c = Statman.metric_registry().get(name)

        if not c:
            c = Calculation(name=name, function=function)

        if not name is None:
            Statman.register(name, c)

        return c

    @staticmethod
    def rate(name: str = None, numerator_metric_name: str = None, denominator_metric_name: str = None) -> Rate:
        ''' Returns a numeric rate calculation instance.  If there is a registered metric with this name, return it.  If there is no registered metric with this name, create a new instance, register it, and return it. '''
        r = Statman.metric_registry().get(name)

        if not r:
            r = Rate(name=None, numerator_metric_name=numerator_metric_name, denominator_metric_name=denominator_metric_name)

        if not name is None:
            Statman.register(name, r)

        return r

    @staticmethod
    def register(name: str, metric: Metric):
        '''Manually register a new metric.'''
        Statman.metric_registry()[name] = metric

    @staticmethod
    def get(name: str) -> Metric:
        metric = None
        if name:
            metric = Statman.metric_registry().get(name)
        return metric

    @staticmethod
    def metric_registry() -> dict:
        metric_registry = _registry.get('metric-registry')
        if not metric_registry:
            _registry['metric-registry'] = {}
            metric_registry = _registry.get('metric-registry')
        return metric_registry

    @staticmethod
    def get_external_source(name: str) -> Metric:
        external_source = None
        if name:
            external_source = Statman.external_source_registry().get(name)
        return external_source

    @staticmethod
    def external_source_registry() -> dict:
        metric_registry = _registry.get('external-source-registry')
        if not metric_registry:
            _registry['external-source-registry'] = {}
            metric_registry = _registry.get('external-source-registry')
        return metric_registry

    @staticmethod
    def register_external_source(name: str, external_source: "ExternalSource"):
        '''Manually register an external source.'''
        Statman.external_source_registry()[name] = external_source

    @staticmethod
    def refresh_external_sources():
        for external_source_key in Statman.external_source_registry():
            external_source = Statman.get_external_source(external_source_key)
            external_source.refresh()

    @staticmethod
    def external_source(name: str, function=None) -> "ExternalSource":
        ''' Registers an external source '''
        s = Statman.get_external_source(name)

        if not s:
            if not function:
                raise Exception('Must provide a valid external source name or function')

            s = ExternalSource(name=name, function=function)

        Statman.register_external_source(name, s)

        return s

    @staticmethod
    def report(output_stdout: bool = False, log_method=None):
        output = []
        report_header = 'statman metric report:'
        line_delimiter = '\n'
        prefix = '- '

        Statman.refresh_external_sources()

        output.append(report_header)
        for metric in Statman.metric_registry().copy():
            output.append(prefix + Statman.get(metric).report(output_stdout=False))

        for line in output:
            if output_stdout:
                print(line)

            if log_method:
                log_method(line)

        return line_delimiter.join(output)


class ExternalSource():
    _function = None
    _name = None

    def __init__(self, name: str, function):
        self._function = function
        self._name = name
        self.refresh()

    def refresh(self):
        try:
            f = self.refresh_function
            result = f()

            if isinstance(result, dict):
                for key in result:
                    value = result.get(key)
                    statman_key = f'{self._name}.{key}'
                    if isinstance(value, (float, int)):
                        Statman.gauge(statman_key).value = value
                    elif isinstance(value, str) and is_numeric(value):
                        value = float(value)
                        Statman.gauge(statman_key).value = value
                    else:
                        # print(f'skipping non-numeric value {key=} {value=} {statman_key=}')
                        pass
            else:
                if isinstance(value, int) or isinstance(value, float):
                    # print(f'skipping non-dictionary, numeric {result=}')
                    pass
                else:
                    # print(f'skipping non-dictionary, non-numeric {result=}')
                    pass

        except Exception as e:
            # print(f'failed to execute refresh method [{self._name}][{e}]')
            raise e

    @property
    def refresh_function(self):
        return self._function

    # @refresh_function.setter
    # def refresh_function(self, function):
    #     self._function = function
