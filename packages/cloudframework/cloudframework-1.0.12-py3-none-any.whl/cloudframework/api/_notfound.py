from cloudframework.RESTFul import RESTFul
class API(RESTFul):

    def main(self):
        return self.setErrorFromCodeLib('not-found', 'The following api route does not exist: /'+self.core.system.url['parts'][0])
