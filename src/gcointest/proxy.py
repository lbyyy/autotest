
import time
import json
import decimal

from fabric.api import run
from fabric.context_managers import settings

from gcointest.exceptions import JSONRPCException, CoreException
from gcointest import config


class AuthServiceProxy(object):

    def __init__(self, host, exception_wrapper=None):
        self.host = host
        self._exception_wrapper = exception_wrapper

    def __getattr__(self, name):
        return RPCMethod(name, self)

    def _raise_exception(self, error):
        if self._exception_wrapper is None:
            raise JSONRPCException(error)
        else:
            raise self._exception_wrapper(error)

    def start(self):
        command = (('$HOME/opensource/src/gcoind -daemon -reindex -logip -debug -datadir=' +
                    self.host.split('_')[3] +
                  ' -port={0} -rpcport={1} -rpcthreads={2}').format(self.host.split('_')[1], self.host.split('_')[2], config.rpcthreads))
        resp = run(command)

        if resp.failed:
            raise CoreException("bitcoind launch failed", self.host)

    def reset(self):
        time.sleep(3)
        command = ("rm -rf " + self.host.split('_')[3] + '/gcoin')
        with settings(warn_only=True):
            return run(command)


class RPCMethod(object):

    def __init__(self, name, service_proxy):
        self._method_name = name
        self._service_proxy  = service_proxy

    def __call__(self, *args, **kwargs):
        warn_only = kwargs.pop("warn_only", False)

        parameter = ' '.join(str(i) for i in args)
        command = ('$HOME/opensource/src/gcoin-cli -datadir=' + self._service_proxy.host.split('_')[3] + '  {method} {param}').format(method=self._method_name,
                                                                               param = parameter)
        with settings(warn_only=True):
            f = open(self._service_proxy.host.split('_')[0] + self._service_proxy.host.split('_')[1] + '.txt','a')
            f.write(command + '\n')
            f.close()
            resp = run(command)

        if resp.find("error") != -1 and not warn_only:
            resp = resp.split("error: ")[1]

            if resp.find("Loading wallet...") != -1 or resp.find("Loading block index...") != -1:
                raise CoreException(resp, self._service_proxy.host)

            try:
                self._service_proxy._raise_exception(json.loads(resp))
            except ValueError:
                raise CoreException(resp, self._service_proxy.host)

        try:
            resp = json.loads(resp, parse_float=decimal.Decimal)
        except ValueError:
            pass
        return resp

    def __repr__(self):
        return '<RPCMethod object "{name}">'.format(name=self._method_name)

