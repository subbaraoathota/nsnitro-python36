from .nsbaseresource import NSBaseResource
__author__ = 'Aleksandar Topuzovic'


class NSLBVServerCSVserverBinding(NSBaseResource):

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSLBVServerCSVserverBinding, self).__init__()
        self.options = {'name': '',
                        'lbvserver': '',
                        'targetvserver': '',
                        'hits': '',
                        '__count': ''}

        if not (json_data is None):
            for key in list(json_data.keys()):
                if key in list(self.options.keys()):
                    self.options[key] = json_data[key]

        self.resourcetype = NSLBVServerCSVserverBinding.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        """
        Binding object showing the csvserver that can be bound to lbvserver.
        """
        return "csvserver_lbvserver_binding"

    # Read/write properties
    def set_lbvserver(self, lbvserver):
        """
        lbvserver.
        """
        self.options['lbvserver'] = lbvserver

    def get_lbvserver(self):
        """
        lbvserver.
        """
        return self.options['lbvserver']

    def set_name(self, name):
        """
        The virtual server name to which the service is bound.
        Minimum length = 1
        """
        self.options['name'] = name

    def get_name(self):
        """
        The virtual server name to which the service is bound.
        Minimum length = 1
        """
        return self.options['name']

    def set_targetvserver(self, targetvserver):
        """
         virtual server.
        """
        self.options['targetvserver'] = targetvserver

    def get_targetvserver(self):
        """
         virtual server.
        """
        return self.options['targetvserver']

    # Read only properties
    def get_hits(self):
        """
        Number of hits.
        """
        return self.options['hits']

    @staticmethod
    def get(nitro, lbvservercsvserverbinding):
        """
        Use this API to fetch lb vserver cs vserver binding resource of given name.
        """
        __url = nitro.get_url() + NSLBVServerCSVserverBinding.get_resourcetype() + "/" + lbvservercsvserverbinding.get_name()
        __json_csvservers = nitro.get(__url).get_response_field(NSLBVServerCSVserverBinding.get_resourcetype())
        __csvservers = []
        for json_csvserver in __json_csvservers:
            __csvservers.append(NSLBVServerCSVserverBinding(json_csvserver))
        return __csvservers

    def add(nitro, csvserver_lbvserver_binding):
        """
        Use this API to add csvserver_lbverser_binding.
        """
        __csvserver_lbvserver_binding = NSLBVServerCSVserverBinding()
        __csvserver_lbvserver_binding.set_name(csvserver_lbvserver_binding.get_name())
        __csvserver_lbvserver_binding.set_lbvserver(csvserver_lbvserver_binding.get_lbvserver())
        __csvserver_lbvserver_binding.set_targetvserver(csvserver_lbvserver_binding.get_targetvserver())
        return __csvserver_lbvserver_binding.update_resource(nitro)

    def delete(nitro, csvserver_lbvserver_binding):
        """
        Use this API to delete csvserver_lbverser_binding.
        """
        __csvserver_lbvserver_binding = NSLBVServerCSVserverBinding()
        __csvserver_lbvserver_binding.set_name(csvserver_lbvserver_binding.get_name())
        __csvserver_lbvserver_binding.set_lbvserver(csvserver_lbvserver_binding.get_lbvserver())
        __csvserver_lbvserver_binding.set_targetvserver(csvserver_lbvserver_binding.get_targetvserver())
        return __csvserver_lbvserver_binding.delete_resource(nitro)
