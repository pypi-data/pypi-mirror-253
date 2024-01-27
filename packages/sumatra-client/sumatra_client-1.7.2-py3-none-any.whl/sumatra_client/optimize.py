from typing import Optional
from sumatra_client.client import Client


class OptimizeClient(Client):
    def __init__(
        self,
        instance: Optional[str] = None,
        branch: Optional[str] = None,
        workspace: Optional[str] = None,
    ):
        super().__init__(
            instance=instance,
            branch=branch,
            workspace=workspace,
        )

    def create_audience(
        self,
        name: str,
        description: Optional[str] = None,
        rule: Optional[dict] = None,
    ) -> str:
        query = """
            mutation CreateAudience($name: String!, $description: String, $rule: JSON) {
                createAudience(name: $name, description: $description, rule: $rule) {
                    slug
                }
            }
        """
        ret = self._execute_graphql(
            query=query,
            variables={"name": name, "description": description, "rule": rule},
        )
        return ret["data"]["createAudience"]["slug"]

    def get_audience(self, slug: str) -> dict:
        query = """
            query GetAudience($slug: String!) {
                audience(slug: $slug) {
                    slug
                    name
                    description
                    rule
                }
            }
        """
        ret = self._execute_graphql(
            query=query,
            variables={"slug": slug},
        )
        return ret["data"]["audience"]

    def list_audiences(self) -> list[dict]:
        query = """
            query ListAudiences {
                audiences(first: 100) {
                    nodes {
                        slug
                        name
                        description
                        rule
                    }
                }
            }
        """
        ret = self._execute_graphql(
            query=query,
        )
        return ret["data"]["audiences"]["nodes"]

    def get_audience_inputs(self) -> list[dict]:
        query = """
            query GetAudienceInputs {
                audienceInputs {
                    name
                    operators
                }
            }
        """
        ret = self._execute_graphql(
            query=query,
        )
        return ret["data"]["audienceInputs"]

    def delete_audience(self, slug: str) -> None:
        query = """
            mutation DeleteAudience($slug: String!) {
                deleteAudience(slug: $slug) {
                    slug
                }
            }
        """
        self._execute_graphql(
            query=query,
            variables={"slug": slug},
        )

    def create_optimization(
        self,
        name: str,
        rootPage: str,
        holdout_percentage: float = 0,
        description: Optional[str] = None,
    ) -> str:
        query = """
            mutation CreateOptimization($name: String!, $rootPage: String!, $holdoutPercentage: Float!, $description: String) {
                putOptimization(name: $name, rootPage: $rootPage, holdoutPercentage: $holdoutPercentage, description: $description) {
                    id
                }
            }
        """
        ret = self._execute_graphql(
            query=query,
            variables={
                "name": name,
                "rootPage": rootPage,
                "description": description,
                "holdoutPercentage": holdout_percentage,
            },
        )
        return ret["data"]["putOptimization"]["id"]

    def delete_optimization(self, id):
        query = """
            mutation DeleteOptimization($id: String!) {
                deleteOptimization(id: $id) {
                    id
                }
            }
        """
        self._execute_graphql(
            query=query,
            variables={"id": id},
        )

    def get_optimization(self, id):
        query = """
            query GetOptimization($id: String!) {
                optimization(id: $id) {
                    id
                    slug
                    name
                    description
                    rootPage
                    holdoutPercentage
                }
            }
        """
        ret = self._execute_graphql(
            query=query,
            variables={"id": id},
        )
        return ret["data"]["optimization"]

    def list_optimizations(self):
        query = """
                query ListOptimizations {
                    optimizations(first: 10) {
                        nodes {
                            id
                            name
                            slug
                            holdoutPercentage
                            rootPage
                        }
                    }
                }
            """
        ret = self._execute_graphql(
            query=query,
        )
        return ret["data"]["optimizations"]["nodes"]

    def get_goals(self, optimization_id: str) -> list[dict]:
        query = """
            query GetGoals($optimizationId: String!) {
                optimization(id: $optimizationId) {
                    goal {
                        type
                        name
                        value
                        path
                    }
                }
            }
        """
        ret = self._execute_graphql(
            query=query,
            variables={"optimizationId": optimization_id},
        )
        return ret["data"]["optimization"]["goal"]

    def create_experience(
        self, optimization_id: str, name: str, audience: str = "everyone"
    ) -> dict:
        query = """
                mutation CreateExperience($optimizationId: String!, $name: String!, $audience: String!) {
                    createExperience(
                        optimizationId: $optimizationId
                        audiences: [$audience]
                        variants: [{name: "Default", overrides: []}]
                        name: $name
                    ) {
                        ...ExperienceParts
                    }
                }

                fragment ExperienceParts on Experience {
                    id
                    status
                }
        """
        ret = self._execute_graphql(
            query=query,
            variables={
                "optimizationId": optimization_id,
                "name": name,
                "audience": audience,
            },
        )
        return ret["data"]["createExperience"]["id"]

    def list_experiences(self, optimization_id: str) -> list[dict]:
        query = """
                query ListExperiences($optimizationId: String!) {
                    optimization(id: $optimizationId) {
                        experiences {
                            ...ExperienceParts
                        }
                    }
                }

                fragment ExperienceParts on Experience {
                    id
                    name
                    slug
                    status
                    experimentId
                    audiences {
                        ...AudienceParts
                    }
                    variants {
                        ...VariantParts
                    }
                }

                fragment AudienceParts on Audience {
                    slug
                    name
                }

                fragment VariantParts on Variant {
                    name
                    slug
                    percentage
                    overrides {
                        path
                        selector
                        type
                        value
                        xPath
                    }
                }
        """
        ret = self._execute_graphql(
            query=query,
            variables={"optimizationId": optimization_id},
        )
        return ret["data"]["optimization"]["experiences"]

    def get_experience(self, optimization_id: str, experience_id: str) -> dict:
        query = """
                query GetExperience($optimizationId: String!, $experienceId: String!) {
                    optimization(id: $optimizationId) {
                        experience(id: $experienceId) {
                            ...ExperienceParts
                        }
                    }
                }

                fragment ExperienceParts on Experience {
                    id
                    name
                    slug
                    status
                    experimentId
                    audiences {
                        ...AudienceParts
                    }
                    variants {
                        ...VariantParts
                    }
                }

                fragment AudienceParts on Audience {
                    slug
                    name
                }

                fragment VariantParts on Variant {
                    name
                    slug
                    percentage
                    overrides {
                        path
                        selector
                        type
                        value
                        xPath
                    }
                }

                """
        ret = self._execute_graphql(
            query=query,
            variables={
                "optimizationId": optimization_id,
                "experienceId": experience_id,
            },
        )
        return ret["data"]["optimization"]["experience"]

    def update_experience(
        self,
        optimization_id: str,
        experience_id: str,
        status: Optional[str] = None,
        audience: Optional[str] = None,
    ):
        query = """
                mutation UpdateExperience($optimizationId: String!, $experienceId: String!, $status: String, $audiences: [String]) {
                    updateExperience(
                        optimizationId: $optimizationId
                        experienceId: $experienceId
                        status: $status
                        audiences: $audiences
                    ) {
                        ...ExperienceParts
                    }
                }

                fragment ExperienceParts on Experience {
                    id
                    status
                }
        """
        ret = self._execute_graphql(
            query=query,
            variables={
                "optimizationId": optimization_id,
                "experienceId": experience_id,
                "status": status,
                "audiences": [audience] if audience else None,
            },
        )
        return ret["data"]["updateExperience"]

    def delete_experience(self, optimization_id: str, experience_id: str):
        query = """
                mutation DeleteExperience($optimizationId: String!, $experienceId: String!) {
                    deleteExperience(optimizationId: $optimizationId, experienceId: $experienceId) {
                        id
                    }
                }
        """
        self._execute_graphql(
            query=query,
            variables={
                "optimizationId": optimization_id,
                "experienceId": experience_id,
            },
        )
