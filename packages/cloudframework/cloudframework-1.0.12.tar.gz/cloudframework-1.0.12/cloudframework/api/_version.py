from cloudframework.RESTFul import RESTFul
import os
class API(RESTFul):

    def main(self):
        res = {
            "self.core.version": self.core.version,
            "self.core.isThis.development()": self.core.isThis.development(),
            "self.core.isThis.production()": self.core.isThis.production(),
        }
        self.addReturnData(res)
