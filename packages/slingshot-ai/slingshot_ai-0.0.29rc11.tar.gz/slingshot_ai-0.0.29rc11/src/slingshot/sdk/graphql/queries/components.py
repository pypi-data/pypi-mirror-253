from __future__ import annotations

from pydantic import BaseModel, Field

from ..base_graphql import BaseGraphQLQuery
from ..fragments import ComponentSpec


class ComponentSpecsForProjectResponse(BaseModel):
    component_specs: list[ComponentSpec] = Field(..., alias="componentSpecs")


class ComponentSpecsForProjectQuery(BaseGraphQLQuery[ComponentSpecsForProjectResponse]):
    _query = """
        query ComponentSpecsForProject($projectId: String!) {
            componentSpecs(where: {
                project: { projectId: {_eq: $projectId} },
                isArchived: {_eq: false}
            }) {
                ...ComponentSpec
            }
        } """

    _depends_on = [ComponentSpec]

    def __init__(self, project_id: str):
        super().__init__(variables={"projectId": project_id}, response_model=ComponentSpecsForProjectResponse)


class ComponentSpecsResponse(BaseModel):
    component_specs: list[ComponentSpec] = Field(..., alias="componentSpecs")


class ComponentSpecByIdQuery(BaseGraphQLQuery[ComponentSpecsResponse]):
    _query = """
        query ComponentSpecQueryByIdQuery($specId: String!, $projectId: String!) {
            componentSpecs(where: {_and: {specId: {_eq: $specId}, projectId: {_eq: $projectId}}}) {
                ...ComponentSpec
           }
        }
    """

    _depends_on = [ComponentSpec]

    def __init__(self, spec_id: str, project_id: str):
        super().__init__(variables={"specId": spec_id, "projectId": project_id}, response_model=ComponentSpecsResponse)


class ComponentSpecByNameQuery(BaseGraphQLQuery[ComponentSpecsResponse]):
    _query = """
        query ComponentSpecByName($specName: String!, $projectId: String!) {
            componentSpecs(where: {_and: {specName: {_eq: $specName}, projectId: {_eq: $projectId}}}) {
                ...ComponentSpec
           }
        }
    """

    _depends_on = [ComponentSpec]

    def __init__(self, spec_name: str, project_id: str):
        super().__init__(
            variables={"specName": spec_name, "projectId": project_id}, response_model=ComponentSpecsResponse
        )
