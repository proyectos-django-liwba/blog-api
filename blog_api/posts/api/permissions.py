from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # si el metodo es seguro, retornar true
        if request.method == "GET":
            return True
        
        # si usuario es tipo staff, retornar true si el usuario es admin
        return request.user.is_staff
    
# staff: es un usuario que puede acceder al admin