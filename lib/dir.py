import os


# validate and return the source dir
def get_abs_path(resource_dir):
    abs_resource_dir = os.path.abspath(resource_dir)

    if os.path.isdir(abs_resource_dir):
        return abs_resource_dir
    else:
        raise Exception('Invalid source directory.')


# get the list of resources
def get_resources_list(resource_dir):
    resources_list = []

    # get all files and folders from resource dir
    for resource in os.listdir(resource_dir):
        # check if it's a directory
        resource_abs_path = os.path.abspath(os.path.join(resource_dir, resource))
        if os.path.isdir(resource_abs_path):
            resources_list.append(tuple([resource, resource_abs_path]))

    return resources_list
