from cloudframework.RESTFul import RESTFul
import os
class API(RESTFul):

    def main(self):
        res = {
            "Description": "Hello World",
            "Version": self.core.version,
            "request.form": self.formParams,
            "system.url": self.core.system.url,
            "core.errors": self.core.errors.data
        }

        res = {
            "self.core.version": self.core.version,
            "self.core.system.root_path": self.core.system.root_path if self.core.isThis.development() else 'production-server/*****',
            "self.core.isThis.development()": self.core.isThis.development(),
            "self.core.isThis.production()": self.core.isThis.production(),
            "self.core.system.url": self.core.system.url,
            "self.formParams": self.formParams,
            "self.core.errors.data": self.core.errors.data,
        }
        self.addReturnData(res)
