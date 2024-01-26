# -*- encoding: utf-8 -*-
import json
import multiprocessing
import sys
from argparse import ArgumentParser

from zerocs.config import Config
from zerocs.build import WorkBuild
from zerocs.rabbit import RabbitMq
from zerocs.database import MongoDB
from zerocs.observer import ObserverBase
from zerocs.logger import AsynchronousLog
from zerocs.utils import GetClusterRpcProxy, ZeroProxy, Utils


class MultiProcess:

    def __init__(self, function, work_name, work_ip, config):
        self.function = function
        self.work_name = work_name
        self.work_ip = work_ip
        self.config = config

    def run_task_func(self, function, task_data):
        MongoDB.init(self.config.get('MONGODB_CONFIG'))
        RabbitMq.rabbitmq_init(self.config.get('RABBITMQ_CONFIG'))
        logger = AsynchronousLog.init_asynchronous_log(self.work_name, self.work_ip)
        rpc_obj = GetClusterRpcProxy.get_cluster_rpc_proxy({"AMQP_URI": self.config.get('RABBITMQ_CONFIG')})

        setattr(function, 'logger', logger)
        setattr(function, 'rpc_obj', rpc_obj)
        setattr(function, 'work_ip', self.work_ip)
        setattr(function, 'work_name', self.work_name)
        setattr(function, 'rpc_proxy', ZeroProxy)

        try:
            function(task_data)
        except Exception as e:
            logger.error(f'{e}')

        MongoDB.delete_run_task(service_name=self.work_name, service_ip=self.work_ip, task_id=task_data['task_id'])

    def mq_callback(self, ch, method, properties, body):
        ch.basic_ack(delivery_tag=method.delivery_tag)
        task_data = json.loads(body.decode())
        if 'task_id' in task_data:
            _server = MongoDB.get_service_by_name_and_ip(service_name=self.work_name, service_ip=self.work_ip)
            _max_work = _server.get('max_work')
            _run_work = len(_server.get('run_work'))

            if _run_work < _max_work:
                _stops = MongoDB.get_stop_tasks_by_task_id(task_data['task_id'])
                if len(_stops) < 1:
                    MongoDB.update_run_task(
                        service_name=self.work_name, service_ip=self.work_ip, task_id=task_data['task_id'])

                    process = multiprocessing.Process(
                        target=self.run_task_func,
                        args=(self.function, task_data,)
                    )
                    process.start()
            else:
                ch.basic_publish(body=body, exchange='', routing_key=self.work_name)

    def start_work(self):
        RabbitMq.get_message(self.work_name, self.mq_callback)


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('--CONFIG', '-CONFIG', help='CONFIG')

    args = parser.parse_args()
    config = Utils.get_b64decode(args.CONFIG)
    config = json.loads(config)

    sys.path.insert(0, config.get('PATH'))

    Config.set_configs(config)
    ObserverBase.attach(Config, subject=RabbitMq)
    ObserverBase.attach(Config, subject=MongoDB)
    ObserverBase.notify(Config)

    module = __import__(config.get('SERVICE_PATH'), globals=globals(), locals=locals(), fromlist=['RpcFunction'])
    func = WorkBuild.build(func=module.WorkFunction, rabbitmq_config=config.get('RABBITMQ_CONFIG'))

    _work_ip = func.__dict__.get("work_ip")
    _work_name = func.__dict__.get("work_name")

    obj = MultiProcess(
        function=func,
        work_ip=_work_ip,
        config=config,
        work_name=_work_name
    )
    obj.start_work()
