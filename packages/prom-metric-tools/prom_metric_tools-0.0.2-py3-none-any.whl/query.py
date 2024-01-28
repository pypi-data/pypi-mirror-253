import yaml
from tqdm import tqdm
from datetime import datetime
from prometheus_api_client import PrometheusConnect, MetricRangeDataFrame

class QueryExecutor:
    
    def __init__(self, conf, *, headers={}) -> None:
        self.__dateformat = "%Y-%m-%dT%H:%M:%S"
        self.conf = yaml.load(open(conf, 'r'), Loader=yaml.FullLoader)
        print(self.conf['prometheus']['proto'])
        print(self.conf['prometheus']['url'])
        print(self.conf['prometheus']['port'])
        self.prom = PrometheusConnect(
            url=self.__build_url(
                str(self.conf['prometheus']['proto']),
                str(self.conf['prometheus']['url']),
                str(self.conf['prometheus']['port'])
            ),
            disable_ssl=True,
            headers=headers
        )
    
    def __build_url(self, proto, url, port):
        return proto + '://' + url + ':' + port

    def execute(self, output_path):
        results = []
        for metric in tqdm(self.conf['metrics']):
            metric_data = self.prom.custom_query_range(
                query=metric['query'],
                start_time=datetime.strptime(metric["start_time"], self.__dateformat),
                end_time=datetime.strptime(metric["end_time"], self.__dateformat),
                step=metric['step']
            )
            results.append(metric_data)
            metric_df = MetricRangeDataFrame(metric_data)
            metric_df.to_csv(output_path + '/' + metric['name']+'.csv')
    
