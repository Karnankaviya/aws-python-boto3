def get_available_resources(self):
    return self._loader.list_available_services(type_name='S3')

get_available_resources("S3")