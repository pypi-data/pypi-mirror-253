# coding=utf-8
import pika
import functools
import threading
from .config import sca_config

class BaseRabbit(object):

    def __init__(self, **kwargs):
        self._host = kwargs.get('host', sca_config("rabbit", "host"))
        self._port = kwargs.get('port', sca_config("rabbit", "port"))
        self._user = kwargs.get('user', sca_config("rabbit", "user"))
        self._password = kwargs.get('password', sca_config("rabbit", "password"))
        self._exchange = kwargs.get('exchange', sca_config("rabbit", "exchange"))
        self._connection = None
        self._channel = None
        self._caller = None
        self.no_ack = False

    def init_connection(self):
        credentials = pika.PlainCredentials(self._user, self._password)
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(self._host, self._port, '/', credentials, heartbeat=600, blocked_connection_timeout=300))
        self._channel = self._connection.channel()

    def check_connection(self):
        if not self._connection or not self._connection.is_open:
            self.init_connection()

    def close_connection(self):
        if self._connection:
            try:
                self._connection.close()
            except:
                pass
            self._connection = None


class RabbitProducer(BaseRabbit):

    def execute(self, topic, message, need_close=False, **kwargs):
        self.check_connection()
        routing_key = kwargs.get('routing_key', topic)
        self._channel.queue_declare(queue=topic, durable=True)
        self._channel.basic_publish(exchange=self._exchange,
                                    routing_key=routing_key,
                                    body=message)
        if need_close:
            self.close_connection()


class RabbitConsumer(BaseRabbit):

    def execute(self, topic, caller, prefetch_count=1, no_ack=False):
        self._caller = caller
        self.no_ack = no_ack
        self.check_connection()
        self._channel.queue_declare(queue=topic, durable=True)
        self._channel.basic_qos(prefetch_count=prefetch_count)
        self._channel.basic_consume(topic, self.callback,
                                    auto_ack=no_ack)
        self._channel.start_consuming()
    
    def execute_once(self, topic, caller, no_ack=False):
        self._caller = caller
        self.check_connection()
        self._channel.queue_declare(queue=topic, durable=True)
        mframe, hframe, body = self._channel.basic_get(queue=topic, auto_ack=no_ack)
        if body is not None:
            caller(body.decode())
            if not no_ack:
                self._channel.basic_ack(delivery_tag=mframe.delivery_tag)
        self.close_connection()
        return body is not None
    
    def callback(self, ch, method, properties, body):
        self._caller(body)
        if not self.no_ack:
            ch.basic_ack(delivery_tag=method.delivery_tag)
    
    def _ack_message(self, ch, delivery_tag):
        if ch.is_open:
            ch.basic_ack(delivery_tag)
        else:
            pass

    def execute_with_thread_ack(self, topic, caller, prefetch_count=1, no_ack=False):
        threads = []
        self._caller = caller
        self.check_connection()
        self._channel.queue_declare(queue=topic, durable=True)
        self._channel.basic_qos(prefetch_count=prefetch_count)
        on_message_callback = functools.partial(self.on_message, args=(threads))
        self._channel.basic_consume(queue=topic, on_message_callback=on_message_callback, auto_ack=no_ack)
        self._connection.process_data_events()
        try:
            self._channel.start_consuming()
        except KeyboardInterrupt:
            self._channel.stop_consuming()
        for thread in threads:
            thread.join()
        self.close_connection()
    
    def on_message(self, ch, method_frame, _header_frame, body, args):
        thrds = args
        delivery_tag = method_frame.delivery_tag
        t = threading.Thread(target=self._do_work, args=(ch, delivery_tag, body))
        t.start()
        thrds.append(t)

    def _do_work(self, ch, delivery_tag, body):
        self._caller(body.decode())
        cb = functools.partial(self._ack_message, ch, delivery_tag)
        ch.connection.add_callback_threadsafe(cb)
        return

