# -*- encoding: utf-8 -*-
import json
import logging

import pika
from zerocs.rabbit import RabbitMq


def print_exception(e):
    logging.error(e)


@RabbitMq
class _RabbitMq:
    mq_channel = None
    config_key = 'RABBITMQ_CONFIG'

    @staticmethod
    def get_mq_channel(host, user, passwd, port):
        credentials = pika.PlainCredentials(user, passwd)
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host, port=port, virtual_host='/', credentials=credentials, heartbeat=0))
        RabbitMq.mq_channel = connection.channel()

    @staticmethod
    def rabbitmq_init(config):
        host = config.split('@')[1].split(':')[0]
        port = config.split('@')[1].split(':')[1]

        user = config.split('@')[0].split('//')[1].split(':')[0]
        passwd = config.split('@')[0].split('//')[1].split(':')[1]
        try:
            RabbitMq.get_mq_channel(host, user, passwd, port)
        except Exception as e:
            print_exception(e)

    @staticmethod
    def update(subject):
        config = subject.get_configs()
        if RabbitMq.config_key in config:
            mq_config = config.get(RabbitMq.config_key)
            RabbitMq.rabbitmq_init(mq_config)

    @staticmethod
    def create_queue(queue):
        try:
            RabbitMq.mq_channel.queue_declare(queue=queue)
        except Exception as e:
            print_exception(e)

    @staticmethod
    def send_message(queue, message):
        RabbitMq.create_queue(queue=queue)
        if type(message) is not str:
            message = json.dumps(message)
        RabbitMq.mq_channel.basic_publish(exchange='', routing_key=queue, body=message)

    @staticmethod
    def get_message(queue, callback):
        RabbitMq.create_queue(queue=queue)
        RabbitMq.mq_channel.basic_consume(on_message_callback=callback, queue=queue)
        RabbitMq.mq_channel.start_consuming()
