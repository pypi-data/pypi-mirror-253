from djangoldp.filters import NoFilterBackend
from djangoldp.permissions import LDPBasePermission
from djangoldp.utils import is_anonymous_user

class JoinCirclePermission(LDPBasePermission):
    filter_backend = None
    def has_permission(self, request:object, view:object) -> bool:
        if is_anonymous_user(request.user):
            return False
        return request.method == 'PATCH'

    def check_patch(self, first, second, user):
        diff = first - second
        return diff == set() or diff == {user.urlid}

    def has_object_permission(self, request:object, view:object, circle:object) -> bool:
        '''only accept patch request, only if the only difference on the user_set is the user'''
        if not self.has_permission(request, view) or not circle or not 'user_set' in request.data:
            return False
        new_members = request.data['user_set']
        if not isinstance(new_members, list):
            new_members = [new_members]
        new_ids = {user['@id'] for user in new_members}
        old_ids = {user.urlid for user in circle.members.user_set.all()}
        return self.check_patch(new_ids, old_ids, request.user) and self.check_patch(old_ids, new_ids, request.user)