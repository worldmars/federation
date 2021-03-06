#!/usr/bin/env python3
import threading
import multiprocessing
from abc import ABC, abstractmethod

class Messenger(ABC):
    def __init__(self, nodes, my_id):
        self.nodes = nodes
        self.my_id = my_id
        pass

    @abstractmethod
    def produce_block(self):
        pass

    @abstractmethod
    def produce_sig(self):
        pass

    @abstractmethod
    def consume_block(self):
        pass

    @abstractmethod
    def consume_sigs(self):
        pass

    @abstractmethod
    def reconnect(self):
        pass
