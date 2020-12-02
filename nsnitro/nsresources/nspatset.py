from .nsbaseresource import NSBaseResource
 
__author__ = 'subbaraoathota'
 
 
class NSPatset(NSBaseResource):
 
    # Configuration for content-switching policy resource.
 
    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """
        super(NSPatset, self).__init__()
        self.options = {'name': '',
                        'comment': '',
                        'indextype': '',
	                'description': '',
                        '__count': ''}
 
        self.resourcetype = NSPatset.get_resourcetype()
 
        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]
 
    @staticmethod
    def get_resourcetype():
        return "policypatset"
 
    def set_name(self, name):
        self.options['name'] = name

    def get_name(self):
        return self.options['name']
 
    def get_indextype(self):
        return self.options['indextype']
 
    def set_indextype(self, indextype):
        self.options['indextype'] = indextype
 
    def get_comment(self):
        return self.options['comment']
 
    def set_comment(self, comment):
        self.options['comment'] = comment
 
    def get_description(self):
        return self.options['description']
 
    # Operations methods
    @staticmethod
    def get(nitro, policypatset):
        """
        Use this API to fetch patset resource of given name.
        """
        __policypatset = NSPatset()
        __policypatset.set_name(policypatset.get_name())
        __policypatset.get_resource(nitro, policypatset.get_name())
        return __policypatset
 
    @staticmethod
    def get_all(nitro):
        """
        Use this API to fetch all configured patset resources.
        """
        __url = nitro.get_url() + NSPatset.get_resourcetype()
        __json_policypatsets = nitro.get(__url).get_response_field(NSPatset.get_resourcetype())
        __policypatsets = []
        for json_policypatset in __json_policypatsets:
            __policypatsets.append(NSPatset(json_policypatset))
        return __policypatsets
 
    @staticmethod
    def add(nitro, policypatset):
        """
        Use this API to add patset.
        """
        __policypatset = NSPatset()
        __policypatset.set_name(policypatset.get_name())
        return __policypatset.add_resource(nitro)
 
    @staticmethod
    def delete(nitro, policypatset):
        """
        Use this API to delete patset of a given name.
        """
        __policypatset = NSPatset()
        __policypatset.set_name(policypatset.get_name())
        return __policypatset.delete_resource(nitro)
