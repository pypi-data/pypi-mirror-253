import uuid
import yaml
import time

class Metric:
    def __init__(self) -> None:
        self.name = None
        self.query = None
        self.step = None
        self.start_time = None
        self.end_time = None
        self.id = uuid.uuid4()

    def get_id(self):
        return self.id


class ConfigGenerator:

    def __init__(self, *, proto=None, url=None, port=None, site=None) -> None:
        self.metrics = {}
        self.proto = proto
        self.url = url
        self.port = port
        self.site = site

    def set_prometheus_url(self, proto, url, port):
        self.proto = proto
        self.url = url
        self.port = port
        return True

    def get_prometheus_url(self):
        return "Prometheus url is not set" if self.proto is None or self.url is None or self.port is None else self.proto + '://' + self.url + ':' + self.port
    
    def get_metrics(self):
        return self.metrics

    def get_metric(self, id):
        return self.metrics[id]

    def _gen_metric(self, metric_params):
        metric = Metric()
        metric.name = metric_params['name']
        metric.query = metric_params['query']
        metric.step = metric_params['step']
        metric.start_time = metric_params['start_time']
        metric.end_time = metric_params['end_time']
        return metric

    def check_metric_params(self, metric_params):
        error_message = None
        for key,metric in metric_params.items():
            if metric is None:
                error_message = "Metric parameter --{}/-{} is not set".format(key,key[0])
                break
        return error_message is None, error_message
    
    def add_metric(self, metric_params):
        is_valid,error_message = self.check_metric_params(metric_params)
        if not is_valid:
            print(error_message)
            return False,error_message
   
        try:
            metric = self._gen_metric(metric_params)
            self.metrics[str(metric.get_id())] = metric
            return True, metric.get_id()
        except Exception as e:
            print(e)
            return False

    def delete_metric(self, metric_id):
        try:
            del self.metrics[metric_id]
            return True
        except Exception as e:
            print(e)
            return False

    def modify_metric(self, metric_id, metric_params):
        try:
            metric = self.get_metric(metric_id)
            metric.name = metric_params['name']
            metric.query = metric_params['query']
            metric.step = metric_params['step']
            metric.start_time = metric_params['start_time']
            metric.end_time = metric_params['end_time']

            return True, metric_id
        except Exception as e:
            print(e)
            return False

    def add_site(self, site):
        self.site = site

    def get_site(self):
        return "Site is not set" if self.site is None else self.site
    
    def check_config(self):
        return False if self.proto is None or self.url is None or self.port is None or self.site is None or len(self.metrics) == 0 else True

    def save_config(self):
        if not self.check_config():
            return False
        else:
            conf = {}
            conf['site'] = self.site
            conf['prometheus'] = {
                'proto': self.proto,
                'url': self.url,
                'port': self.port
            }
            conf['metrics'] = []
            for metric_id in self.metrics:
                metric = self.metrics[metric_id]
                conf['metrics'].append({
                    'name': metric.name,
                    'query': metric.query,
                    'step': metric.step,
                    'start_time': metric.start_time,
                    'end_time': metric.end_time
                })
            with open('metrics_{}.yaml'.format(time.time()), 'w') as f:
                yaml.dump(conf, f,sort_keys=False)
            return True
        
    def reset_config(self):
        self.metrics = {}
        self.proto = None
        self.url = None
        self.port = None
        self.site = None
        return True
    
    def get_config(self):
        return {
            'site': self.site,
            'prometheus': {
                'proto': self.proto,
                'url': self.url,
                'port': self.port
            },
            'metrics': self.metrics
        }