from rest_framework import permissions
from .shortcuts import get_current_site

class IsOwnerOrReadOnly(permissions.BasePermission):

	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True

		site = get_current_site(request)
		return (request.user.is_authenticated and request.user.is_staff)

	def has_object_permission(self, request, view, obj):	
		if request.method in permissions.SAFE_METHODS:
			return True

		site = get_current_site(request)
		return site and request.user.is_staff and \
			((hasattr(obj, 'site') and obj.site == site) \
				or \
			(hasattr(obj, 'page') and obj.page.site == site))
