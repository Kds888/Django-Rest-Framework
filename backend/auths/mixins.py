from . permissions import IsStaffEditorPermission
from rest_framework import permissions

class StaffEditorPermissionMixin():
    permission_classes=[
        permissions.IsAdminUser,IsStaffEditorPermission
    ]
    # NOw we have this permission mixin that we can use in any of our views.

class UserQuerysetMixin(): # this filter is working and we are able to sort the data based of given user.
    user_field='user'
    def get_queryset(self,*args,**kwargs):
        lookup_data={}
        lookup_data[self.user_field]=self.request.user.id
        qs= super().get_queryset(*args,**kwargs)
        return qs.filter(**lookup_data)
     
# similar to what we have defined in our views class of productlist create view