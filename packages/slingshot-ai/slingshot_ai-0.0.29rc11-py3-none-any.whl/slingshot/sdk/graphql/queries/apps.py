from __future__ import annotations

from pydantic import BaseModel, Field

from slingshot.sdk import backend_schemas

from ..base_graphql import BaseGraphQLQuery
from ..fragments import AppInstance


class AppInstancesResponse(BaseModel):
    app_instances: list[AppInstance] = Field(..., alias="appInstances")


class AppInstancesByAppSubTypeQuery(BaseGraphQLQuery[AppInstancesResponse]):
    _query = """
        query AppInstancesByAppSubType($appSubType: AppTypeEnumEnum!, $projectId: String!) {
            appInstances(where: {_and: {appSubType: {_eq: $appSubType}, projectId: {_eq: $projectId}}}) {
                ...AppInstance
            }
        }
    """

    _depends_on = [AppInstance]

    def __init__(self, app_sub_type: str, project_id: str):
        super().__init__(
            variables={"appSubType": app_sub_type, "projectId": project_id}, response_model=AppInstancesResponse
        )


class LatestAppInstanceForComponentQuery(BaseGraphQLQuery[AppInstancesResponse]):
    _query = """
        query LatestAppInstanceForComponentQuery($specId: String!) {
            appInstances(where: {specId: {_eq: $specId}}, orderBy: {createdAt: DESC}, limit: 1) {
                ...AppInstance
            }
        } """

    _depends_on = [AppInstance]

    def __init__(self, spec_id: str):
        super().__init__(variables={"specId": spec_id}, response_model=AppInstancesResponse)


class AppInstanceQuery(BaseGraphQLQuery[AppInstancesResponse]):
    _query = """
        query AppInstance($appInstanceId: String!, $projectId: String!) {
            appInstances(where: {_and: {appInstanceId: {_eq: $appInstanceId}, componentSpec: {projectId: {_eq: $projectId}}}}) {
                ...AppInstance
           }
        }
    """

    _depends_on = [AppInstance]

    def __init__(self, app_instance_id: str, project_id: str):
        super().__init__(
            variables={"appInstanceId": app_instance_id, "projectId": project_id}, response_model=AppInstancesResponse
        )


class AppInstanceWithStatus(BaseModel):
    app_instance_status: backend_schemas.ComponentInstanceStatus = Field(..., alias="appInstanceStatus")


class AppInstancesWithStatusResponse(BaseModel):
    app_instances: list[AppInstanceWithStatus] = Field(..., alias="appInstances")


class AppInstanceStatusForSpecSubscription(BaseGraphQLQuery[AppInstancesWithStatusResponse]):
    _query = """
        subscription AppInstanceStatusForSpecSubscription($specId: String!) {
          appInstances(where: {componentSpec: {specId: {_eq: $specId}}}, orderBy: {createdAt: DESC}, limit: 1) {
            appInstanceStatus
          }
        }
    """
    _depends_on = []

    def __init__(self, spec_id: str):
        super().__init__(variables={"specId": spec_id}, response_model=AppInstancesWithStatusResponse)
