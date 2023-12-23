from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)

    
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     # the permission are not having very good effect as they are being used in the list create view which give acess to do anything once you give access to 
    #     # even one of the methods
    #     if user.is_staff:
    #         # app_name.verb_model_name
    #         if user.has_perm("products.add_product"):# this is predefined and we have to look for this 
    #             return True
    #         if user.has_perm("products.view_product"):# this is predefined and we have to look for this 
    #             return True
    #         if user.has_perm("products.change_product"):# this is predefined and we have to look for this 
    #             return True
    #         if user.has_perm("products.delete_product"):# this is predefined and we have to look for this 
    #             return True
    #         # these permission are mostly based in the models that we have registered with the admin portal.
    #         return False 
    #     return False
    
# This is the way we define permissions for various users involved in our project using functions
    