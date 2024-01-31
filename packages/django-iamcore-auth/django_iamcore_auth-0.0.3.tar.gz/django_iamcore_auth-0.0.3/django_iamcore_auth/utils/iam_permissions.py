import logging

from iamcore.client.evaluete import authorize
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.request import Request

from ..settings import IAM_APPLICATION_NAME, IAM_TENANT_ID, IAM_ACCOUNT_NAME

logger = logging.getLogger(__name__)

METHOD_OPERATION_MAPPING_DEFAULT = {
    "POST": "create",
    "DELETE": "delete",
    "GET": "read",
    "PUT": "update",
    "PATCH": "update",
}


def action_adapter(application, resource_type, method, method_mapping):
    action = application
    if not resource_type:
        return action + ":*"
    action += ":" + resource_type

    if not method:
        return action + ":*"

    return action + ":" + method_mapping.get(method, "*")


def get_action(request, view, application, resource_type) -> str:
    if hasattr(view, "METHOD_ACTION_MAPPING") and isinstance(view.METHOD_ACTION_MAPPING, dict):
        return view.METHOD_ACTION_MAPPING.get(request.method)
    method_mapping = getattr(view, "METHOD_OPERATION_MAPPING", METHOD_OPERATION_MAPPING_DEFAULT)
    return action_adapter(application, resource_type, request.method, method_mapping)


class IAMTenantManagerPermissions(permissions.BasePermission):
    """Permissions Class that will check only resource type level permissions"""
    @classmethod
    def has_filtering_enabled(cls, request, view) -> bool:
        return hasattr(view, "HAS_QUERYSET_FILTERING_ENABLED")

    @classmethod
    def has_permission_disabled(cls, request, view) -> bool:
        if isinstance(view, (mixins.ListModelMixin, mixins.CreateModelMixin)) and not hasattr(view, "RESOURCE_ID"):
            return False
        if isinstance(view, (mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin)):
            return True
        return hasattr(view, "HAS_PERMISSION_DISABLED")


    @classmethod
    def has_permission(cls, request, view):
        if not hasattr(view, "RESOURCE_TYPE"):
            logger.error("Missing RESOURCE_TYPE attribute definition for model " + view.__class__)
            return False
        if cls.has_permission_disabled(request, view):
            logger.info("Going to skip has_permission because has_object_permission expected")
            return True

        resource_type = view.RESOURCE_TYPE
        action = get_action(request, view, IAM_APPLICATION_NAME, resource_type)
        tenant_id = _get_tenant_id(request, view, None)
        resource_path = _get_resource_path(request, view, None)
        resource_id = _get_resource_id(request, view, None)

        logger.info(
            "Going to check permissions for:"
            f" principal_irn={request.irn}"
            f" account_id={IAM_ACCOUNT_NAME}"
            f" application={IAM_APPLICATION_NAME}"
            f" tenant_id={tenant_id}"
            f" resource_type={resource_type}"
            f" resource_path={resource_path}"
            f" resource_ids=[{resource_id}]"
            f" action={action}"
        )
        if resource_id:
            request.resources_ids = authorize(
                authorization_headers=request.auth_headers,
                principal_irn=request.irn,
                account_id=IAM_ACCOUNT_NAME,
                application=IAM_APPLICATION_NAME,
                tenant_id=tenant_id,
                resource_type=resource_type,
                resource_path=resource_path,
                resource_ids=[resource_id],
                action=action
            )
            return True
        if cls.has_filtering_enabled(request, view):
            request.resources_ids = authorize(
                authorization_headers=request.auth_headers,
                principal_irn=request.irn,
                account_id=IAM_ACCOUNT_NAME,
                application=IAM_APPLICATION_NAME,
                tenant_id=tenant_id,
                resource_type=resource_type,
                resource_path=resource_path,
                action=action
            )
            return True
        return False

    @classmethod
    def has_object_permission(self, request: Request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        logger.info("Going to verify permissions by resource id")
        if not hasattr(view, "RESOURCE_TYPE"):
            logger.error("Missing RESOURCE_TYPE attribute definition for model " + view.__class__)
            return False
        resource_type = view.RESOURCE_TYPE

        tenant_id = _get_tenant_id(request, view, obj)
        resource_path = _get_resource_path(request, view, obj)
        resource_id = _get_resource_id(request, view, obj)
        action = get_action(request, view, IAM_APPLICATION_NAME, resource_type)
        logger.info(
            "Going to check permissions for:"
            f" principal_irn={request.irn}"
            f" account_id={IAM_ACCOUNT_NAME}"
            f" application={IAM_APPLICATION_NAME}"
            f" tenant_id={tenant_id}"
            f" resource_type={resource_type}"
            f" resource_path={resource_path}"
            f" resource_ids=[{resource_id}]"
            f" action={action}"
        )
        request.resources_ids = authorize(
            authorization_headers=request.auth_headers,
            principal_irn=request.irn,
            account_id=IAM_ACCOUNT_NAME,
            application=IAM_APPLICATION_NAME,
            tenant_id=tenant_id,
            resource_type=resource_type,
            resource_path=resource_path,
            action=action,
            resource_ids=[resource_id]
        )
        return True


def _get_tenant_id(request: Request, view, obj):
    if hasattr(view, "get_tenant_id") and callable(getattr(view, "get_tenant_id")):
        return view.get_tenant_id(request, obj)
    tenant_id_params = (
        'tenant_id', 'tenant-id', 'tenantId'
    )
    for param in tenant_id_params:
        if param in request.query_params.keys():
            return request.query_params.get(param)
    return IAM_TENANT_ID


def _get_resource_path(request: Request, view, obj):
    resource_path = ""
    if hasattr(view, "get_resource_path") and callable(getattr(view, "get_resource_path")):
        resource_path = view.get_resource_path(request, obj)
    elif obj and hasattr(obj, "get_resource_path") and callable(getattr(obj, "get_resource_path")):
        resource_path = obj.get_resource_path(request)
    return resource_path


def _get_resource_id(request: Request, view, obj):
    resource_id = ""
    if hasattr(view, "get_resource_id") and callable(getattr(view, "get_resource_id")):
        resource_id = view.get_resource_id(request, obj)
    elif obj and hasattr(obj, "get_resource_id") and callable(getattr(obj, "get_resource_id")):
        resource_id = obj.get_resource_id(request)
    elif hasattr(view, "RESOURCE_ID") and isinstance(getattr(view, "RESOURCE_ID"), str):
        resource_id = view.RESOURCE_ID
    return resource_id
